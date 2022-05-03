from monigta import MongitaClientDisk

# [API Documentation — PyMongo 4.1.1 documentation](https://pymongo.readthedocs.io/en/stable/api/index.html)


# Client Function Calls
mongita.MongitaClient.close()
mongita.MongitaClient.list_database_names()
mongita.MongitaClient.list_databases()
mongita.MongitaClient.drop_database(name_or_database)i


# Database Calls
# [database – Database level operations — PyMongo 4.1.1 documentation](https://pymongo.readthedocs.io/en/stable/api/pymongo/database.html)

mongita.Database.list_collection_names()
mongita.Database.list_collections()
mongita.Database.drop_collection(name_or_collection)


# Collection Functions
mongita.Collection.insert_one(document)
mongita.Collection.insert_many(documents, ordered=True)
mongita.Collection.find_one(filter, sort)
mongita.Collection.find(filter, sort, limit)
mongita.Collection.replace_one(filter, replacement, upsert=False)
mongita.Collection.update_one(filter, update)
mongita.Collection.update_many(filter, update)
mongita.Collection.delete_one(filter)
mongita.Collection.delete_many(filter)
mongita.Collection.count_documents(filter)
mongita.Collection.distinct(key, filter)
mongita.Collection.create_index(keys)
mongita.Collection.drop_index(index_or_name)
mongita.Collection.index_information()


# Cursor Functions
mongita.Cursor.sort(key_or_list, direction=None)
mongita.Cursor.next()
mongita.Cursor.limit(limit)
mongita.Cursor.skip(skip)
mongita.Cursor.clone()
mongita.Cursor.close()


# CommandCursor Functions
mongita.CommandCursor.next()
mongita.CommandCursor.close()


# Errors
mongita.errors.MongitaError (parent class of all errors)
mongita.errors.PyMongoError (alias of MongitaError)
mongita.errors.InvalidOperation
mongita.errors.OperationFailure
mongita.errors.DuplicateKeyError
mongita.errors.MongitaNotImplementedError


# Results
mongita.results.InsertOneResult
mongita.results.InsertManyResult
mongita.results.UpdateResult
mongita.results.DeleteResult


# Query Operators
$eq
$gt
$gte
$in
$lt
$lte
$ne
$nin


# Update Operators
$set
$inc
$push
