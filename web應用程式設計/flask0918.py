from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!48763'


@app.route('/helloo')  # 新增路由 在網址後加上hello進入另一個葉面
def hello_world2():
    return 'Hello!'


@app.route('/hello/<name>')  # 在hello頁面後加上/後的參數會顯示在頁面
def hello(name):
    return 'Hello, {}!'.format(name)


@app.route('/hello', defaults={'name': 'Someone'})  # 同上，但在沒有打東西時有預設值Someone
@app.route('/hello/<name>')
def hello3(name):
    return 'Hello, {}!'.format(name)


@app.route('/<int:num>')
def get_integer(num):
    return 'Integer: {}'.format(num)

@app.route('/<float:num>')
def get_float(num):
    return 'Float: {}'.format(num)
