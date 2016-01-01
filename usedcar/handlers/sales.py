# coding: utf-8

import os
import os.path
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, abort, jsonify
from flask.ext.babel import gettext as _
from ..forms import AddForm
from ..utils import requtils
from ..models import SalesVehicle,Brand,VehicleType

__all__ = ['bp']

bp = Blueprint('sales', __name__)
run_path = os.getcwd()

"""
5.1.	我要卖车
"""
@bp.route('/add', methods=['GET','POST'])
def add():
	"""
	form = AddForm()
	if form.validate_on_submit():
		salesVehicle = form.save()
		print salesVehicle
		return "haha"
	"""
	params = requtils.get_params_dict(request)
	salesVehicle = SalesVehicle(**params)
	sv = salesVehicle.save()
	js = {'code':0}
	print sv
	return jsonify(**js)
	#return abort(403)

@bp.route('/test', methods=['GET','POST'])
def test():
	print SalesVehicle.query.all()
	print SalesVehicle.query.order_by(SalesVehicle.id).all()
	print SalesVehicle.query.first()
	return ""

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
			#print t_dict, brand_map[t_dict.get('brand_name')]
			t_dict['brand_id'] = brand_map.get(t_dict.get('brand_name',0),0)
			print t_dict
			t = VehicleType(**t_dict).save()
			type_map[t.name] = t.id
	finally:
		file_obj.close()

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
