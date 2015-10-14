# coding: utf-8

def get_params_dict(request):
	params = {}
	for (key,value) in request.args.iteritems():
		params[key] = value
	return params