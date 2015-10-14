# coding: utf-8

from flask import current_app
from wtforms import TextField, PasswordField, BooleanField
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

class AddForm(BaseForm):
	brandId = TextField(
		_('brandId'), validators=[DataRequired()],
		description=_('brandId required')
	)

	typeId = TextField(
		_('typeId'), validators=[DataRequired()],
		description=_('typeId required')
	)

	styleId = TextField(
		_('styleId'), validators=[DataRequired()],
		description=_('styleId required')
	)

	name = TextField(
		_('name'), validators=[DataRequired()],
		description=_('name required')
	)

	mobile = TextField(
		_('mobile'), validators=[DataRequired()],
		description=_('mobile required')
	)

	location = TextField(
		_('location'), validators=[DataRequired()],
		description=_('location required')
	)

	def save(self):
		salesVehicle = SalesVehicle(**self.data)
		salesVehicle.save()
		return salesVehicle