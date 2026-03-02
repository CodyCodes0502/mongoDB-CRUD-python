# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'password123' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try:
                self.collection.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                print("Something went wrong")
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            try:
                results = self.collection.find(data)
                return list(results)
            except Exception as e:
                print("Something went wrong")
                return []
        else:
            raise Exception("Nothing to save because data parameter is empty")
            
    #The U in CRUD, Update.
    def update(self, data, new_data):
        if data is not None and new_data is not None:
            try:
                x = self.collection.update_many(data, new_data)
                return x.modified_count
            except Exception as e:
                print("Something went wrong:", e)
                return 0
        else:
            raise Exception("Nothing to update or nothing to update to")
                
    
    #The D in CRUD
    def delete(self, data):
        if data is not None:
            try:
                x = self.collection.delete_many(data)
                return x.deleted_count
            except Exception as e:
                print("Something went wrong, could not delete")
                return 0
            else:
                raise Exception("Nothing to delete")