from flask import Flask ,render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index1008.html')

@app.route('/')
def query():
    name=request.args.get('name')
    return 'Hello, {}!'.format(name)
    