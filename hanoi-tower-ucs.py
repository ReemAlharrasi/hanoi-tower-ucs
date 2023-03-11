# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:49:21 2023

@author: Reem
"""

import heapq

space_set={'LMS,0,0':[('LM,0,S',1),('LM,S,0',1)],
           'LM,0,S':[('L,M,S',2),('LM,S,0',1),('LMS,0,0',1)],
           'LM,S,0':[('L,S,M',2),('LM,0,S',1),('LMS,0,0',1)],
           'L,M,S':[('L,MS,0',1),('LS,M,0',1),('LM,0,S',2)],
           'L,S,M':[('L,0,MS',1),('LS,0,M',1),('LM,S,0',2)],
           
           }