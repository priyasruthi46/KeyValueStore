# KeyValueStore

A Key-Value based data store that supports the basic CRD (create, read, delete) operations. This data store is meant to be used as a local data store for one process on a laptop. It can be exposed as a library to the clients.

I used python programming language to solve the problem statement. 
The data store supports the following functionalities:

1. Key - value pairs can be added to the data store using create. The key is always a string which is mapped to the value which is a JSON object. It is capped at 16KB while the key is capped at 32 characters.


2. If a new value is being inserted for an existing key, it will result in an error. Also, there is a time-to-live property for each pair in the datastore and if that time expires, no operations can be performed on that pair.

3. Appropriate error messages are displayed whenever the memory limit is expired or illegal operations are performed on the database.

It also supports the following non-functional requirements :

-> The size of the datastore is limited to 1GB only.
-> There can be a chance where client process can create multiple threads and access the datastore making it threadsafe. 
-> Very little memory is needed and in response we will have maximum performance. 
