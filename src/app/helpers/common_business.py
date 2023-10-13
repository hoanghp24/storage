
# Create your custom here.



# used for direct action
def get_data(request, is_form_data = False):
	if is_form_data:
		request.data._mutable = True
	data = request.data
	data["company_id"] = request.headers['X-Company-Id']
	return data


# used for action from raw data
def get_querystring(request, list_querystring=[]):
	list_data_resp = {}
	company_id = request.headers['X-Company-Id']
	limit = int(request.GET.get('limit', 100))
	page = int(request.GET.get('page', 1))
	offset = int(page-1)*limit
	list_data_resp['limit'] = limit
	list_data_resp['offset'] = offset
	list_data_resp['page'] = page
	for query_string in list_querystring:
		data = request.GET.get(query_string, None)
		list_data_resp[query_string] = data
	
	return company_id, list_data_resp
