# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ['Brand']

"""品牌信息model"""
class Brand(db.Model, SessionMixin):
	"""id"""
	id = db.Column(db.Integer, primary_key=True)

	"""品牌名称"""
	name = db.Column(db.String(40), nullable=False)

	"""首字母"""
	first_letter = db.Column(db.String(2), nullable=False, default='')

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('name')

		if 'first_letter' in kwargs:
			self.first_letter = kwargs.pop('first_letter')

	def __str__(self):
		return '<Brand: %s %s %s>' %(self.id,self.name,self.first_letter)

	def __repr__(self):
		return '<Brand: %s %s %s>' %(self.id,unicode(self.name),self.first_letter)
