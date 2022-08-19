# -*- encoding=utf8 -*-
__author__ = "Joy"

from airtest.core.api import *

auto_setup(__file__)


touch(Template(r"tpl1660900985388.png", record_pos=(-0.356, -0.544), resolution=(900, 1600)))

sleep(1)

swipe(Template(r"tpl1660901042056.png", record_pos=(-0.081, -0.666), resolution=(900, 1600)), vector=[0.3853, 0.4382])
sleep(1)
touch(Template(r"tpl1660901059760.png", record_pos=(-0.366, -0.413), resolution=(900, 1600)))

sleep(3)
assert_exists(Template(r"tpl1660901152462.png", record_pos=(-0.202, -0.677), resolution=(900, 1600)), "成功进入首页")

touch(Template(r"tpl1660901206656.png", record_pos=(0.434, -0.782), resolution=(900, 1600)))

