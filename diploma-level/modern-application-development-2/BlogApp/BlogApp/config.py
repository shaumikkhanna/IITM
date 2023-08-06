import os
import redis
basedir = os.path.abspath(os.path.dirname(__file__))

class local_conf: 
    SQLALCHEMY_DATABASE_URI='sqlite:///database.db'
    DEBUG= True
    SQLALCHEMY_TRACK_MODIFICATOINS=True
    BASE_URL="http://localhost:8000"
    SECRET_KEY="QS App"
    CELERY_BROKER_URL="redis://localhost:6379/1"
    CELERY_RESULT_BACKEND="redis://localhost:6379/2"
    PROPAGATE_EXCEPTIONS=True
    CACHE_TYPE="redis"
    CACHE_REDIS_HOST="redis"
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_DB=0
    CACHE_REDIS_URL="redis://localhost:6379/0"
    CACHE_DEFAULT_TIMEOUT=500