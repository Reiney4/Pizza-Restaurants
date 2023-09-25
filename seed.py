#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

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
    
    