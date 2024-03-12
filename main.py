from flask import Flask
import os
import modules
from modules.messages.views import messages_router

app = Flask(__name__)

app.register_blueprint(messages_router, url_prefix='/messages')

@app.route('/')
def index():
    return 'Sever Online'

if __name__ == '__main__':
    app.run("0.0.0.0", port=os.getenv('PORT', 8000),debug=False)
