from flask_restful import reqparse, Resource

"""
参数 restful
1>添加参数
2>在请求中获取参数

参数类型

1>普通参数
2>必要参数
3>一键多值[列表]
4>位置参数
"""


# 　排序　按热度　价格　时间　评论　销量
class Demo(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        """
        arg:传递参数的key
        type:int str 
        help:错误的提示信息
        default:参数默认值
        required 必要
        action 'append'
        location 位置参数 args form files headers
        
        """

        # 添加请求的参数
        # self.parser.add_argument('uid', type=int, default=1)
        # 　添加必要参数
        # self.parser.add_argument('page', type=int, required=True, help='必要参数')

        self.parser.add_argument('ids', type=int, required=True, action='append')

    def get(self):
        # 获得参数 返回的是字典对象
        args = self.parser.parse_args()
        # request.values.get()
        # args.get()
        return u'测试参数'
