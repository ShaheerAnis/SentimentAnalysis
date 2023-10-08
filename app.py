import logging
from Models import db
from flask import Flask
from config import Config
from flask_session import Session
from blueprints.user.user import user_bp

app = Flask(__name__)


app.config.from_object(Config)  

app.jinja_env.autoescape = True


# Configure logging
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=log_format)

# Create a logger instance for your application
logger = logging.getLogger(__name__)




app.register_blueprint(user_bp) 

db.init_app(app)


if __name__ =="__main__":
    app.run(debug=True)
    
