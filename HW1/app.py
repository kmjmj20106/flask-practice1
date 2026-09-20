from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/profile")
def profile():
  hobby=["기타치기","클라이밍","음악감상"]
  return render_template('profile.html',hobby=hobby)

@app.route("/greet/<name>")
def greet(name):
  return render_template('greet.html',name = name)

if __name__ == "__main__":
  app.run(debug=True)