#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
from kookmin_test import Kookmin

rospy.init_node('main')

kookmin = Kookmin()

while not rospy.is_shutdown():
    kookmin.control()
