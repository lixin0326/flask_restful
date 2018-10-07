# 路由系统
from flask_restful import Api

from apps.arg.api import Demo
from apps.main.apis import IndexApi
from apps.test.apis import HomeheadApi, HomedataApi

api = Api(prefix='/api/v1')  # 前缀


def init_api(app):
    api.init_app(app)


# 注册路由系统
api.add_resource(IndexApi, '/')
api.add_resource(HomeheadApi, '/home/head/')
api.add_resource(HomedataApi, '/home/list/')
api.add_resource(Demo, '/args/base/')
