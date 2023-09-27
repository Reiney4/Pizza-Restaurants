#!/usr/bin/env python3
#  import the necessary files
from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza
import random
fake = Faker()

# create the pizza list

pizza_names = [
"Margherita Pizza"
"Pepperoni Pizza"
"Hawaiian Pizza"
"Mushroom and Garlic Pizza"
"Veggie Supreme Pizza"
"Meat Lovers Pizza"
"BBQ Chicken Pizza"
"White Pizza"
"Buffalo Chicken Pizza"
"Four Cheese Pizza"
"Pesto Pizza"
"Taco Pizza"
"Mediterranean Pizza"
"Supreme Pizza"
"Breakfast Pizza"
"Clam Pizza"
"BBQ Pulled Pork Pizza"
"Philly Cheesesteak Pizza"
"BLT Pizza"
"Shrimp Scampi Pizza"
]

# add a list of pizza ingredients
pizza_ingredients = [
"Tomato sauce"
"Mozzarella cheese"
"Ham"
"Pineapple chunks" 
"Fresh basil"
"Olive oil"  
"Sautéed mushrooms"
"Roasted garlic" 
"Onions"
"Black olives"
"Sausage"
"Bacon"
"Ham" 
]

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    restaurants = []
    for i in range(50):
        b = Restaurant(
            name=fake.company()
        )
        restaurants.append(b)
    
    db.session.add_all(restaurants)

    pizzas = []
    names = []
    for i in range(100):

        name = fake.first_name()
        while name in names:
            name = fake.first_name()
        names.append(name)

        bg = Pizza(
            name=name,
            price=randint(1,10),
            pizza=rc(restaurants)
        )

        pizzas.append(bg)

    db.session.add_all(pizzas)
    db.session.commit()
    
    