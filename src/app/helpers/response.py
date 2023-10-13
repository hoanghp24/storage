from django.utils.translation import gettext as _
import sys

#django restframework
from rest_framework.response import Response

#helpers
from app.helpers import messsage_code

# Create your custom here.



def GetSuccess(data, message='get data success',  dev_message='', page_info={}):
    if page_info != {}:
        response = {
            'success': True,
            'message': message,
            'message_code': messsage_code.GET_DATA_SUCCESS_CODE,
            'status_code': 200,
            'dev_message': dev_message,
            'data': data,
            'page_info': page_info,
        }
    else:
        response = {
            'success': True,
            'message': message,
            'message_code': messsage_code.GET_DATA_SUCCESS_CODE,
            'status_code': 200,
            'dev_message': dev_message,
            'data': data,
            
        }
    return Response(response)

def CreateSuccess(data, message='create data success',  dev_message=''):
    response = {
        'success': True,
        'message': message,
        'message_code': messsage_code.CREATE_DATA_SUCCESS_CODE,
        'status_code': 201,
        'dev_message': dev_message,
        'data': data,
    }
    return Response(response)

def UpdateSuccess(data, message='update data success',  dev_message=''):
    response = {
        'success': True,
        'message': message,
        'message_code': messsage_code.UPDATE_DATA_SUCCESS_CODE,
        'status_code': 200,
        'dev_message': dev_message,
        'data': data,
    }
    return Response(response)

def DeleteSuccess(message='delete data success',  dev_message=''):
    response = {
        'success': True,
        'message': message,
        'message_code': messsage_code.DELETE_DATA_SUCCESS_CODE,
        'status_code': 200,
        'dev_message': dev_message,
        'data': [],
    }
    return Response(response)

def BadRequest(data, message_code='', dev_message=''):
    response = {
        'success': False,
        'message': "bad request",
        'message_code': messsage_code.BAD_REQUEST_CODE,
        'status_code': 400,
        'dev_message': dev_message,
        'data': data
    }
    return Response(response)

def NotFound(message_code='', dev_message=''):
    response = {
        'success': False,
        'message': "data not found",
        'message_code': messsage_code.DATA_NOT_FOUND_CODE,
        'status_code': 404,
        'dev_message': dev_message,
        'data': []
    }
    return Response(response)

def ServerError(dev_message=''):
    response = {
        'success': False,
        'message': "server error",
        'status_code': 500,
        'message_code': messsage_code.SERVER_ERROR_CODE,
        'dev_message': dev_message,
        'data': []
    }
    return Response(response)

def Unauthorized(message_code='', dev_message=''):
    
    response = {
        'success': False,
        'message': "unauthorized",
        'status_code': 401,
        'message_code': messsage_code.UNAUTHORIZED_CODE,
        'dev_message': dev_message,
        'data': []
    }
    return Response(response)

def page_info_pagination(request_data, query_set):
        limit = 100
        page = 1
        if 'limit' in request_data:
            limit = int(request_data['limit'])
        if 'page' in request_data:
            page = int(request_data['page'])
        offset = (page - 1) * limit
        total = query_set.count()
        result = query_set[offset:offset+limit]
        pageInfo = {
            'total': total,
            'limit': limit,
            'offset': offset,
            'page': page,
        }
        return result, pageInfo


# page info 
def result_page_info(total, limit, offset, page):
	pageInfo = {
            'total': total,
            'limit': limit,
            'offset': offset,
            'page': page,
    }
	return pageInfo

def result_info(total):
	pageInfo = {
		'total': total
    }
	return pageInfo


