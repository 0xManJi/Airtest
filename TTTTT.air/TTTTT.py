# -*- encoding=utf8 -*-
__author__ = "ZHANG CHUN HE"

from airtest.core.api import *

auto_setup(__file__)


swipe(Template(r"tpl1660901042056.png", record_pos=(-0.081, -0.666), resolution=(900, 1600)), vector=[0.3853, 0.4382])
sleep(1)
touch(Template(r"tpl1660901059760.png", record_pos=(-0.366, -0.413), resolution=(900, 1600)))
sleep(1)

touch(Template(r"tpl1661089787193.png", record_pos=(-0.131, 1.006), resolution=(1080, 2340)))

sleep(1)

assert_exists(Template(r"tpl1661089825564.png", record_pos=(-0.381, -0.806), resolution=(1080, 2340)), "进入分类模块")

sleep(1)
touch(Template(r"tpl1661093424474.png", record_pos=(-0.367, 1.004), resolution=(1080, 2340)))

touch(Template(r"tpl1661089118258.png", record_pos=(0.434, -0.782), resolution=(900, 1600)))
