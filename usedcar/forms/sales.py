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
	brandId = IntegerField(
		'brandId', validators=[DataRequired()],
		description=_('brandId required')
	)

	typeId = IntegerField(
		'typeId', validators=[DataRequired()],
		description=_('typeId required')
	)

	styleId = IntegerField(
		'styleId', validators=[DataRequired()],
		description=_('styleId required')
	)

	name = StringField(
		'name', validators=[DataRequired()],
		description=_('name required')
	)

	mobile = StringField(
		_('mobile'), validators=[DataRequired()],
		description=_('mobile required')
	)

	location = StringField(
		'location', validators=[DataRequired()],
		description=_('location required')
	)
	salesType = IntegerField(
		'salesType', validators=[DataRequired()],
		description=('salesType required')
	)

	def save(self):
		print self.data
		return
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.save()
		return salesVehicle
