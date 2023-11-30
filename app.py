from flask import Flask, render_template, request
import feedparser, os
import pandas as pd
import Merger
import logging

app = Flask(__name__)
# 로깅 레벨을 DEBUG로 설정
app.logger.setLevel(logging.DEBUG)

# 파일 핸들러를 추가하여 모든 로그를 파일에 기록
file_handler = logging.FileHandler('web.log')
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST','GET'])
def process():
    file = request.files['file']
    if file is None:
        return render_template("index.html")
    '''
    temp_file_path = os.path.join('uploads','temp_uploaded_file.csv')
    print(temp_file_path)
    file.save(temp_file_path)
    df = pd.read_csv(temp_file_path, encoding='utf-8')
    print(df)
    '''
    File = Merger.File(file,file.filename)
    File.extension()
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)