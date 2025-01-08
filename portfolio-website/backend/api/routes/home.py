from . import main

@main.route('/', methods=['GET'])
def index():
    return {"message": "Welcome to the Portfolio Website!"}
