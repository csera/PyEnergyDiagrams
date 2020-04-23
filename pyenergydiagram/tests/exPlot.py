#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 11:45:00 2018

@author: csera
"""

from energydiagram import ED

diagram = ED()
diagram.add_level(0 + 0,'$n_x = 0$ \n $n_y = 0$')
diagram.add_level(1 + 0,'$n_x = 1$ \n $n_y = 0$')
diagram.add_level(0 + 1,'$n_x = 0$ \n $n_y = 1$')
diagram.add_level(2 + 0,'$n_x = 2$ \n $n_y = 0$')
diagram.add_level(1 + 1,'$n_x = 1$ \n $n_y = 1$')
diagram.add_level(0 + 2,'$n_x = 0$ \n $n_y = 2$')
diagram.add_level(3 + 0,'$n_x = 3$ \n $n_y = 0$')
diagram.add_level(0 + 1.5,'$n_x = 0$ \n $n_y = 1.5$','last')
diagram.add_level(2 + 1,'$n_x = 2$ \n $n_y = 1$')
diagram.add_level(3 - 1.5,'$n_x = 3$ \n $n_y = -0.5$','last')

diagram.set_yName("y axis in $units_{energy}$")
diagram.plot(True)

diagram.add_link(0,1)
diagram.add_link(2,3)
diagram.add_link(5,6)
diagram.add_link(5,7)

diagram.plot(False)
