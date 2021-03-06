# coding: utf-8

import time
import datetime
import os
import os.path
from sqlalchemy.sql import and_
from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, abort, jsonify
from flask import json
from flask.ext.babel import gettext as _
from ..forms import PurchaseAddForm
from ..utils import requtils
from ..helpers import force_int
from ..models import VehiclePurchase,db

__all__ = ['bp']

bp = Blueprint('purchase', __name__)
run_path = os.getcwd()

"""我要买车"""
@bp.route('/add', methods=['GET','POST'])
def add():
	form = PurchaseAddForm(request.args)
	if form.validate():
		vehible = form.save()
		print vehible
		js = {'code':0}
		return '%s(%s)' %('window.purchase.add',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.purchase.add',json.dumps(js))

"""查询已有“车务办理”信息"""
@bp.route('/query', methods=['GET','POST'])
def query():
	submitDate = request.args.get('submitDate')
	if not submitDate:
		return abort(404)

	s_time = time.strptime(submitDate,'%Y%m')
	start_timestamp = int(time.mktime( s_time ))
	dt = datetime.datetime.strptime(submitDate,'%Y%m')
	end_timestamp = int(time.mktime(datetime.date(dt.year,dt.month+1,1).timetuple()))
	q = db.session.query(VehiclePurchase)
	print start_timestamp, end_timestamp
	#car_list = list(VehicleTransition.query.filter_by(timestamp=timestamp))
	car_list=list(q.filter(and_(VehiclePurchase.timestamp>=start_timestamp, VehiclePurchase.timestamp<=end_timestamp)).all())
	json_list = []

	for c in car_list:
		json_list.append(c.json())

	js = {'code':0,'list':json_list}
	return '%s(%s)' %('window.purchase.query',json.dumps(js)) 