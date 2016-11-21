from flask import Flask, request,  render_template, session
from demo1 import com


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    if username != '' and password != '':
        if com.chark(username, password):  # 验证是否存在账户及密码

            return render_template('org.html', username=username)
        else:

            return render_template('index.html')
    else:
        print('用户名或密码为空')
        return render_template('index.html')


@app.route('/reg')
def reg():
    return render_template('reg.html')


@app.route('/reg2', methods=['POST'])
def reg2():
    user = request.form['username']
    pswd = request.form['password']
    pswd2 = request.form['password2']
    if user != '' and pswd != "" and pswd2 != "":
        if pswd == pswd2:

            if com.chark_user(user):
                print('此用户已被注册')
                return render_template('reg.html', methods=['POST'])
            else:
                print(user)
                print(pswd)
                com.insers(user, pswd)
                return render_template('index.html', username=user, methods=['POST'])
        else:
            print('请输入相同密码')
            return render_template('reg.html', methods=['POST'])
    else:
        print('用户名或密码为空')
    return  render_template('reg.html', methods=['POST'])


@app.errorhandler(404)
def err_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def err_500(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host='localhost')
