from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html', number=3)

@app.route('/play/<int:count>')
def playcount(count):
    return render_template('count.html', count=count)

@app.route('/play/<int:count>/<string:color>')
def playcolorcount(count, color):
    return render_template('color.html', count=count, color=color)

if __name__=="__main__":

    app.run(debug=True)
