# coding: utf-8

import os
import os.path
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, abort, jsonify
from flask import json
from flask.ext.babel import gettext as _
from ..forms import AddForm,AppraiseForm,IndividualForm,ReplaceForm,AgencyForm
from ..utils import requtils
from ..helpers import force_int
from ..models import SalesVehicle,Brand,VehicleType,VehicleStyle,db

__all__ = ['bp']

bp = Blueprint('sales', __name__)
run_path = os.getcwd()

"""
6.1.我要卖车
"""
@bp.route('/add', methods=['GET','POST'])
def add():
	
	form = AddForm(request.args)
	if form.validate():
	#print form.errors
		salesVehicle = form.save()
		print salesVehicle
		js = {'code':0}
		return '%s(%s)' %('window.usedcar.add',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.usedcar.add',json.dumps(js))

"""
6.2.鉴定评估车辆
"""
@bp.route('/appraise', methods=['GET','POST'])
def appraise():
	form = AppraiseForm(request.args)
	if form.validate():
		salesVehicle = form.save()
		print salesVehicle
		js = {'code':0}
		return '%s(%s)' %('window.usedcar.appraise',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.usedcar.appraise',json.dumps(js))

"""
6.3.出售车辆（不需要预约）
"""
@bp.route('/individual', methods=['GET','POST'])
def individual():
	form = IndividualForm(request.args)
	if form.validate():
		salesVehicle = form.save()
		print salesVehicle
		js = {'code':0}
		return '%s(%s)' %('window.usedcar.individual',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.usedcar.individual',json.dumps(js))

"""
6.4.出售车辆（置换卖）
"""
@bp.route('/replace', methods=['GET','POST'])
def replace():
	form = ReplaceForm(request.args)
	if form.validate():
		salesVehicle = form.save()
		print salesVehicle
		js = {'code':0}
		return '%s(%s)' %('window.usedcar.replace',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.usedcar.replace',json.dumps(js))

"""
6.5.出售车辆（经销商代理）
"""
@bp.route('/agency', methods=['GET','POST'])
def agency():
	form = AgencyForm(request.args)
	if form.validate():
		salesVehicle = form.save()
		print salesVehicle
		js = {'code':0}
		return '%s(%s)' %('window.usedcar.agency',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.usedcar.agency',json.dumps(js))

"""6.6.查询卖车信息"""
@bp.route('/query', methods=['GET','POST'])
def query():
	salesType = force_int(request.args.get('salesType'))
	submitDate = force_int(request.args.get('submitDate'))

	if not salesType or not submitDate:
		return abort(404)

	"""
	q = db.session.query(SalesVehicle)
	q.filter(SalesVehicle.sales_type==salesType)
	car_list = list(q.all())
	"""

	car_list=list(SalesVehicle.query.filter_by(sales_type=salesType,timestamp=submitDate))
	json_list = []

	for c in car_list:
		json_list.append(c.json())

	js = {'code':0,'list':json_list}
	return '%s(%s)' %('window.sales.query',json.dumps(js)) 



@bp.route('/load', methods=['GET','POST'])
def load():
	"""
	读取品牌brand.txt
	"""
	brand_file_path = os.path.join(run_path,'data/brand.txt')
	file_obj = open(brand_file_path,'r')
	brand_map = {}
	
	try:
		list_of_all_lines = file_obj.readlines()
		#return '<br>'.join(list_of_all_lines)
		for line in list_of_all_lines:
			line = line.strip('\r\n')
			b_dict = {}
			b_dict['name']=unicode(line,'utf-8')
			print b_dict
			b=Brand(**b_dict).save()
			brand_map[b.name]=b.id
	finally:
		file_obj.close()
	#brand_list = list(Brand.query.all())
	#print brand_map
	"""
	读取车型type.txt
	"""
	type_file_path = os.path.join(run_path,'data/type.txt')
	file_obj = open(type_file_path,'r')
	type_map = {}
	
	try:
		list_of_all_lines = file_obj.readlines()
		for line in list_of_all_lines:
			line = line.strip('\r\n')
			t_dict = get_type_dict(line)
			t_dict['brand_id'] = brand_map.get(t_dict.get('brand_name',0),0)
			t = VehicleType(**t_dict).save()
			#print t_dict
			type_map[t.name] = t.id
	finally:
		file_obj.close()

	"""
	读取车款detail.txt
	"""
	detail_file_path = os.path.join(run_path,'data/detail.txt')
	file_obj = open(detail_file_path,'r')
	
	try:
		list_of_all_lines = file_obj.readlines()
		for line in list_of_all_lines:
			line = line.strip('\r\n')
			d_dict = get_detail_dict(line)
			d_dict['typeId'] = type_map.get(d_dict.get('type_name',''),0)
			print d_dict
			VehicleStyle(**d_dict).save()
	finally:
		file_obj.close()
	
	return 'OK'

def get_detail_dict(line):
	detail_line_arrays = line.split(',')
	brand_name = to_unicode(detail_line_arrays[0])
	type_name = to_unicode(detail_line_arrays[1])
	style_name = to_unicode(detail_line_arrays[2])
	produce_year = detail_line_arrays[3]

	if not str(produce_year)  == '':
		produce_year = int(produce_year)	

	displacement = to_unicode(detail_line_arrays[4])
	transmission = get_transmission(detail_line_arrays[5])

	seat = detail_line_arrays[6]
	if not str(seat) == '':
		seat = int(seat)
	else:
		seat = 5

	body_model = get_body_model(detail_line_arrays[7])
	gear = detail_line_arrays[8]
	
	if gear == 'CV':
		gear = 0
	elif not str(gear) == '':
		gear = int(gear[0])
	else:
		gear = 0

	gate = detail_line_arrays[9]
	if not str(gate) == '':
		gate = int(gate)
	else:
		gate = 4

	d_dict = {}
	d_dict['type_name'] = type_name
	d_dict['name'] = style_name
	d_dict['produce_year'] = produce_year
	d_dict['displacement'] = displacement
	d_dict['transmission'] = transmission
	d_dict['seat'] = seat
	d_dict['body_model'] = body_model
	d_dict['gear'] = gear
	d_dict['gate'] = gate

	return d_dict
	
def get_body_model(text):
	if u'两厢车' == text:
		return 1
	elif u'三厢车' == text:
		return 2
	elif u'SUV' == text:
		return 3
	elif u'MPV' == text:
		return 4
	elif u'皮卡' == text:
		return 5
	else:
		print 'body_model=%s' %text
		return 0

def get_transmission(text):
	if u'手动' == text:
		return 1
	elif u'自动' == text:
		return 2
	elif u'手自一体' == text:
		return 3
	elif u'双离合' == text:
		return 4
	elif text.find(u'E-CVT无级变速') > -1:
		return 5
	elif text.find(u'T无级变速') > -1:
		return 6
	else:
		print 'transmission = %s' %text
		return 0

"""
提取车型内容
"""
def get_type_dict(line):
	type_line_arrays = line.split(',')
	brand_name = to_unicode(type_line_arrays[0])
	type_name = to_unicode(type_line_arrays[1])
	price_range = to_unicode(type_line_arrays[2])
	displacements = to_unicode(type_line_arrays[3])
	transmissions = to_unicode(type_line_arrays[4])
	
	t_dict = {}
	t_dict['brand_name'] = brand_name
	t_dict['name'] = type_name
	t_dict['price_range'] = price_range
	t_dict['displacements'] = displacements
	t_dict['transmissions'] = transmissions 
	return t_dict

def to_unicode(line):
	return unicode(line,'utf-8')
