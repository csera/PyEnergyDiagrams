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

# Note that 'last' will place the new level at the same exact x position as the *immediately* 
# preceding level. Thus, you must group by columns, not rows when adding
diagram.add_level(3 + 0,'$n_x = 3$ \n $n_y = 0$')
diagram.add_level(0 + 1.5,'$n_x = 0$ \n $n_y = 1.5$','last')


diagram.add_level(-1 + 0,'$n_x = -1$ \n $n_y = 0$')

diagram.set_yName("y axis in $units_{energy}$")
diagram.plot(True)

diagram.add_link(1,2)
diagram.add_link(3,4)
diagram.add_link(6,7)
diagram.add_link(7,8)
diagram.add_link(7,9)

diagram.plot(False)
