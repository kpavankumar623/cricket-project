#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pytest
import toss_main as tm

def test_lengaburu():
    toss = "lengaburu"
    weather = 'cloudy'
    day = 'night'
    
    choice = tm.choose_option(toss,weather,day)
    assert choice == 'bowls'

def test_enchai():
    toss = "enchai"
    weather = 'clear'
    day = 'night'
    
    choice = tm.choose_option(toss,weather,day)
    assert choice == 'bats'

def test_lenga_diff():
    toss = "lengaburu"
    weather = 'cloudy'
    day = 'day'
    
    choice = tm.choose_option(toss,weather,day)
    assert choice == 'bats'

def test_enchai_diff():
    toss = "enchai"
    weather = 'cloudy'
    day = 'day'
    
    choice = tm.choose_option(toss,weather,day)
    assert choice == 'bats'