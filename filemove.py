##########################################################
#  Automate file moves between folders (Static Locations)
#  Creation Date:  2/16/2022
#  Revision:  v3 1/1/2023
##########################################################

#  Modules required for this script to funtion.
import os
import shutil

print('''
============================
===== File Move Script =====
============================
''')

#  Source pathing (Pathing is constant and doesn't require user input).
srcpath = 'D:\Training\Python\scripts\source'
destpath = 'D:\Training\Python\scripts\destination'

#  Creating a list of the files in the source path.
filelist = os.listdir(srcpath)


#  Moving the files from the source (srcpath) location to the destination (destpath).
def filemove():
    print('''Note:
    Moving files, a log has been created with the names of the files moved and has beem placed 
    in the "Source" directory for review.\n''')
    
    try:
        for file_name in filelist:
            if file_name.endswith(('.xlsx')):
                shutil.move(os.path.join(srcpath, file_name), destpath)
    except Exception as e:
        print('There was an error: ', e)


filemove()