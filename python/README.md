# Python scripts

1. CreatCred - Creates an encrypted password and puts it into a credential file.
               Default variables in the file are BaseURL, Username and password.
               Issue: The os.startfile() works only in windows. 

2. RetrieveCred - This file is in relation to CreateCred file,
                 It reads the data from CreateCred file and decrypts the password.

3. delete_expired - deletes all the files that go over the expired time. By default time is two days.
                    It requires a "files_list.txt" file storing the file paths to the files to be deleted

4. expire - The file is used by the CreateCred file to expire the key in the given amount of time.
