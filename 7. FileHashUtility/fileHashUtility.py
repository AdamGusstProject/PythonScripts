#######################################
#  Project:  Hashing file utility
#  Date:  1-18-2023
#  Version: 
########################################

#  Modules to import
import os
from filehash import FileHash

#  Requesting file you need the hash from

print('''
    ==================================
    Provides the following hash values
    (md5, SHA215, SHA512)
    ==================================\n''')

file_to_hash = input('What is the file you want a hash of?  Drop file here: ')

def getFileHash():
    
    md5hasher = FileHash('md5')
    sha256hasher = FileHash('sha256')
    sha512hasher = FileHash('sha512')

    test1 = md5hasher.hash_file(file_to_hash)
    test2 = sha256hasher.hash_file(file_to_hash)
    test3 = sha512hasher.hash_file(file_to_hash)

    print('md5 hash = ', test1)
    print('sha256 hash = ', test2)
    print('sha512 hash = ', test3)

getFileHash()
