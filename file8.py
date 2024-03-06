#all in one
import os

def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write('Hello World\n')
            print('File' +filename +'created successfully.')
    except IOError:
        print('Error: Could not create the file '+filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content=f.read()
            print(content)
    except IOError:
        print('Error: could not read the file '+filename)

def append_file(filename,text):
    try:
        with open(filename,'a') as f:
            f.write(text)
            print('Text appended on the file '+filename+'successfully')
    except IOError:
        print('Error :could not append to the file '+filename)

def rename_file(filename,new_filename):
    try:
        os.rename(filename,new_filename)
        print("File "+filename + "renamed to "+new_filename +"successfully")
    except IOError:
        print('Error: could not rename the file '+filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print('File '+filename +'successfully deleted')
    except IOError:
        print('Error: could not delete the file' +filename)


if __name__ == '__main__':
    filename='example.txt'
    new_filename='new_example.txt'


create_file(filename)
read_file(filename)
append_file(filename ,'This is some additional text\n')
read_file(filename)
rename_file(filename,new_filename)
read_file(new_filename)
delete_file(new_filename)