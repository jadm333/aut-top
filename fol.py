#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:59:28 2017

@author: peps
"""
import os
import re
def folder():
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    i = []
    for f in all_subdirs:
        n = re.findall('\d+', f)
        if len(n) > 0:
            i.append(int(n[0]))
    return max(i)
folder()
#%%
    os.makedirs(newpath)
    
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    
#%%
import re
re.findall('\d+', 'modelo5')
