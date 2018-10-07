from flask_restful import Resource, fields, marshal_with

from apps.comm.result import Result
from apps.main.models import User

#  djangorestframework
#  ModelSerializer
#  Response()


# 数据json数据格式
# 第一步定义数据格式
user_fields = {
    'uid': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'email': fields.String,
    'phone': fields.Integer,
    'create_date': fields.DateTime,
    'url': fields.String,
}

result = {
    'status': fields.Integer(default=200),
    'msg': fields.String(default='success'),
    'data': fields.List(fields.Nested(user_fields))
}

# 装饰 marshal_with

'''

    status:
    msg:
    data:[]
}
'''


# 接口
class IndexApi(Resource):
    @marshal_with(result)
    def get(self):
        users = User.query.all()
        return {'status': 200, 'msg': 'success', 'data': users}
        # return Result.to_success({
        #     'data': users
        # })
