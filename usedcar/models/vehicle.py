# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ('VehicleType', 'VehicleStyle', 'VehicleInfo', 'VehicleImg')

class VehicleType(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), unique=True, index=True,
						 nullable=False)
	brand_id = db.Column(db.Integer, default=0)
	price_range = db.Column(db.String(40), unique=True, index=True,
						 nullable=False)

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('kwargs')

		if 'brand_id' in kwargs:
			self.brand_id = kwargs.pop('brand_id')

		if 'price_range' in kwargs:
			self.price_range = kwargs.pop('price_range')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<VehicleType: %s>' % self.name

class VehicleStyle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), unique=True, index=True,
						 nullable=False)
	type_id = db.Column(db.Integer, default=0)
	displacement = db.Column(db.Integer, default=0)
	transmission = db.Column(db.Integer, default=0)
	type_info = db.Column(db.Integer, default=0)
	seat = db.Column(db.Integer, default=0)
	body_model = db.Column(db.Integer, default=0)
	gear = db.Column(db.Integer, default=0)
	gate = db.Column(db.Integer, default=0)
	produce_year = db.Column(db.Integer, default=0)