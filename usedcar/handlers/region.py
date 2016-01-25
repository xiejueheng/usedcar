# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for, abort
from flask.ext.babel import gettext as _
from flask import jsonify
from flask import json
from ..models import City,country
from ..helpers import force_int

__all__ = ['bp']

bp = Blueprint('region', __name__)

@bp.route('/city', methods=['GET', 'POST'])
def city():
	city_list = list(City.query.all())
	city_json_list = []
	for city in city_list:
		city_json_list.append(city.json())
	return '%s(%s)' %('window.region.city', json.dumps({'code': 0, 'list': city_json_list}))

@bp.route('/country', methods=['GET','POST'])
def country():
	cityId = force_int(request.args.get('cityId'),None)
	if not cityId:
		return abort(404)

	country_list = list(country.query.filter_by(city_id=cityId))
	country_json_list = []
	for c in country_list:
		country_json_list.append(c.json())

	return '%s(%s)' %('window.region.country', json.dumps({'code': 0, 'list': country_json_list}))