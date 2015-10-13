# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ('VehicleType', 'VehicleStyle', 'VehicleInfo', 'VehiclePhoto')

"""
车型VehicleType
"""
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

"""
车款VehicleStyle
"""
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

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<VehicleStyle: %s>' % self.name

"""
车辆信息VehicleInfo
"""
class VehicleInfo(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	vehicle_style =  db.Column(db.Integer, default=0)
	mileage = db.Column(db.Integer, default=0)
	vehicle_age = db.Column(db.Integer, default=0)
	register_time = db.Column(db.DateTime, default=datetime.utcnow)
	source_type = db.Column(db.Integer, default=0)
	vehicle_typeid = db.Column(db.Integer, default=0)
	brand_id = db.Column(db.Integer, default=0)

	def __str__(self):
		return self.id

	def __repr__(self):
		return '<VehicleInfo: %s>' % self.id


"""
车辆图片
"""
class VehiclePhoto(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	vehicle_id = db.Column(db.Integer, default=0)
	photo_type = db.Column(db.Integer, default=0)
	photo_url = db.Column(db.String(200), unique=True, index=True,
						 nullable=False)

	def __str__(self):
		return '%s %s' %(self.id, self.vehicle_id)

	def __repr__(self):
		return '<VehiclePhoto: %s_%s>' % (self.id,self.vehicle_id)

	