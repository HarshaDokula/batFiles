#Python scripts

1. CreatCred - Creates an encrypted password and puts it into a credential file.
               Default variables in the file are BaseURL, Username and password.

2. RetriveCred - This file is in relation to CreateCred file,
                 It reads the data from CreateCred file and decrypts the password.

3. delete_expired - deletes all the files that go over the expired time. By default time is two days.
                    It requires a "files_list.txt" file storing the file paths to the files to be deleted
