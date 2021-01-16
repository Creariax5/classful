from flask import render_template, request


def run(web_server):
    @web_server.app.route("/", methods=["POST"])
    def index():
        data = request.get_json()
        op = data.get('operation')

        return op ** 2
