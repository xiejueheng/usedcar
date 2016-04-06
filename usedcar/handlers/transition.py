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
from ..forms import TransitionAddForm
from ..utils import requtils
from ..helpers import force_int
from ..models import SalesVehicle,Brand,VehicleType,VehicleStyle,VehicleTransition,db

__all__ = ['bp']

bp = Blueprint('transitions', __name__)
run_path = os.getcwd()

"""车务办理"""
@bp.route('/add', methods=['GET','POST'])
def add():
	form = TransitionAddForm(request.args)
	if form.validate():
		vehible = form.save()
		print vehible
		js = {'code':0}
		return '%s(%s)' %('window.transition.add',json.dumps(js))
	else:
		js = {'code':508, 'data':form.errors}
		return '%s(%s)' %('window.transition.add',json.dumps(js))

"""查询已有“车务办理”信息"""
@bp.route('/query', methods=['GET','POST'])
def query():
	submitDate = request.args.get('submitDate')
	if not submitDate:
		return abort(404)

	s_time = time.strptime(submitDate,'%Y%m')
	end_timestamp = int(time.mktime( s_time ))
	dt = datetime.datetime.strptime(submitDate,'%Y%m')
	start_timestamp = int(time.mktime(datetime.date(dt.year,dt.month-1,1).timetuple()))
	q = db.session.query(VehicleTransition)
	#car_list = list(VehicleTransition.query.filter_by(timestamp=timestamp))
	car_list=q.filter(and_(VehicleTransition.timestamp>=start_timestamp, VehicleTransition.timestamp<=end_timestamp).all())
	json_list = []

	for c in car_list:
		json_list.append(c.json())

	js = {'code':0,'list':json_list}
	return '%s(%s)' %('window.transition.query',json.dumps(js)) 