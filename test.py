#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import os

# nuevos parametros False, os.path.dirname(os.path.abspath(__file__))
api = InstagramAPI("username", "password", False, os.path.dirname(os.path.abspath(__file__)))
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")
    # nuevo codigo
    if(api.LastJson['message'] == 'challenge_required'):
		
        path = api.LastJson['challenge']['api_path'][1:]
		
        choice = 1 # 0 - SMS; 1 - EMail
        api.getCodeChallengeRequired(path, choice) 
		
        code = input('Enter the code: ')

        api.setCodeChallengeRequired(path,code)
		
        if(api.login()):
            print('ok')
        else:
            print('bad')
    # fin nuevo codigo
