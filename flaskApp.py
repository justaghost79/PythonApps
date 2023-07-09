from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Welcome to the jungle, baby!</h1><p>Under Construction</p>"
@app.route('/aboutMe')
def aboutMe():
    return "About me!"
if __name__ == '__main__':
    app.run()
