# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ['SalesVehicle']

"""
卖车信息
"""
class SalesVehicle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	"""品牌"""
	brand_id = db.Column(db.Integer, default=0)

	"""车型id"""
	type_id = db.Column(db.Integer, default=0)

	#车款id
	style_id = db.Column(db.Integer, default=0)
	name = db.Column(db.String(100), nullable=False)
	location = db.Column(db.String(100), nullable=False)
	mobile = db.Column(db.String(11), nullable=False)

	licesing_year = db.Column(db.Integer, default=0)
	mileage =  db.Column(db.Integer, default=0)
	price = db.Column(db.String(11), nullable=False)
	status = db.Column(db.Integer, default=0)
	use_frequency = db.Column(db.Integer, default=0)
	production_status = db.Column(db.Integer, default=0)
	licesing_place = db.Column(db.String(11), nullable=False)
	sales_time = db.Column(db.String(11), nullable=False)
	type = db.Column(db.Integer, default=0)

	replace_brand_id = db.Column(db.Integer, default=0)
	replace_type_id = db.Column(db.Integer, default=0)
	replace_style_id = db.Column(db.Integer, default=0)
	agency_id = db.Column(db.Integer, default=0)

	sales_type = db.Column(db.Integer, default=0)

	def __init__(self, **kwargs):
		if 'brandId' in kwargs:
			brandId = kwargs.pop('brandId')
			self.brand_id = brandId

		if 'typeId' in kwargs:
			typeId = kwargs.pop('typeId')
			self.type_id = typeId

		if 'styleId' in kwargs:
			styleId = kwargs.pop('styleId')
			self.style_id = styleId

		if 'name' in kwargs:
			name = kwargs.pop('name')
			self.name = name

		if 'mobile' in kwargs:
			mobile = kwargs.pop('mobile')
			self.mobile = mobile

		if 'location' in kwargs:
			location = kwargs.pop('location')
			self.location = location

		if 'licesingYear' in kwargs:
			licesing_year = kwargs.pop('licesing_year')
			self.licesing_year = licesing_year

		if 'mileage' in kwargs:
			mileage = kwargs.pop('mileage')
			self.mileage = mileage

		if 'price' in kwargs:
			price = kwargs.pop('price')
			self.price = price

		if 'status' in kwargs:
			status = kwargs.pop('status')
			self.status = status

		if 'useFrequency' in kwargs:
			use_frequency = kwargs.pop('useFrequency')
			self.use_frequency = use_frequency

		if 'productionStatus' in kwargs:
			production_status = kwargs.pop('productionStatus')
			self.production_status = production_status

		if 'licesingPlace' in kwargs:
			licesing_place = kwargs.pop('licesingPlace')
			self.licesing_place = licesing_place

		if 'salesTime' in kwargs:
			sales_time = kwargs.pop('salesTime')
			self.sales_time = sales_time

		if 'type' in kwargs:
			type = kwargs.pop('type')
			self.type = type

		if 'replaceBrandId' in kwargs:
			replace_brand_id = kwargs.pop('replaceBrandId')
			self.replace_brand_id = replace_brand_id

		if 'replaceTypeId' in kwargs:
			replace_type_id = kwargs.pop('replaceTypeId')
			self.replace_type_id = replace_type_id

		if 'replaceStyleId' in kwargs:
			replace_style_id = kwargs.pop('replaceStyleId')
			self.replace_style_id = replace_style_id

		if 'agencyId' in kwargs:
			agency_id = kwargs.pop('agencyId')
			self.agency_id = agency_id

		if 'salesType' in kwargs:
			sales_type = kwargs.pop('salesType')
			self.sales_type = sales_type

		for k, v in kwargs.items():
			setattr(self, k, v)

	def __str__(self):
		return 'SalesVehicle id=%s, brand_id=%s, type_id=%s, style_id=%s, name=%s, location=%s, mobile=%s' %(self.id,self.brand_id,self.type_id,self.style_id,self.name,self.location,self.mobile)

	def __repr__(self):
		return '<SalesVehicle: %d>' % self.id

	def save(self):
		db.session.add(self)
		db.session.commit()
		return self