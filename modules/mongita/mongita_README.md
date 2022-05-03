Mongita Module


[GitHub - scottrogowski/mongita: "Mongita is to MongoDB as SQLite is to SQL"](https://github.com/scottrogowski/mongita
)

GITHUB INTRO:
Mongita is a lightweight embedded document database that implements a commonly-used subset of the MongoDB/PyMongo interface. Mongita differs from MongoDB in that instead of being a server, Mongita is a self-contained Python library. Mongita can be configured to store its documents either on disk or in memory.


## Installation
pip install mongita

Installing collected packages: sortedcontainers, pymongo, mongita

## Important Note about Mongita

Note: By default, MongitaClientDisk stores its data in ~/.mongita. To use a different directory, pass host when initializing client = MongitaClientDisk(host=<db_path>).

MongoDB compatibility: Mongita implements a commonly-used subset of the PyMongo API. This allows projects to be started with Mongita and later upgraded to MongoDB once they reach an appropriate scale.

Limited dependencies: Mongita runs anywhere that Python runs. Currently the only dependencies are pymongo (for bson) and sortedcontainers (for faster indexes).


## TODO:
TODO: Make Class and Class decorators for Mongita



