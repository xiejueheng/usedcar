# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ('SalesVehicle')

class SalesVehicle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	brand_id = db.Column(db.Integer, default=0)
	type_id = db.Column(db.Integer, default=0)
	style_id = db.Column(db.Integer, default=0)
	name = db.Column(db.String(100), nullable=False)
	location = db.Column(db.String(100), nullable=False)
	mobile = db.Column(db.String(11), nullable=False)

	def __init__(self, **kwargs):
		if 'brandId' in kwargs:
			brandId = kwargs.pop('brandId')
			self.brand_id = brandId

		if 'typeId' in kwargs:
			typeId = kwargs.pop('typeId')
			self.type_id = typeId

		if 'styleId' in kwargs:
			styleId = kwargs.pop('styleId')
			self.style_id = style_id

		if 'name' in kwargs:
			name = kwargs.pop('name')
			self.name = name

		if 'mobile' in kwargs:
			mobile = kwargs.pop('mobile')
			self.mobile = mobile

		if 'location' in kwargs:
			location = kwargs.pop('location')
			self.location = location

		for k, v in kwargs.items():
			setattr(self, k, v)

	def __str__(self):
		return self.id

	def __repr__(self):
		return '<SalesVehicle: %s>' % self.id

	def save(self):
		db.session.add(self)
		db.session.commit()
		return self