#hi this project is for db visualization
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello welcome to db visulizer'

if __name__ == '__main__':
    app.run()