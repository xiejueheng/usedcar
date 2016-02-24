# coding: utf-8

from flask import current_app
from wtforms import TextField, PasswordField, BooleanField, StringField, IntegerField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL
from flask_babel import lazy_gettext as _

from ._base import BaseForm
from ..models import VehicleInfo

__all__ = [
	'VehicleForm'
]


"""我要卖车"""
class VehicleForm(BaseForm):
	""" 品牌ID """
	brandId = IntegerField(
		'brandId', validators=[DataRequired()],
		description=_('brandId required')
	)

	"""车系ID"""
	typeId = IntegerField(
		'typeId', validators=[DataRequired()],
		description=_('typeId required')
	)

	"""车款ID"""
	styleId = IntegerField(
		'styleId', validators=[DataRequired()],
		description=_('styleId required')
	)

	"""车龄"""
	vehicleAge = IntegerField(
		'vehicleAge', validators=[DataRequired()],
		description=_('vehicleAge required')
	)

	"""上牌时间"""
	registerTime = IntegerField(
		'registerTime', validators=[],
		description=_('')
	)

	"""车源类型"""
	sourceType = IntegerField(
		'sourceType', validators=[DataRequired()],
		description=_('sourceType required')
	)

	"""销售状态"""
	salesStatus = IntegerField(
		'salesStatus', validators=[],
		description=_('')
	)

	def save(self):
		salesVehicle = VehicleInfo(**self.data)
		salesVehicle.save()
		return salesVehicle

