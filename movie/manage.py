#@TIME   : 2018/11/19 5:45 PM
#@Author : Qunzhu Pu
#@File   :manage.py
from app import app
from flask_script import Manager

manage = Manager(app)

if __name__ == '__main__':
    app.run()