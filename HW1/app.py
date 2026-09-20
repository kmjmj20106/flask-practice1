from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/profile")
def profile():
  return render_template('profile.html')

@app.route("/greet/<name1>")
def greet(name1):
  return render_template('greet.html',name = name1)

if __name__ == "__main__":
  app.run(debug=True)