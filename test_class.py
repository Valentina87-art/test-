# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:48:48 2022

@author: 57314
"""
#%% CL: ALIAS 

from cal_class import calculator1 as CL 

in_a= 15
in_b= 7

classobj = CL( input_a=in_a, in_b=in_b)

result1= classobj.add()
result2 = classobj.floor_div()

print 
