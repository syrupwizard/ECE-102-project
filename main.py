#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:55:03 2024

@author: Austin, Cece, and Chris
"""

import system as sys #file containing

sys.load_file()

prompt = "Enter a command or type 'help': "
user_string = sys.get_line(prompt)

while user_string != "exit":
    ###HELP
    sys.help_function(user_string)#prints out help info for user
    
    ###ALARM
    sys.arm_disarm(user_string)#operate alarm
    sys.alarm_state = sys.change_stuff(user_string)
    sys.trigger_alarm(user_string)#alarm goes off until user 

    ###DOORS
    sys.open_close(user_string)#operate doors
    sys.check_doors(user_string)#check doors
    sys.trigger_alarm(user_string)#alarm goes off until user 

    ###LIGHTS
    sys.activate_lights(user_string)#turns on and off lights      
    sys.check_lights(user_string)#check lights
    user_string = sys.get_line(prompt)#get input at end of loop  
    sys.trigger_alarm(user_string)#alarm goes off until user 


sys.save_file()


    

















