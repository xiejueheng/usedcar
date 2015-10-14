# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, abort, jsonify
from flask.ext.babel import gettext as _
from ..forms import AddForm
from ..utils import requtils
from ..models import SalesVehicle

__all__ = ['bp']

bp = Blueprint('sales', __name__)

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
	salesVehicle = SalesVehicle(**self.data)
	return "haha"
	#return abort(403)