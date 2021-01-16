from flask import Flask, session, redirect, url_for, escape, request, make_response, render_template
app = Flask(__name__)
app.secret_key = 'any random string'

def run(web_server):
    @web_server.app.route("/")
    def index():
        if 'username' in session:
            username = session['username']
            return render_template("readcookie.html")
        return render_template("index.html")


    @web_server.app.route('/setcookie', methods=['POST', 'GET'])
    def setcookie():
        if request.method == 'POST':
            user = request.form['nm']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp

    @app.route('/')
    def logout():
        # remove the username from the session if it is there
        session.pop('username', None)
        return redirect(url_for('index'))


    @web_server.app.route('/getcookie')
    def getcookie():
        name = request.cookies.get('userID')
        return '<h1>welcome ' + name + '</h1>'
