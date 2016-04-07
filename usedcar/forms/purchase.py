# coding: utf-8

import time
from flask import current_app
from wtforms import TextField, PasswordField, BooleanField, StringField, IntegerField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL
from flask_babel import lazy_gettext as _

from ._base import BaseForm
from ..models import VehiclePurchase

__all__ = [
	'PurchaseAddForm'
]

RESERVED_WORDS = [
	
]


"""我要买车"""
class PurchaseAddForm(BaseForm):

	"""买车姓名"""
	name = StringField(
		'name', validators=[DataRequired()],
		description=_('name required')
	)

	""" 手机号码"""
	mobile = StringField(
		_('mobile'), validators=[DataRequired()],
		description=_('mobile required')
	)

	"""所在城市"""
	city = IntegerField(
		'city', validators=[DataRequired()],
		description=_('city required')
	)

	"""品牌ID"""
	brandId = IntegerField(
		'brandId', validators=[DataRequired()],
		description=_('brandId required')
	)

	"""车型ID"""
	typeId = IntegerField(
		'typeId', validators=[DataRequired()],
		description=_('typeId required')
	)

	"""车龄"""
	carAge = IntegerField(
		'carAge', validators=[],
		description=_('')
	)

	"""其它说明"""
	common = StringField(
		'common', validators=[],
		description=_('')
	)

	def save(self):
		purchase = VehiclePurchase(**self.data)
		purchase.timestamp = int(time.time())
		purchase.save()
		return purchase