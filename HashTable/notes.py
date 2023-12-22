"""
A hash table is a data structure that allows for quick insertion,
deletion, and retrieval of data. It works by using a hash function 
to map a key to an index in an array. In this article, we will implement 
a hash table in Python using separate chaining to handle collisions.
"""

"""
Separate chaining is a technique used to handle collisions in a hash table.
When two or more keys map to the same index in the array, we store them in a linked list at that index.
This allows us to store multiple values at the same index and still be able to retrieve them using their key.
"""


"""
Time Complexity and Space Complexity:

**
The time complexity of the insert, search and remove methods in a
hash table using separate chaining depends on the size of the hash table,
the number of key-value pairs in the hash table, and the length of the linked list at each index.

**
Assuming a good hash function and a uniform distribution of keys
, the expected time complexity of these methods is O(1) for each operation. However,
in the worst case, the time complexity can be O(n),
where n is the number of key-value pairs in the hash table.

**
However, it is important to choose a good hash function
and an appropriate size for the hash table to minimize the likelihood of 
collisions and ensure good performance.

**
The space complexity of a hash table using separate chaining depends
on the size of the hash table and the number of key-value pairs stored in the hash tab

**
complexity for the worst case analysis is Order(N) for all operation this occures
when multiple collishion happens that time it may not gonna be efficiant
"""



"""APPLICATION OF HASHTABLE"""
'''
** Domain Name System (DNS) servers use hashtables to quickly resolve domain names to IP addresses

** Natural Language Processing:
    In applications involving text processing and natural language understanding,
    hashtables can be used for efficient storage and retrieval of linguistic information.

** Cryptographic Applications:
    Hashtables play a role in cryptographic hash functions and digital signatures, 
    providing fast data integrity verification.
    
'''


""" TYPES OF HASH FUNCTIONS """
'''
1. Cryptographic Hash Functions:

    In simple terms, a cryptographic hash function is like a magic blender
    that takes any piece of information, whether it's a password, a file,
    or a message, and turns it into a fixed-size jumble of characters that looks random.
    This jumble is unique to the original information, and even a tiny change to the original 
    will create a completely different jumble.

2. Non-Cryptographic Hash Functions
    it's not designed to be super secure or resistant to certain types of attacks.
    Instead, it's chosen for its speed and simplicity.

3. Checksums:
    checksum hashing is a way to create a unique fingerprint for data,
    making it easy to detect any changes or errors. It's not designed for 
    security like cryptographic hashing but is effective for ensuring data integrity.
    
'''

"""  Separate chaining """