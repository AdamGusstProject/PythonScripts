#######################################
#  Project:  Zip file utility
#  Date:  1-10-2023
#  Version: 3 1-12-2023
########################################

import zipfile
import sys
import pathlib

def menu():
    print('''
    =============================================
    This tool is used for working with zip files:
    =============================================   
    \nSelect and option:
    Option 1, Read the files in a zip
    Option 2, Unzip the files
    Option 3, Creat a zip file
    Option 4. Enter 4 to quit''')

    choice = input('Enter Selection: ')

    if choice == "1":
        read_zipfile()
        menu()
    if choice == "2":
        unzip_files()
        menu()
    if choice == "3":
        zipping_files()
        menu()
    if choice == "4":
        exitScript()


def read_zipfile():
    print('''
    =============================
    Reading the zip file contents
    =============================\n''')

    read_zip = input('What file would you like to read? Enter full path to zip: ')
    try:
        with zipfile.ZipFile(read_zip, 'r') as zip_archive:
            zip_archive.printdir()
    except Exception as e:
        print('There was an error with Option 1: ', e)

def unzip_files():
    print('''
    ====================================
    Unzipping the contents of a zip file
    ====================================\n''')

    zip_file = input('What file would you like unzipped? ')
    unzip_dir = input('Where do you want the files placed? Enter full path to folder: ')

    try: 
       with zipfile.ZipFile(zip_file, 'r') as zip_object:
        #  Static location to drop files, change this location to your own are for the extract
           zip_object.extractall(unzip_dir)
    except Exception as e:
        print('There was an error in Option 2: ', e)

    # List of files that are archived in the zip file
    print(zip_object.namelist())

def zipping_files():
    print('''
    ================================
    Zipping the contents of a folder
    ================================\n''')
    #  Builds out location of files to zip and the name of the zip file to be created
    src_dir = input('What directory are the files to zip: \n')
    zip_name = input('What do you want the zip file name to be: \n')
    print('Zipping files, please wait...\n')

    #  Builds out the directory structure of the files to zip
    directory = pathlib.Path(src_dir) 

    #  Zipping the files and placing them on the root
    try:
        with zipfile.ZipFile(zip_name + ".zip", mode="w") as archive:
            for file_path in directory.iterdir():
                archive.write(file_path, arcname=file_path.name)
                print('The files are being placed up a folder level')
    except Exception as e:
        print('There was an error in Option 3: ', e)
        

def exitScript():
    print('Exiting program')
    sys.exit()

menu()