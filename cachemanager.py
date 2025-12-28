import json
import os
import hashlib

class CacheManager:
    def __init__(self):
        # Create cache folder when CacheManager is created
        self.cache_dir = 'cache'
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def urlhasher(self,url):
        hash_object = hashlib.md5(url.encode())
        filename = hash_object.hexdigest()  # Gets something like "5f2b8c9a3d1e4f6b"
        # print(f"URL: {url}")
        # print(f"Filename: {filename}.json")   
        return filename
        

    def get(self, url):
        # Check if this URL is cached
        # For now, use simple filename (we'll improve this later)
        url=self.urlhasher(url)
        filename = f"{self.cache_dir}/{url}.json"
        
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return None  # Not found in cache
    
    def set(self, url, response_data):
        # Save response to cache
        oldurl=url
        url=self.urlhasher(url)

        filename = f"{self.cache_dir}/{url}.json"
        with open(filename, 'w') as f:
            json.dump(response_data, f)
        print(f"{oldurl} CACHED!")
    def clear(self):
        # Delete all cached files
        for filename in os.listdir(self.cache_dir):
            file_path = os.path.join(self.cache_dir, filename)
            os.remove(file_path)
        print("Cache cleared!")
