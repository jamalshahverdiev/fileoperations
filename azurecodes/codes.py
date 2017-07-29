#!/usr/bin/env python

from azure.storage.file import FileService
file_service = FileService(account_name, account_key1)
#file_service.create_share('myshare')

#file_service.create_directory(
#    'myshare',
#    'uploads',
#)

#from azure.storage.file import FileService

#file_service.put_file_from_path(
#    'myshare',
#        'uploads',
#    'azurefile.txt',
#    'localfile.txt',
#    max_connections=5,
#)


with open('localfile.txt') as localfile:
    file_service.put_file_from_stream(
        'myshare',
            'uploads',
        'remote.txt',
        localfile,
        count=50000,
        max_connections=4,
    )

#file = file_service.get_file_to_path(
#    'myshare',
#        'uploads',
#    'image.png',
#    'downloads/localimage.png',
#    max_connections=8,
#)
