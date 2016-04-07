# coding: utf-8

import time
from flask import current_app
from wtforms import TextField,FloatField, PasswordField, BooleanField, StringField, IntegerField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL
from flask_babel import lazy_gettext as _

from ._base import BaseForm
from ..models import SalesVehicle

__all__ = [
	'AddForm','AppraiseForm','IndividualForm','AgencyForm','ReplaceForm'
]

RESERVED_WORDS = [
	
]


"""我要卖车"""
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
		salesVehicle.timestamp = int(time.time())
		salesVehicle.save()
		return salesVehicle

"""鉴定评估车辆"""
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
		'licesingYear', validators=[],
		description=_('')
	)

	""" 裸车价格"""
	price = StringField(
		'price', validators=[],
		description=_('')
	)

	""" 车辆状况"""
	status = IntegerField(
		'status', validators=[],
		description=_('')
	)

	""" 使用频率"""
	useFrequency = IntegerField(
		'useFrequency', validators=[],
		description=_('')
	)

	""" 生产情况"""
	productionStatus = IntegerField(
		'productionStatus', validators=[],
		description=_('')
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
	licesingPlace = IntegerField(
		'licesingPlace', validators=[DataRequired()],
		description=_('licesingPlace required')
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
		salesVehicle.timestamp = int(time.time())
		salesVehicle.save()
		return salesVehicle

"""6.3.出售车辆（不需要预约）"""
class IndividualForm(BaseForm):
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

	""" 车身颜色"""
	color = IntegerField(
		'color', validators=[DataRequired()],
		description=_('color required')
	)

	""" 上牌时间，年份 """
	licesingYear = IntegerField(
		'licesingYear', validators=[],
		description=_('')
	)

	""" 里程 """
	mileage = FloatField(
		'mileage', validators=[DataRequired()],
		description=_('mileage required')
	)

	""" 裸车价格"""
	price = StringField(
		'price', validators=[DataRequired()],
		description=_('price required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.sales_type = 3
		salesVehicle.timestamp = int(time.time())
		salesVehicle.save()
		return salesVehicle

"""6.4.出售车辆（置换卖）"""
class ReplaceForm(BaseForm):
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

	"""上牌时间"""
	licesingYear = IntegerField(
		'licesingYear', validators=[DataRequired()],
		description=_('licesingYear required')
	)

	""" 里程 """
	mileage = FloatField(
		'mileage', validators=[DataRequired()],
		description=_('mileage required')
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

	""" 验证码"""
	verifyCode = StringField(
		_('verifyCode'), validators=[DataRequired()],
		description=_('verifyCode required')
	)

	""" 品牌ID """
	replaceBrandId = IntegerField(
		'brandId', validators=[DataRequired()],
		description=_('brandId required')
	)

	"""车系ID"""
	replaceTypeId = IntegerField(
		'typeId', validators=[DataRequired()],
		description=_('typeId required')
	)

	"""车款ID"""
	replaceStyleId = IntegerField(
		'styleId', validators=[DataRequired()],
		description=_('styleId required')
	)

	"""经销商ID"""
	agencyId = IntegerField(
		'agencyId', validators=[DataRequired()],
		description=_('agencyId required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.sales_type = 4
		salesVehicle.timestamp = int(time.time())
		salesVehicle.save()
		return salesVehicle

""" 6.5.出售车辆（经销商代理） """
class AgencyForm(BaseForm):
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

	"""上牌时间"""
	licesingYear = IntegerField(
		'licesingYear', validators=[DataRequired()],
		description=_('licesingYear required')
	)

	""" 验证码"""
	verifyCode = StringField(
		_('verifyCode'), validators=[DataRequired()],
		description=_('verifyCode required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.sales_type = 5
		salesVehicle.timestamp = int(time.time())
		salesVehicle.save()
		return salesVehicle