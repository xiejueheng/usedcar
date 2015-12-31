# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ['VehicleType', 'VehicleStyle', 'VehicleInfo', 'VehiclePhoto']

"""
车型VehicleType model
"""
class VehicleType(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	"""车型名称"""
	name = db.Column(db.String(40), unique=True, index=True, nullable=False)
	
	"""品牌id"""
	brand_id = db.Column(db.Integer, default=0)

	"""排量"""
	displacements = db.Column(db.String(40), nullable=False)

	"""变速箱"""
	transmissions = db.Column(db.String(40), nullable=False)

	"""价格区间"""
	price_range = db.Column(db.String(40), unique=True, index=True,nullable=False)

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('kwargs')

		if 'brand_id' in kwargs:
			self.brand_id = kwargs.pop('brand_id')

		if 'price_range' in kwargs:
			self.price_range = kwargs.pop('price_range')

		if 'displacements' in kwargs:
			self.displacements = kwargs.pop('displacements')

		if 'transmissions' in kwargs:
			self.transmissions = kwargs.pop('transmissions')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<VehicleType: %s>' % self.name

"""
车款VehicleStyle model
"""
class VehicleStyle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	
	"""车款名称"""
	name = db.Column(db.String(40), unique=True, index=True, nullable=False)

	"""车型id"""
	type_id = db.Column(db.Integer, default=0)

	"""排量"""
	displacement = db.Column(db.String(40), nullable=False)

	"""变速箱"""
	transmission = db.Column(db.Integer, default=0)

	"""车辆类型"""
	type_info = db.Column(db.Integer, default=0)

	"""座位数"""
	seat = db.Column(db.Integer, default=0)

	"""车身形式"""
	body_model = db.Column(db.Integer, default=0)

	"""档位数"""
	gear = db.Column(db.Integer, default=0)

	"""车门数"""
	gate = db.Column(db.Integer, default=0)

	"""款式年份"""
	produce_year = db.Column(db.Integer, default=0)

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<VehicleStyle: %s>' % self.name

"""
车辆信息VehicleInfo model
"""
class VehicleInfo(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)

	"""车款ID"""
	vehicle_style_id =  db.Column(db.Integer, default=0)

	"""里程（公里）"""
	mileage = db.Column(db.Integer, default=0)

	"""车龄"""
	vehicle_age = db.Column(db.Integer, default=0)

	"""上牌时间（时间戳）"""
	register_time = db.Column(db.DateTime, default=datetime.utcnow)

	"""车源类型,1:认证车,2:商户车源,3:其他车源"""
	source_type = db.Column(db.Integer, default=0)

	"""车型ID"""
	vehicle_type_id = db.Column(db.Integer, default=0)

	"""品牌ID"""
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

	
