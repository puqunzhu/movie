#@TIME   : 2018/11/19 5:47 PM
#@Author : Qunzhu Pu
#@File   :__init__.py.py
from flask import Blueprint
home = Blueprint("home",__name__)
import app.home.views