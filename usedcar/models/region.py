# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ['City', 'Country']

class City(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(40), nullable=False)

	def __init__(self, **kwargs):
		if 'id' in kwargs:
			self.id = kwargs.pop('id')

		if 'name' in kwargs:
			self.name = kwargs.pop('name')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<City: %s>' % self.name

	def json(self):
		t_dict = {}
		t_dict['id'] = self.id
		t_dict['name'] = self.name
		return t_dict

class Country(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(40), nullable=False)

	cityId = db.Column(db.Integer, nullable=False)

	def __init__(self, **kwargs):
		if 'id' in kwargs:
			self.id = kwargs.pop('id')

		if 'name' in kwargs:
			self.name = kwargs.pop('name')

		if 'cityId' in kwargs:
			self.cityId = kwargs.pop('cityId')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<country: %s>' % self.name

	def json(self):
		t_dict = {}
		t_dict['id'] = self.id
		t_dict['name'] = self.name
		t_dict['cityId'] = self.cityId
		return t_dict
