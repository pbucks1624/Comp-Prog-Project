from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<Patty>')
def hello(Patty):
    return render_template('page.html', Patty=Patty)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/instagram")
def insta():
    return render_template('insta.html')

@app.route("/youtube")
def yt():
    return render_template('yt.html')

@app.route("/xbox")
def xbox():
    return render_template('xbox.html')

@app.route("/twitch")
def twitch():
    return render_template('twitch.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')