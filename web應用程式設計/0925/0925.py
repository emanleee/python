from  flask  import  Flask
from  flask  import  render_template
app  =  Flask(__name__)

@app.route('/')
def  index():
    return  render_template('0925index.html')

@app.route('/base')
def  base():
    return  render_template('0925base.html')

@app.route('/page2')
def  page2():
    return  render_template('0925header.html')
