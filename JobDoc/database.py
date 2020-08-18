from JobDoc import db

class Company(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), unique=True, nullable=False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "Name: " + self.name


class Skill(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(), unique=True, nullable=False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "Skill: " + self.name