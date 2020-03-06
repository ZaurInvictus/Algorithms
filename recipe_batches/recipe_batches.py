#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    portionLowest = None
    for key in recipe:
        if key in ingredients:
            if portionLowest == None or (ingredients[key] // recipe[key]) < portionLowest:
                portionLowest = ingredients[key] // recipe[key]
            elif ingredients[key] // recipe[key] == 0:
                portionLowest = 0
        else:
            portionLowest = 0
    return portionLowest


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))