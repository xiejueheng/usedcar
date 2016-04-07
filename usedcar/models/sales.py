# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ['SalesVehicle']

"""
卖车信息model
"""
class SalesVehicle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	"""品牌"""
	brand_id = db.Column(db.Integer, default=0)

	"""车型id"""
	type_id = db.Column(db.Integer, default=0)

	""" 车款 """
	style_id = db.Column(db.Integer, default=0)
	
	""" 卖家姓名 """
	name = db.Column(db.String(100), nullable=True)

	""" 车辆所在城市 """
	city = db.Column(db.Integer, default=0)

	""" 车辆所在区县 """
	country = db.Column(db.Integer, default=0)

	""" 手机号码 """
	mobile = db.Column(db.String(11), nullable=True)

	""" 上牌时间 """
	licesing_year = db.Column(db.Integer, default=0)

	"""里程"""
	mileage =  db.Column(db.Float, default=0.0)

	"""裸车价格"""
	price = db.Column(db.String(11), nullable=True)

	"""车辆状况 1:很好,2:较好,3:一般,4:较差,5:差	"""
	status = db.Column(db.Integer, default=0)

	"""使用频率"""
	use_frequency = db.Column(db.Integer, default=0)

	"""生产情况 1:畅销,2:一般,3:滞销,4:停产"""
	production_status = db.Column(db.Integer, default=0)

	"""上牌地点"""
	licesing_place = db.Column(db.Integer, default=0)

	"""期待多久卖掉"""
	sales_time = db.Column(db.String(11), nullable=True)

	"""1：鉴定评估,2：快速估价"""
	type = db.Column(db.Integer, default=0)

	"""置换品牌ID"""
	replace_brand_id = db.Column(db.Integer, default=0)

	"""置换车系ID"""
	replace_type_id = db.Column(db.Integer, default=0)

	"""置换车款ID"""
	replace_style_id = db.Column(db.Integer, default=0)

	"""经销商ID"""
	agency_id = db.Column(db.Integer, default=0)

	"""数据类型, 1:我要卖车,2:鉴定评估,3:出售车辆(不需要预约),4:出售车辆(置换卖),5:出售车辆(经销商代理)"""
	sales_type = db.Column(db.Integer, default=0)

	timestamp = db.Column(db.Integer, default=0)

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

		if 'city' in kwargs:
			city = kwargs.pop('city')
			self.city = city

		if 'country' in kwargs:
			country	= kwargs.pop('country')
			self.country = country

		if 'licesingYear' in kwargs:
			licesing_year = kwargs.pop('licesingYear')
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

		if 'timestamp' in kwargs:
			timestamp = kwargs.pop('timestamp')
			self.timestamp = timestamp

		for k, v in kwargs.items():
			setattr(self, k, v)

	def __str__(self):
		return 'SalesVehicle sales_type=%s, id=%s, brand_id=%s, type_id=%s, style_id=%s, name=%s, city=%s, country=%s, mobile=%s' %(self.sales_type,self.id,self.brand_id,self.type_id,self.style_id,self.name,self.city,self.country,self.mobile)

	def __repr__(self):
		return '<SalesVehicle: %d>' % self.id

	def json(self):
		s_dict={}
		s_dict['id']=self.id
		s_dict['brandId']=self.brand_id
		s_dict['typeId']=self.type_id
		s_dict['styleId']=self.style_id
		s_dict['name']=self.name
		s_dict['mobile']=self.mobile
		s_dict['city']=self.city
		s_dict['country']=self.country
		s_dict['licesingYear']=self.licesing_year
		s_dict['mileage']=self.mileage
		s_dict['price']=self.price
		s_dict['status']=self.status
		s_dict['useFrequency']=self.use_frequency
		s_dict['productionStatus']=self.production_status
		s_dict['licesingPlace']=self.licesing_place
		s_dict['salesTime']=self.sales_time
		s_dict['type']=self.type
		s_dict['replaceBrandId']=self.replace_brand_id
		s_dict['replaceTypeId']=self.replace_type_id
		s_dict['replaceStyleId']=self.replace_style_id
		s_dict['agencyId']=self.agency_id
		s_dict['salesType']=self.sales_type
		s_dict['timestamp'] = self.timestamp
		return s_dict

	def save(self):
		db.session.add(self)
		db.session.commit()
		return self
