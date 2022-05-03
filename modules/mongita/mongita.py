from mongita import MongitaClientDisk  

client = MongitaClientDisk() 

hello_world_db = client.hello_world_db

mongoose_collection = hello_world_db.mongoose_collection
mongoose_collection.insert_many([{'name': 'Meercat', 'does_not_eat': 'Snakes'},
                                     {'name': 'Yellow mongoose', 'eats': 'Termites'}])
# returns: <mongita.results.InsertManyResult object at 0x000000000>
    
mongoose_collection.count_documents({})
# returns: 2 
  
mongoose_collection.update_one({'name': 'Meercat'}, {'$set': {"weight": 2}})
# returns: <mongita.results.UpdateResult object at 00000000000>

mongoose_collection.find({'weight': {'$gt': 1}})
# returns: <mongita.cursor.Cursor object at 00000000000>

list(mongoose_collection.find({'weight': {'$gt': 1}}))
# returns: [{'_id': 'a1b2c3d4e5f6', 'name': 'Meercat', 'does_not_eat': 'Snakes', 'weight': 2}]

mongoose_collection.delete_one({'name': 'Meercat'})
# returns: <mongita.results.DeleteResult object at 00000000000>
