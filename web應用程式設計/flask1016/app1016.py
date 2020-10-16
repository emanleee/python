from flask import Flask,render_template,request,jsonify,send_file,make_response,url_for
import numpy as np
import cv2
import base64
import os
import datetime

app=Flask(__name__)

# @app.route('/2')
# def index2():
#     return 'hi'

@app.route('/')
def index():
    # 顯示表單
    return render_template('form1016.html')


@app.route('/test',methods=['GET','POST'])
def test():
    return jsonify({
        'request.values.get()':request.values.get('name'),
        'request.args.get()':request.args.get('name'),
        'request.form.get()':request.form.get('name'),
        'request.json.get()':request.json.get('name')
    })

@app.route('/json',methods=['GET','POST'])
def json():
    name = request.args.get('name')
    return jsonify({
        'name':name
    })

@app.route('/file',methods=['POST'])
def file():
    return send_file('cat.jpg')

@app.route('/aaa', methods=['POST'])
def process():
    # 處理圖片
    return 'Process'


@app.route('/66', methods=['POST'])
def process2():
    # 取得上傳的圖片
    file1 = request.files['image1']
    # 讀取檔案內容
    file1_content = file1.read()
    # 將檔案內容轉為 Numpy Array
    npimg1 = np.fromstring(file1_content, np.uint8)
    # 將 Numpy Array 進行圖像解碼
    bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
    return jsonify(bgr1.shape)


@app.route('/', methods=['POST'])
def process3():
    # 取得上傳的圖片
    file1 = request.files['image1']
    # 讀取檔案內容
    file1_content = file1.read()
    # 將檔案內容轉為 Numpy Array
    npimg1 = np.fromstring(file1_content, np.uint8)
    # 將 Numpy Array 進行圖像解碼
    bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
    
    
    line_color_hex = request.form.get('line_color').lstrip('#')
    line_color_rgb = tuple(int(line_color_hex[i:i+2], 16) for i in (0, 2, 4))
    line_thickness = int(request.form.get('line_thickness'))


    rgb1 = cv2.cvtColor(bgr1, cv2.COLOR_BGR2RGB) 
    height, width = rgb1.shape[:2]
    radius = int(min(height, width) * 0.48)
    thickness = int(min(height, width) * 0.01 *
      line_thickness)
    cv2.circle(rgb1, (int(width / 2), int(height / 2)),
               radius, line_color_rgb, thickness)

    bgr1 = cv2.cvtColor(rgb1, cv2.COLOR_BGR2RGB)

    #base64編碼回傳
    # response = {
    #     'output_image': base64.b64encode(cv2.imencode('.jpg', bgr1)[1]).decode()
    # }

    #原圖回傳
    # _, buffer = cv2.imencode('.jpg', bgr1)
    # response = make_response(buffer.tobytes())
    # response.mimetype = 'image/jpg'

    #網址回傳
    # folderPath = 'static/output_image'
    # if not os.path.exists(folderPath):
    #     os.makedirs(folderPath)
    # filename = '{}.jpg'.format(
    #     datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # )
    # cv2.imwrite(os.path.join(folderPath, filename), bgr1)
    # response = {
    #     'url': url_for('static', filename='output_image/{}'.format(filename), _external=True)
    # }

    # return response

    base64_image = base64.b64encode(cv2.imencode('.jpg', bgr1)[1]).decode()
    return render_template('show_image.html', base64_image=base64_image)
