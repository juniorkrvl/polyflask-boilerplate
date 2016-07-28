# In this file we can use some general API calls
# It will work like the center of application 
# but registered normally through blueprint

from flask import Blueprint
core = Blueprint('core', __name__)

@core.route('/')
def main():
    return 'Hello Main'