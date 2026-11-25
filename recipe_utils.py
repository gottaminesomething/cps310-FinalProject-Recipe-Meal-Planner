"""Utility functions for the Recipe & Meal Planner."""

import json
import Objects as obj

def load_config(filename):
	"""Load application configuration from a JSON file."""
	with open(filename, encoding="utf-8") as file:
		return json.load(file)


def load_recipes(filename):
	"""Load recipe data from a JSON file."""
	with open(filename, encoding="utf-8") as file:
		return json.load(file)


def search_by_name(recipes, search_term):
	"""Return recipes whose names contain the search term."""
	search_term = search_term.lower()
	return [
		recipe
		for recipe in recipes
		if search_term in recipe["name"].lower()
	]


def filter_by_category(recipes, category):
	"""Return recipes that match the requested category."""
	category = category.lower()
	return [
		recipe
		for recipe in recipes
		if recipe["category"].lower() == category
	]


#added by me

def load_favorites(filename, favorites):
	with open(filename, encoding="utf-8") as file:
		recipes = json.load(file)

	favorites.clear()

	for recipe in recipes:
		ingredients = []

		for item in recipe["ingredients"]:
			ingredients.append(obj.ingredient(**item))

		favorites.append(obj.favorite(
			recipe["name"],
			recipe["category"],
			recipe["servings"],
			recipe["prep_time"],
			recipe["cook_time"],
			ingredients
		))
	return recipes