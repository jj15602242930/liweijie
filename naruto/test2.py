from flask import Flask, request,  render_template


app = Flask(__name__)


# 登陆验证方法
@app.route('/login', methods=['POST'])
def login():
    print("登陆验证")
    username = request.form['username']
    print(username)
    return render_template('index.html')

