# coding=utf-8

from flask import Flask, request
from flask.ext import restful as rst
from flask_restful import reqparse, abort
import orchestrator

app = Flask(__name__)
api = rst.Api(app)

DATA = {
    "data1": {"url": "jasonliu.rocks/static/swag.jpg"}
}

parser = reqparse.RequestParser()
parser.add_argument('url', type=str)


def abort_if_todo_doesnt_exist(id):
    if id not in DATA:
        abort(404, message="{} doesn't exist".format(id))

class Api(rst.Resource):
    def get(self, id):
        abort_if_todo_doesnt_exist(id)
        return DATA[id]

    def delete(self, id):
        abort_if_todo_doesnt_exist(id)
        del DATA[id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        url = {'url': args['url']}
        DATA[id] = url
        return url, 201

# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class ApiList(rst.Resource):
    def get(self):
        return DATA

    def post(self):
        args = parser.parse_args()
        id = 'data%d' % (len(DATA) + 1)
        DATA[id] = {'url': args['url']}
        return DATA[id], 201

def classify():
    """
    Accept post request and run orchestration
    :return: classification object
    """
    url = Api.get()
    return orchestrator.run(url)

api.add_resource(ApiList, '/api')
api.add_resource(Api, '/api/<string:id>', endpoint='api-ep')



if __name__ == "__main__":
    app.run(debug=True)
    classify()