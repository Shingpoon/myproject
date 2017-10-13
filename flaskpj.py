from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
import sqlite3

app = Flask('shing')

app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/<value>')
def test(value):
    return 'test world %s' % value


# 规定参数类型 int methods 接收方法
@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    if request.method == 'POST':
        result = 'Post int %d' % post_id
    else:
        result = 'Get int %d' % post_id

    # show the post with the given id, the id is an integer
    return result


# 重写参数类型 string
@app.route('/post/<string:post_id_str>')
def show_post2(post_id_str):
    # show the post with the given id, the id is an integer
    return 'Post str %s' % post_id_str


@app.route('/template/')
@app.route('/template/<name>')
def template(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
