# coding: utf-8

from flask import Blueprint
from flask import g, request, flash, current_app
from flask import render_template, redirect, url_for
from flask.ext.babel import gettext as _
from flask import jsonify
from flask import json

__all__ = ['bp']

bp = Blueprint('market', __name__)

@bp.route('/getbrandlist', methods=['GET', 'POST'])
def getbrandlist():
	js = {'id':1, 'brandName': '宝马'}
	return jsonify(**js)