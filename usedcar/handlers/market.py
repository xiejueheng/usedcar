# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from flask.ext.babel import gettext as _
from flask import jsonify
from flask import json
from ..models import Brand

__all__ = ['bp']

bp = Blueprint('market', __name__)

@bp.route('/getbrandlist', methods=['GET', 'POST'])
def getbrandlist():
	brand_list = list(Brand.query.all())
	brand_json_list = []
	for brand in brand_list:
		brand_json_list.append(brand.json())
	return json.dumps(brand_json_list)
