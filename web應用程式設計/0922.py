from flask import Flask,request,render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/query')
def query():
    name = request.args.get('name')
    return 'Hello, {}!'.format(name)

@app.route('/form')
def form():
    return '''
        <form method="POST" action="/process">
            <label>Input Name: <input type="text" name="name"></label>
            <input type="submit" value="Submit">
        </form>
    '''
    
@app.route('/process', methods=['POST'])
def post_form():
    name = request.form['name']
    return 'Hello, {}!'.format(name)

@app.route('/')
def index():
    return render_template('0922index.html')

@app.route('/48763')
@app.route('/48763/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/loop')
@app.route('/loop/<int:n>')
def loop(n=20):
    return render_template('loop.html',n=n)
    