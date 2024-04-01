#assuming you have a folder that contains subfolders with files in them, you may want to traverse through all the
# files in the subfolders
# os.walk() allows one to do this

import os

for foldername, subfolders,filenames in os.walk('/home/daniel/Documents/trial'):
    print('The current folder is : '+foldername)

    for subfolder in subfolders:
        print('SUBFOLDER of '+foldername +':  '+ subfolder)

    for filename in filenames:
        print('FILE IN '+subfolder + ':' +filename)
    print('\n')