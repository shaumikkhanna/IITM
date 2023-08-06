from functools import wraps
import uuid
from flask import Flask, request, jsonify, render_template, Response,make_response
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta
from BlogApp.exceptions import AuthError, NotFoundError, ValidationError, InternalError
from BlogApp.jwtSetup import auth_required,get_username_with_token,get_token
from flask_migrate import Migrate
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from celery import Celery
from flask_mail import Mail
from celery.schedules import crontab
from flask_mail import Message


app = Flask(__name__)
app.config['enable_utc'] = False
app.config['timezone'] = 'Asia/Kolkata'
celery = Celery(app.name, broker='redis://localhost:6379/0')
celery.conf.update(app.config)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogpage.db'
app.config['SECRET_KEY'] = 'secret_key'
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, command='migrate')
cache_config={
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_HOST": "0.0.0.0",
    "CACHE_REDIS_PORT": "6379"
}
cache = Cache(config=cache_config)
cache.init_app(app)

CORS(app)

ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'email', 'token', 'blogs')

class BlogsSchema(ma.Schema):
    class Meta:
        fields = ('id','title', 'content','author_id','image_url','date')

class FollowSchema(ma.Schema):
    class Meta:
        fields = ('id','follower_id','followed_id',"timestamp")


blog_schema_individual = BlogsSchema()
blog_schema = BlogsSchema(many=True)

follow_schema = FollowSchema()
follow_schema = FollowSchema(many=True)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    blogs = db.relationship('Blog', backref='author')

    def __repr__(self):
        return f"<User {self.username}>"

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Add a helper method to retrieve a list of followed users for a given user
    @staticmethod
    def followed_by(user):
        return User.query.join(Follow, Follow.followed_id == User.id).filter(Follow.follower_id == user.id)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_url = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Blog {self.title}>"

# db.drop_all()
db.create_all()


# CELERY TASKS
@celery.task
def send_daily_email(to):
    msg = Message('Daily update', sender='noreply@example.com', recipients=[to])
    msg.body = 'This is your daily update'
    mail.send(msg)

celery.conf.beat_schedule = {
    'send-daily-email': {
        'task': 'new.send_daily_email',
        'schedule': crontab(hour=14, minute=5),
        'args': ('user@example.com',),
    },
}   

@celery.task
def send_pdf_reports(filename,to):
    msg = Message('PDF Report', sender='noreply@example.com', recipients=[to])
    msg.body = 'Please find the attached PDF report'
    msg.attach('monthly_reports.pdf', 'application/pdf', filename)
    with app.app_context():
        mail.send(msg)


# Signup
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully.'}), 201
    except:
        db.session.rollback()
        return jsonify({'message': 'Error creating user.'}), 400

# Login
@app.route('/api/login', methods=['POST'])
def login():
    now = datetime.now()
    data = request.get_json()
    user = User.query.filter_by(email=data['email'], password=data['password']).first()
    if user:
        expirationTime = now + timedelta(hours=24)
        token = jwt.encode(payload={"username" : user.username},key="BlogApp",algorithm='HS256')
        user.token = token
        db.session.commit()
        send_daily_email(user.email)
        return jsonify({'message': 'Login successful.', 'token': token}), 200
    else:
        return jsonify({'message': 'Invalid email or password.'}), 401

# Create blog
@app.route('/api/create_blog', methods=['POST'])
@auth_required
def create_blog():
    username = get_username_with_token()
    user = User.query.filter_by(username=username).first()   #username = username
    if not user:
        return jsonify({'message': 'Unauthorized.'}), 401
    data = request.get_json()
    now = datetime.now()
    new_blog = Blog(title=data['title'], content=data['content'], author_id=user.id,image_url = data['image_url'], date = now)
    # imageurl + date time
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({'message': 'Blog created successfully.'}), 201

    # get blogs

# get all blogs of 1 user
@app.route('/api/<int:author_id>/blogs', methods=['GET'])
@cache.cached(timeout=36000, key_prefix='All Blogs')
@auth_required
def get_user_blogs(author_id):
    user = User.query.get(author_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    blogs = Blog.query.filter_by(author_id=author_id).all()
    # print(blogs)
    blog_list = blog_schema.dump(blogs)
    # blog_list = [blog.to_dict() for blog in blogs]

    return jsonify(blog_list)

# get 1 blog
@app.route('/api/blog/<int:blog_id>', methods=['GET'])
@auth_required
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    blog_data = {}
    blog_data['id'] = blog.id
    blog_data['title'] = blog.title
    blog_data['content'] = blog.content
    blog_data['image_url'] = blog.image_url
    blog_data['date'] = blog.date
    blog_data['author_id'] = blog.author.username
    return jsonify({'blog': blog_data})

# Edit Blogs
@app.route('/api/blog/<int:blog_id>', methods=['PUT'])
@auth_required
def edit_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    if request.headers.get('Content-Type')=='application/json':
            args=json.loads(request.data)
    else:
            args=request.form
    
    blog.title = args["title"]
    blog.content = args["content"]
    blog.image_url = args["image_url"]
    db.session.commit()

    return jsonify({'blog edited': "true"})

# Delete Blog
@app.route('/api/blog/<int:blog_id>', methods=['DELETE'])

@auth_required
def delete_blog(blog_id):
    db.session.query(Blog).filter_by(id=blog_id).delete()
    db.session.commit()
    return jsonify({
        "Blog":"deleted"
    })

# follow 
@app.route('/follow/<string:followed_username>', methods=['POST'])
@auth_required
def follow(followed_username):
    user_id = User.query.filter_by(username = followed_username).first().id
    user_to_follow = User.query.get_or_404(user_id)
    user = get_username_with_token()
    if user == user_to_follow.username:
        return jsonify({'message': 'You cannot follow yourself.'}), 400
    user_details = User.query.filter_by(username = user).first()
    
    if (Follow.query.filter_by(follower_id=user_details.id, followed_id=user_to_follow.id).first() != None):
        return jsonify({'message': 'You are already following this user.'}), 400
    print(type(user_details.id))
    print(type(user_to_follow.id))
    follow = Follow(follower_id=user_details.id, followed_id=user_to_follow.id)
    db.session.add(follow)
    db.session.commit()

    return jsonify({'message': 'You are now following {}.'.format(user_to_follow.username)})

@app.route('/api/unfollow/<string:followed_username>', methods=['POST'])
@auth_required
def unfollow(followed_username):
    user_id = User.query.filter_by(username = followed_username).first().id
    user_to_unfollow = User.query.get_or_404(user_id)
    user = get_username_with_token()
    user_details = User.query.filter_by(username = user).first()
    if (Follow.query.filter_by(follower_id=user_details.id, followed_id=user_to_unfollow.id).first() == None):
        return jsonify({'message': 'You are not following this user.'}), 400

    follow = Follow.query.filter_by(follower_id=user_details.id, followed_id=user_to_unfollow.id).first()
    db.session.delete(follow)
    db.session.commit()

    return jsonify({'message': 'You have unfollowed {}.'.format(user_to_unfollow.username)})

@app.route('/followers/<string:username>')

@auth_required
def followers(username):
    user_id = User.query.filter_by(username=username).first().id
    followers = Follow.query.filter_by(follower_id=user_id).all()
    followings = Follow.query.filter_by(followed_id=user_id).all()
    follower_ids = [follower.followed_id for follower in followers]
    following_ids = [following.follower_id for following in followings]
    follower_names = [User.query.get(follower_id).username for follower_id in follower_ids]
    following_names = [User.query.get(followed_id).username for followed_id in following_ids]
    return jsonify({'Followers' : follower_names, 'Following': following_names})


@app.route('/following/<int:user_id>')

@auth_required
def following(user_id):
    followers = Follow.query.filter_by(follower_id=user_id).all()
    follower_ids = [follower.followed_id for follower in followers]
    follower_names = [User.query.get(follower_id).username for follower_id in follower_ids]
    return jsonify({'Following' : follower_names})


@app.route("/feed", methods=['GET'])

@auth_required
def get_feed():
    user = get_username_with_token()
    print(user)
    user_id = User.query.filter_by(username = user).first().id
    followers = Follow.query.filter_by(follower_id=user_id).all()
    follower_ids = [follower.followed_id for follower in followers]
    blogs = Blog.query.filter(Blog.author_id.in_(follower_ids)).all()
    blog_data = blog_schema.dump(blogs)
    return jsonify(blog_data)


@app.route('/<string:username>')
@auth_required
def get_user_data(username):
    print(username)
    user = User.query.filter_by(username=username).first()
    blogs = Blog.query.filter_by(author_id = user.id).all()
    blogs_json = blog_schema.dump(blogs)
    if not user:
        return jsonify({'error': 'User not found'})
    
    user_data = {
        'username': user.username,
        'email': user.email,
        'id':user.id,
        'blogs': [{
            'title': blog['title'],
            'content': blog['content'],
            'image_url' : blog['image_url'],
            'id': blog['id']
        } for blog in blogs_json]
    }
    
    return jsonify(user_data)

@app.route('/check_user')

@auth_required
def check_user():
    return get_username_with_token()

@app.route('/is_following/<string:followed_username>')

@auth_required
def is_following(followed_username):
    username = get_username_with_token()
    user = User.query.filter_by(username = username).first()
    userid = User.query.filter_by(username = followed_username).first().id
    isFollowing = (Follow.query.filter_by(followed_id = userid, follower_id = user.id).first() != None)
    return jsonify(isFollowing)

@app.route('/search')

@auth_required
def search_user():
    query = request.args.get('q')
    results = User.query.filter(or_(User.username.ilike('%'+query+'%'), User.email.ilike('%'+query+'%')))
    response = []
    for user in results:
        user_data = {
            'id': user.id,
            'username': user.username,
        }
        response.append(user_data)
    return jsonify(response)

import pdfkit


@app.route('/monthly/<string:username>')
@auth_required
def monthly_reports(username):
    user = User.query.filter_by(username=username).first()
    blogs = Blog.query.filter_by(author_id=user.id).all()
    blogs_json = blog_schema.dump(blogs)
    out = render_template('reports.html', blogs=blogs_json)
    options = {
        'orientation': 'landscape',
        'page-size': 'A4',
        'margin-top': '1.0cm',
        'margin-right': '1.0cm',
        'margin-bottom': '1.0cm',
        'margin-left': '1.0cm',
        'encoding': 'UTF-8'
    }
    pdf = pdfkit.from_string(out, options=options)
    send_pdf_reports(pdf, user.email)

    response = make_response('Email sent successfully!')
    response.headers['Content-Type'] = 'text/plain'
    
    return response


@app.route("/download/<int:id>")

def route_download(id):
    blog = Blog.query.get_or_404(id)
    blog_json = blog_schema_individual.dump(blog)
    out = render_template("export.html" , blog=blog_json)
    print(blog_json)
    options = {
        "orientation": "landscape",
        "page-size": "A4",
        "margin-top": "1.0cm",
        "margin-right": "1.0cm",
        "margin-bottom": "1.0cm",
        "margin-left": "1.0cm",
        "encoding": "UTF-8",
    } 
    pdf = pdfkit.from_string(out, options=options)
    headers = {"Content-Disposition": "attachment;filename=blog.pdf"}
    return Response(pdf, mimetype="application/pdf", headers=headers)

if __name__ == '__main__':
    app.run(port=8000,debug=True)



