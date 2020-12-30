'''
Autor: Wentao Lin
Description: run fuction of all files in app folder
Date: 2020-12-26 12:19:47
LastEditTime: 2020-12-26 12:19:56
LastEditors: Wentao Lin
'''

from app import app
from datetime import timedelta
 
# sets the static file cache expiration time
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.run(debug=True)
