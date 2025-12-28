import requests
import argparse
import os
import json
import hashlib

from cachemanager import CacheManager



def create_cache_folder():
    # Create a folder
    if not os.path.exists('cache'):
        os.makedirs('cache')
        print("Cache folder created!")

def urlhasher(url):
    hash_object = hashlib.md5(url.encode())
    filename = hash_object.hexdigest()  # Gets something like "5f2b8c9a3d1e4f6b"

    print(f"URL: {url}")
    print(f"Filename: {filename}.json")


#parser for port number and url command line
parser=argparse.ArgumentParser()
#postitional arguments
parser.add_argument('port',help='port number to listen to')
parser.add_argument('url',help='url to forward requests to')
#optional arguments
parser.add_argument('--clear-cache', action='store_true', help='Clear the cache')
# parser.add_argument('--clear-cache',help='clears previous cache',choices=['y','n'])

#initialisation of args
args=parser.parse_args()

#print output of received args
print(f'arg 1 is : {args.port}')
print(f'arg 2 is : {args.url}')
print(f'arg 3 is : {args.clear_cache}')




# main
create_cache_folder()

fake_response = {
    'url': 'http://dummyjson.com/products',
    'status_code': 200,
    'content': 'Some product data here'
}



cachemgr=CacheManager()
#clear cache logic
if args.clear_cache:
    cachemgr.clear()









    

# cachemgr.set('w',fake_response)

# fake_response["content"]="sex"
# cachemgr.set('ww',fake_response)

# fake_response["content"]="sexx"
# cachemgr.set('www',fake_response)

# fake_response["content"]="sexxx"
# cachemgr.set('wwww',fake_response)

# fake_response["content"]="sexxxx"
# cachemgr.set('wwwww',fake_response)

# fake_response["content"]="sexxxxx"
# cachemgr.set('wwwww',fake_response)

# print ("----------------------------------------------------------------------")

# print(cachemgr.get('w'))
# print(cachemgr.get('ww'))
# print(cachemgr.get('www'))
# print(cachemgr.get('wwww'))
# print(cachemgr.get('wwwww'))
# print(cachemgr.get('wwwww'))

# print(cachemgr.get('wjjh'))
# cachemgr.clear()


#cachemanager











# # Pretend we got this response from a server
# fake_response = {
#     'url': 'http://dummyjson.com/products',
#     'status_code': 200,
#     'content': 'Some product data here'
# }

# # Save it to a file in cache folder
# filename = 'cache/products.json'
# with open(filename, 'w') as f:
#     json.dump(fake_response, f)
    
# print(f"Saved to {filename}")

# import json
# import os

# # Check if the file exists
# filename = 'cache/products.json'

# if os.path.exists(filename):
#     # File exists - read it
#     with open(filename, 'r') as f:
#         cached_data = json.load(f)
#     print("Found in cache!")
#     print(cached_data)
# else:
#     print("Not in cache - need to fetch from server")




