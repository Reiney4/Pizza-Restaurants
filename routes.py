#!/usr/bin/env python3

# make the necessary importations

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound

from models import db, Restaurant,Pizza,RestaurantPizza


