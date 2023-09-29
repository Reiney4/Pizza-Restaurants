#!/usr/bin/env python3

# Import necessary modules
from random import choice as sample
from faker import Faker
from models import db, Restaurant, Pizza, RestaurantPizza
from routes import app
import random

# Create a Faker instance to generate fake data
fake = Faker()

# Define a list of pizza names
pizza_names = [
    "Margherita Pizza",
    "Pepperoni Pizza",
    "Hawaiian Pizza",
    "Mushroom and Garlic Pizza",
    "Veggie Supreme Pizza",
    "Meat Lovers Pizza",
    "BBQ Chicken Pizza",
    "White Pizza",
    "Buffalo Chicken Pizza",
    "Four Cheese Pizza",
    "Pesto Pizza",
    "Taco Pizza",
    "Mediterranean Pizza",
    "Supreme Pizza",
    "Breakfast Pizza",
    "Clam Pizza",
    "BBQ Pulled Pork Pizza",
    "Philly Cheesesteak Pizza",
    "BLT Pizza",
    "Shrimp Scampi Pizza",
]

# Define a list of pizza ingredients
pizza_ingredients = [
    "Tomato sauce",
    "Mozzarella cheese",
    "Ham",
    "Pineapple chunks",
    "Fresh basil",
    "Olive oil",
    "Sautéed mushrooms",
    "Roasted garlic",
    "Onions",
    "Black olives",
    "Sausage",
    "Bacon",
    "Ham",
]

# Clear existing data from the database
with app.app_context():
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    db.session.commit()

# Create fake restaurants
with app.app_context():
    restaurants = [
        Restaurant(
            name=fake.company(),
            address=fake.address(),
        )
        for _ in range(10)
    ]
    db.session.add_all(restaurants)
    db.session.commit()

# Create fake pizzas
with app.app_context():
    pizzas = [
        Pizza(
            name=pizza_name,
            ingredients=', '.join(sample(pizza_ingredients, 3))
        )
        for pizza_name in pizza_names
    ]
    db.session.add_all(pizzas)
    db.session.commit()

# Create restaurant-pizza relationships
with app.app_context():
    restaurant_pizzas = [
        RestaurantPizza(
            pizza_id=random.choice(pizzas).id,
            restaurant_id=random.choice(restaurants).id,
            price=random.randint(1, 30)
        )
        for _ in range(10)
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
