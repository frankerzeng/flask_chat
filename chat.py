# coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)


@app.route("/")
def helle():
    return "helle dw"


@app.route("/user/<int:user_id>")
def user_info(user_id):
    return render_template('chat.html', name=user_id)


# @app.route("/user/<user_id>")
# def user_info1(user_id):
#     return 'user id = %s' % user_id


@app.route("/sendmsg", methods=['GET', 'POST'])
def send_msg():
    # get
    arg1 = request.args.get('q', '')

    # form 表单
    arg2 = request.form['username']

    return arg1


@app.route("/cookie")
def cookie():
    cook = request.cookies.get('username')

    # cookie
    response = make_response('return cookie')
    response.set_cookie('username', 'zfl')
    app.logger.debug('设置cookie成功')
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
