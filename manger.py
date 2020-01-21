# -*- coding: utf-8 -*-
"""
File Name:       manger
Description : 
Author :         marion
date:            2020-01-21
Change Activity: 2020-01-21
IDE:             PyCharm
"""

from flask_script import Manager
from project import app



manager = Manager(app)

if __name__ == '__main__':
    manager.run()