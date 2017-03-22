from flask import Flask
from models import db

app = Flask(__name__)
db.init_app(app)

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

