# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for, abort
from flask.ext.babel import gettext as _
from flask import jsonify
from flask import json
from ..models import Brand,VehicleType,VehicleStyle,VehicleInfo,db
from ..helpers import force_int

__all__ = ['bp']

bp = Blueprint('market', __name__)

"""
3.1.	查询品牌列表
/market/getbrandlist

"""
@bp.route('/getbrandlist', methods=['GET', 'POST'])
def getbrandlist():
	brand_list = list(Brand.query.all())
	brand_json_list = []
	for brand in brand_list:
		brand_json_list.append(brand.json())
	return '%s(%s)' %('window.market.getbrandlist',json.dumps({'code':0, 'list':brand_json_list}))

"""
3.2.	查询车系列表
/market/getvehicletype
"""
@bp.route('/getvehicletype', methods=['GET', 'POST'])
def getvehicletype():
	brandId = force_int(request.args.get('brandId'),None)
	if not brandId:
		return abort(404)
	type_list = list(VehicleType.query.filter_by(brand_id=brandId))
	type_json_list = []
	for t in type_list:
		type_json_list.append(t.json())
	return '%s(%s)' %('window.market.getvehicletype',json.dumps({'code':0, 'list':type_json_list}))

"""
3.3.	查询车款列表
/market/getvehiclestyle
"""
@bp.route('/getvehiclestyle', methods=['GET', 'POST'])
def getvehiclestyle():
	typeId = force_int(request.args.get('typeId'), None)
	if not typeId:
		return abort(404)

	style_list = list(VehicleStyle.query.filter_by(type_id=typeId))
	style_json_list = []
	for s in style_list:
		style_json_list.append(s.json())
	return '%s(%s)' %('window.market.getvehiclestyle',json.dumps({'code':0,'list':style_json_list}))

"""
4.4.查询车辆列表
"""
@bp.route('/getlist', methods=['GET', 'POST'])
def getlist():
	query = []
	brandId = force_int(request.args.get('brandId'),None)
	vehicleTypeId = force_int(request.args.get('vehicleTypeId'),None)
	name = request.args.get('name')
	mileage = force_int(request.args.get('mileage'),None)
	transmission = force_int(request.args.get('transmission'),None)
	vehicleAge = force_int(request.args.get('vehicleAge'),None)
	sourceType = force_int(request.args.get('sourceType'),None)
	salesStatus = force_int(request.args.get('salesStatus'),None)

	if not brandId:
		query.append(db.and_(VehicleInfo.brand_id==brandId))

	if not vehicleTypeId:
		query.append(db.and_(VehicleInfo.vehicle_type_id==vehicleTypeId))

	if not name:
		pass

	if not mileage:
		query.append(db.and_(VehicleInfo.mileage<=mileage))

	if not transmission:
		#query.append(db.and_(VehicleInfo.transmission==transmission))
		pass

	if not vehicleAge:
		query.append(db.and_(VehicleInfo.vehicle_age<=vehicleAge))

	if not sourceType:
		query.append(db.and_(VehicleInfo.source_type==sourceType))

	if not salesStatus:
		query.append(db.and_(VehicleInfo.sales_status==salesStatus))

	car_list = list(VehicleInfo.query.filter(*query))

