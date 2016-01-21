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
	name = db.Column(db.String(40), index=True, nullable=False)
	
	"""品牌id"""
	brand_id = db.Column(db.Integer, default=0)

	"""排量"""
	displacements = db.Column(db.String(40), nullable=False)

	"""变速箱"""
	transmissions = db.Column(db.String(40), nullable=False)

	"""价格区间"""
	price_range = db.Column(db.String(40),nullable=False)

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('name')

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

	def json(self):
		t_dict = {}
		t_dict['id'] = self.id
		t_dict['name'] = self.name
		t_dict['brandId'] = self.brand_id
		t_dict['priceRange'] = self.price_range
		t_dict['displacements'] = self.displacements
		t_dict['transmissions'] = self.transmissions
		return t_dict

"""
车款VehicleStyle model
"""
class VehicleStyle(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	
	"""车款名称"""
	name = db.Column(db.String(40), index=True, nullable=False)

	"""车型id"""
	type_id = db.Column(db.Integer, default=0)

	"""排量"""
	displacement = db.Column(db.String(40), nullable=False)

	"""变速箱, 1:手动,2:自动,3:手自一体,4:双离合,5:E-CVT无级变速,6:T无级变速"""
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

	"""价格"""
	price = db.Column(db.String(40), nullable=False, default=0)

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('name')
		
		if 'typeId' in kwargs:
			self.type_id =  kwargs.pop('typeId')

		if 'displacement' in kwargs:
			self.displacement = kwargs.pop('displacement')

		if 'transmission' in kwargs:
			self.transmission = kwargs.pop('transmission')

		if 'typeInfo' in kwargs:
			self.type_info = kwargs.pop('typeInfo')

		if 'seat' in kwargs:
			self.seat = kwargs.pop('seat')

		if 'bodyModel' in kwargs:
			self.body_model = kwargs.pop('bodyModel')

		if 'gear' in kwargs:
			self.gear = kwargs.pop('gear')

		if 'gate' in kwargs:
			self.gate = kwargs.pop('gate')

		if 'produce_year' in kwargs:
			self.produce_year = kwargs.pop('produce_year')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<VehicleStyle: %s>' % self.name

	def json(self):
		s_dict = {}
		s_dict['id'] = self.id
		s_dict['typeId'] = self.type_id
		s_dict['displacement'] = self.displacement
		s_dict['transmission'] = self.transmission
		s_dict['typeInfo'] = self.type_info
		s_dict['seat'] = self.seat
		s_dict['bodyModel'] = self.body_model
		s_dict['gear'] = self.gear
		s_dict['gate'] = self.gate
		s_dict['produceYear'] = self.produce_year

		return s_dict

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

	
