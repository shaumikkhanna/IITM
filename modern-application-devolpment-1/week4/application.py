from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('get-details.html')
	elif request.method == 'POST':
		username = request.form['user_name']
		return render_template('display-details.html', display_name=username)

if __name__ == '__main__':
	app.run(debug=True)
