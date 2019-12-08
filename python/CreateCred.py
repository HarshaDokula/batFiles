# Create Credential file.

from cryptography.fernet import Fernet
import ctypes
import time
import re
import os
import sys

cred_filename = "Credential.ini"
key_file = 'key.key'
time_to_expiry = 2 * 60

regex_url = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)


with open(cred_filename) as file_in:
    #ctypes.windll.kernel32.SetFileAttributesW(cred_filename,2)
    while not(re.match(regex_url,base_url)):
          base_url = input("Enter a proper url:")
    username = input('Enter User name:')
    key = Fernet.generate_key()
    f = Fernet(key)
    password = f.encrypt(input('Enter password:').encode()).decode()

    try:
          with open(key_file,'w') as key_in:
                key_in.write(key.decode())
                key_exp_start = time.time()
                ctypes.windll.kernel32.SetFileAttributesW(key_file,2)
    except PermissionError:
          os.remove(key_file)
          print("A Permission error occured.\n Please re run the script")
          sys.exit()
 
 

print("**"*20)
print("Cred file created successfully at {},will expire in 2 minutes and for onetime use only."
      .format(time.ctime()))
while(os.path.isfile(key_file)):
      time.sleep(10)
      if (not(time.time() - key_exp_start <= time_for_exp) and os.path.isfile(key_file)):
            os.remove(key_file)
            print("Credentials expired")
            break
print("**"*20)
