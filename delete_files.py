#permanently deleting files and folders
# os.unlink(path)  will delete the file  at path
# os.rmdir(path)  will delete the folder at path ; the folder must be empty
# shutil.rmtree()  will delete the folder at path along with the files and folders in it

import shutil

shutil.rmtree('/home/daniel/Documents/MYSCHEDULE')

#safe deletes with send2trash module
import send2trash

send2trash.send2trash('/home/daniel/Documents/schedule')

