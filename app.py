from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# a simple page
@app.route('/sample1/')
@app.route('/sample1/<name>')
def sample1(name=None):
    return render_template('sample1/hello.html', name=name, surname=name)


# a basic simple of usage extends
@app.route('/sample2')
def sample2():
    return render_template('sample2/home.html')


# a basic simple of usage include
@app.route('/sample3')
def sample3():
    return render_template('sample3/body.html')


# a basic simple of usage include
@app.route('/sample4')
def sample4():
    return render_template('sample4/index.html')


app.config["DEBUG"] = True
app.run()
