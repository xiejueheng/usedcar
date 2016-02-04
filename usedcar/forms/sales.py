# coding: utf-8

from flask import current_app
from wtforms import TextField, PasswordField, BooleanField, StringField, IntegerField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL
from flask_babel import lazy_gettext as _

from ._base import BaseForm
from ..models import SalesVehicle

__all__ = [
	'AddForm'
]

RESERVED_WORDS = [
	
]


#我要卖车
class AddForm(BaseForm):
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

	"""卖家姓名"""
	name = StringField(
		'name', validators=[DataRequired()],
		description=_('name required')
	)

	""" 手机号码"""
	mobile = StringField(
		_('mobile'), validators=[DataRequired()],
		description=_('mobile required')
	)

	"""车辆所在城市"""
	city = IntegerField(
		'city', validators=[DataRequired()],
		description=_('city required')
	)

	"""车辆所在区域（区、县）"""
	country = IntegerField(
		'country', validators=[DataRequired()],
		description=_('country required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.sales_type = 1
		salesVehicle.save()
		return salesVehicle

class AppraiseForm(BaseForm):
	"""品牌ID"""
	brandId = IntegerField(
		'brandId', validators=[DataRequired()],
		description=_('brandId required')
	)

	""" 车系ID"""
	typeId = IntegerField(
		'typeId', validators=[DataRequired()],
		description=_('typeId required')
	)

	""" 车款ID"""
	styleId = IntegerField(
		'styleId', validators=[DataRequired()],
		description=_('styleId required')
	)

	""" 上牌时间"""
	licesingYear = IntegerField(
		'licesingYear', validators=[DataRequired()],
		description=_('licesingYear required')
	)

	""" 裸车价格"""
	price = IntegerField(
		'price', validators=[DataRequired()],
		description=_('price required')
	)

	""" 车辆状况"""
	status = IntegerField(
		'status', validators=[DataRequired()],
		description=_('status required')
	)

	""" 使用频率"""
	useFrequency = IntegerField(
		'useFrequency', validators=[DataRequired()],
		description=_('useFrequency required')
	)

	""" 生产情况"""
	productionStatus = IntegerField(
		'productionStatus', validators=[DataRequired()],
		description=_('productionStatus required')
	)

	"""车主姓名"""
	name = StringField(
		'name', validators=[DataRequired()],
		description=_('name required')
	)

	""" 手机号码"""
	mobile = StringField(
		_('mobile'), validators=[DataRequired()],
		description=_('mobile required')
	)

	"""车辆所在城市"""
	city = IntegerField(
		'city', validators=[DataRequired()],
		description=_('city required')
	)

	"""车辆所在区域（区、县）"""
	country = IntegerField(
		'country', validators=[DataRequired()],
		description=_('country required')
	)

	"""期待多久卖掉"""
	salesTime = StringField(
		'salesTime', validators=[DataRequired()],
		description=_('salesTime required')
	)

	"""评估类型 0：鉴定评估，1：快速估价"""
	type = IntegerField(
		'type', validators=[DataRequired()],
		description=_('type required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.sales_type = 2
		salesVehicle.save()
		return salesVehicle

class IndividualForm(BaseForm):
	pass