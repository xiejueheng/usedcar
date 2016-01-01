# coding: utf-8

import os
import os.path
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, abort, jsonify
from flask.ext.babel import gettext as _
from ..forms import AddForm
from ..utils import requtils
from ..models import SalesVehicle,Brand

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
	读取品牌文件
	"""
	brand_file_path = os.path.join(run_path,'data/brand.txt')
	file_obj = open(brand_file_path,'r')
	list_of_all_lines = file_obj.readlines()
	#return '<br>'.join(list_of_all_lines)
	brand_map = {}
	for line in list_of_all_lines:
		line = line.strip('\r\n')
		b_dict = {}
		b_dict['name']=unicode(line,'utf-8')
		b=Brand(**b_dict).save()
		brand_map[b.name]=b.id

	#brand_list = list(Brand.query.all())
	#print brand_map
	
