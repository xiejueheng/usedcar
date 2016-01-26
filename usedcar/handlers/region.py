# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for, abort
from flask.ext.babel import gettext as _
from flask import jsonify
from flask import json
from sales import to_unicode
from ..models import City,country
from ..helpers import force_int

__all__ = ['bp']

bp = Blueprint('region', __name__)
run_path = os.getcwd()

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

@bp.route('/load', methods=['GET','POST'])
def load():
	city_list = list(City.query.all())
	if len(city_list) > 0:
		js = {'code':1}
		return json.dumps(js)

	city_list, country_list = get_data()
	for city in city_list:
		city.save()

	for country in country_list:
		country.save()

def get_data():
	city_file_path = os.path.join(run_path,'data/city.txt')
	file_obj = open(city_file_path,'r')

	city_list = []

	try:
		list_of_all_lines = file_obj.readlines()
		for line in list_of_all_lines:
			line = line.strip('\r\n')
			line_arrays = line.split(',')
			b_dict = {}
			b_dict['id'] = int(line_arrays[0])
			b_dict['name'] = to_unicode(line_arrays[1])
			city_list.append(City(**b_dict))
	finally:
		file_obj.close()

	country_file_path = os.path.join(run_path,'data/country.txt')
	file_obj = open(city_file_path,'r')

	country_list = []

	try:
		list_of_all_lines = file_obj.readlines()
		for line in list_of_all_lines:
			line = line.strip('\r\n')
			line_arrays = line.split(',')
			b_dict = {}
			b_dict['cityId'] = int(line_arrays[0])
			b_dict['id'] = int(line_arrays[1])
			b_dict['name'] = to_unicode(line_arrays[2])
			country_list.append(City(**b_dict))
	finally:
		file_obj.close()

	return city_list,country_list
