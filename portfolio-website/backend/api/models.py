from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = "mongodb://mongodb:27017/portfolio"
    mongo.init_app(app)
