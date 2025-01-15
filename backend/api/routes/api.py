from . import main

@main.route('/api', methods=['GET'])
def api_home():
    return {"message": "Welcome to the Portfolio API!"}
