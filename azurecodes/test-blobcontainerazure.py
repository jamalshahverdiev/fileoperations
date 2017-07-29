#!/usr/bin/env python

from azure.storage.blob import BlockBlobService
block_blob_service = BlockBlobService(myaccount, mykey)

#### Create container with name "mycontainer"
#block_blob_service.create_container('mycontainer')

#### By default container is private so, if we want do this container public we must will do as following:
#from azure.storage.blob import PublicAccess
#block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)
#### Alternate way for PUBLIC
#block_blob_service.set_container_acl('mycontainer', public_access=PublicAccess.Container)


#### The following example uploads the contents of the sunset.png file into the "myblockblob" blob.
#from azure.storage.blob import ContentSettings
#block_blob_service.create_blob_from_path(
#    'mycontainer',
#    'remotef.txt',
#    'localfile.txt',
#    content_settings=ContentSettings(content_type='text/html')
#            )

#### To list the blobs in a container, use the list_blobs method. This method returns a generator. 
#### The following code outputs the name of each blob in a container to the console.
#generator = block_blob_service.list_blobs('mycontainer')
#for blob in generator:
#    print(blob.name)

#### The following example demonstrates using get_blob_to_path to download the contents of the myblob blob and store it to the out-sunset.png file.
#block_blob_service.get_blob_to_path('mycontainer', 'remotef.txt', 'fromazure-out.txt')

#### Finally, to delete a blob, call delete_blob.
#block_blob_service.delete_blob('mycontainer', 'myblockblob')

#### The example below creates a new append blob and appends some data to it, simulating a simple logging operation.
#from azure.storage.blob import AppendBlobService
#append_blob_service = AppendBlobService(myaccount, mykey)
####The same containers can hold all types of blobs
#append_blob_service.create_container('mycontainer')
#Append blobs must be created before they are appended to
#append_blob_service.create_blob('mycontainer', 'myappendblob')
#append_blob_service.append_blob_from_text('mycontainer', 'myappendblob', u'Sinaq, cumle!')
#append_blob = append_blob_service.get_blob_to_text('mycontainer', 'myappendblob')
#print(append_blob)

