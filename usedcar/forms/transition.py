# coding: utf-8

from flask import current_app
from wtforms import TextField, PasswordField, BooleanField, StringField, IntegerField
from wtforms import TextAreaField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import Optional, URL
from flask_babel import lazy_gettext as _

from ._base import BaseForm
from ..models import VehicleTransition

__all__ = [
	'TransitionAddForm'
]

RESERVED_WORDS = [
	
]


"""我要卖车"""
class TransitionAddForm(BaseForm):
	""" 车务类型名称 """
	transition = StringField(
		'brandId', validators=[DataRequired()],
		description=_('transition required')
	)

	"""办理车务者姓名"""
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

	def save(self):
		transition = VehicleTransition(**self.data)
		transition.save()
		return transition