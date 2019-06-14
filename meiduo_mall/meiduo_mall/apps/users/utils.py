from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.utils import jwt_payload_handler

def jwt_response_payload_handler(token,user=None,request=None):
    return {
        'token':token,
        'id':user.id,
        'username':user.username
    }

def user_payload_handler(user):
    #给字典中添加手机号
    payload = jwt_payload_handler(user)
    payload['mobile'] = user.mobile
    #从字典中删除邮箱
    if 'email' in payload:
        del payload['email']

    return  payload

