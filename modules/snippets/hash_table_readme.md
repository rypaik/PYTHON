SOURCE:
[How to Implement a Hash Table in Python](https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd)

[education/hashtable.py at master · pagekeysolutions/education](https://github.com/pagekeysolutions/education/blob/master/HashTable/hashtable.py)


[education/test_hashtable.py at master · pagekeysolutions/education](https://github.com/pagekeysolutions/education/blob/master/HashTable/test_hashtable.py)


``` python
# Create a new HashTable

ht = HashTable()
# Create some data to be stored

phone_numbers = ["555-555-5555", "444-444-4444"]
# Insert our data under the key "phoneDirectory"

ht.insert("phoneDirectory", phone_numbers)
# Do whatever we need with the phone_numbers variable

phone_numbers = None
... # Later on...

# Retrieve the data we stored in the HashTable

phone_numbers = ht.find("phoneDirectory")
# find() retrieved our list object

# phone_numbers is now equal to ["555-555-5555", "444-444-4444"]



# FIELDS
class HashTable
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None] * self.capacity
  
  
# HASH TABLE NODE
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
        
# HASH FUNCTION
def hash(self, key):
    	hashsum = 0
	# For each character in the key

	for idx, c in enumerate(key):
		# Add (index + length of key) ^ (current char code)

		hashsum += (idx + len(key)) ** ord(c)
		# Perform modulus to keep hashsum in range [0, self.capacity - 1]

		hashsum = hashsum % self.capacity
	return hashsum


# INSERT FUNCTION
def insert(self, key, value):
    	# 1. Increment size

	self.size += 1
	# 2. Compute index of key

	index = self.hash(key)
	# Go to the node corresponding to the hash

	node = self.buckets[index]
	# 3. If bucket is empty:

	if node is None:
		# Create node, add it, return

		self.buckets[index] = Node(key, value)
		return
	# 4. Collision! Iterate to the end of the linked list at provided index

	prev = node
	while node is not None:
		prev = node
		node = node.next
	# Add a new node at the end of the list with provided key/value

	prev.next = Node(key, value)
 
 
 
 
 
 
 # FIND FUNCTION
 def find(self, key):
    	# 1. Compute hash

	index = self.hash(key)
	# 2. Go to first node in list at bucket

	node = self.buckets[index]
	# 3. Traverse the linked list at this node

	while node is not None and node.key != key:
		node = node.next
	# 4. Now, node is the requested key/value pair or None

	if node is None:
		# Not found

		return None
	else:
		# Found - return the data value

		return node.value




# REMOVE FUNCTION
def remove(self, key):
    	# 1. Compute hash

	index = self.hash(key)
	node = self.buckets[index]
	prev = None
	# 2. Iterate to the requested node

	while node is not None and node.key != key:
		prev = node
		node = node.next
	# Now, node is either the requested node or none

	if node is None:
		# 3. Key not found

		return None
	else:
		# 4. The key was found.

		self.size -= 1
		result = node.value
		# Delete this element in linked list

		if prev is None:
			node = None
		else:
			prev.next = prev.next.next
		# Return the deleted language

		return result





```