# coding: utf-8

import hashlib
from datetime import datetime
from ._base import db, SessionMixin

__all__ = ('Brand')

class Brand(db.Model, SessionMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False)
	first_letter = db.Column(db.String(2), nullable=False)

	def __init__(self, **kwargs):
		if 'name' in kwargs:
			self.name = kwargs.pop('name')

		if 'first_letter' in kwargs:
			self.first_letter = kwargs.pop('first_letter')

	def __str__(self):
		return self.name

	def __repr__(self):
		return '<Brand: %s>' % self.name