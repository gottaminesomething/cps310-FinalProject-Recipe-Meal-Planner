class favorite:

	def __init__(self,name,category,servings,preptime,cooktime,ingredients):
		self.name = name
		self.category = category
		self.servings = servings
		self.preptime = preptime
		self.cooktime = cooktime
		self.ingredients = ingredients

	def __str__(self):
		return f"{self.name}"


class ingredient():
	def __init__(self,name,quantity,unit):
		self.name = name
		self.quantity = quantity
		self.unit = unit
	def __str(self):
		return f"{self.name},{self.quantity},{self.unit}"


favoriteList = []