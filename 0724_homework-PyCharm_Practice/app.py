from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     # TODO 나 열심히 할께요
#     return 'Hello World!'
#
#
# @app.route('/a') # python은 기본적으로 함수끼리 2줄씩 띔
# def hello_world2():
#     # TODO 나 열심히 할께요
#     return '<h1>Hello yelyel!</h1>'
#     # return값에는 html 문법이 들어가야함
#
#
# @app.route('/a/b')
# def hello_world3():
#     # TODO 나 열심히 할께요
#     return 'Hello nanana!'
#     # 주소에도 변수의 개념이 들어감 : <>
#
#
# @app.route('/c/<name>') # python은 기본적으로 함수끼리 2줄씩 띔
# def hello_world4(name):
#     # TODO 나 열심히 할께요
#     return '<h1>%s</h1>' %name
#
#
# @app.route('/x') # python은 기본적으로 함수끼리 2줄씩 띔
# def render_world():
#     return render_template('html_tag_1.html')
#
#
# @app.route('/x') # python은 기본적으로 함수끼리 2줄씩 띔
# def render_world():
#     return render_template('python_0703.html')


# @app.route('/<path>') # python은 기본적으로 함수끼리 2줄씩 띔
# def render_world(path = None):
#     if path == 'a':
#         return render_template('html_tag_1.html')
#     elif path == 'b':
#         return render_template('html_tag_1.html')
#     else:
#         return render_template('python_0703.html')

    # if path:
    #     return render_template('%s.html'%path)
    # else:
    #     return render_template('index.html')


# route를 동시에 두개 적어도 됨
# @app.route('/a/<path>')
# @app.route('/<path>')
# def render_practice(path = None):
#     if path:
#         return render_template('%s.html'%path)
#     else:
#         return render_template('index.html')


@app.route('/')
@app.route('/<path>')
def index(path=None):
    if path:
        return render_template('%s.html' % path)
    else:
        return render_template('base.html')


if __name__ == '__main__':
    app.run()


