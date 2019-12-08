# Deletes files based on the time of creation.

import os
from datetime import datetime, timedelta
import platform

files_list_file = 'files_list.txt'
files_list = []

#The default expiry date will be taken as two days if nothing is entered.

expiry_time = int(input('Enter the expiry time,in minutes - [default = 2 days]:') or "2280")
with open(files_list_file, 'r') as f_read:
    f = f_read.readlines()
    for line in f:
        files_list.append(line[:-1])

current_time = datetime.now()
create_time = 0
for file in files_list:
    if(platform.system() == 'Windows'):
        create_time = os.path.getctime(file)
    else:
        create_time = os.stat(file)
        create_time = create_time.st_ctime
        create_time = datetime.fromtimestamp(create_time)

    if (current_time > create_time + timedelta(minutes = expiry_time)):
        print("{} removed".format(file))
        #os.remove(file)
    #print("**"*20)
    #print("{} file removed,\n{}".format(file,create_time))
