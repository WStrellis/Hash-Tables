# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def insert_after(self, new_node):
        self.next = new_node


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # hash the key
        hashed_key = self._hash(key)
        # choose a place in the list to add the element
        key_ind = self._hash_mod(hashed_key)
        # check if a node exists at that index
        current = self.storage[key_ind]
        if not current:
            # insert new_node at index
            self.storage[key_ind] = LinkedPair(key, value)
            return
        while current:
            if current.key == key:
                # if the key already exists update the value
                current.value = value
                break
            elif current.next:
                current = current.next
            else:
                # add new_node to chain
                current.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash the input key
        hashed_key = self._hash(key)
        # get index
        index = self._hash_mod(hashed_key)
        # if there is one item at the specified index delete it
        storage_item = self.storage[index]

        if storage_item:
            # if there are multiple items at the index find the one with the matching key and delete it from the chain
            while storage_item:
                if storage_item.key == key:
                    self.storage[index] = storage_item.next if storage_item.next else None
                # get next node if key doesn't match
                storage_item = storage_item.next

        # if the key was not found return error message
        else:
            print(f'ERROR: key:{key} does not exist')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash the key
        hashed_key = self._hash(key)
        # get index
        index = self._hash_mod(hashed_key)
        # get node at index
        node = self.storage[index]
        value = None
        # find the node with the matching key
        while node:
            if node.key == key:
                value = node.value
                break
            node = node.next
        return value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        old_capacity = self.capacity
        # calc new capacity
        new_capacity = self.capacity * 2
        # create new storage object
        new_storage = [None] * new_capacity
        # set capacity
        self.capacity = new_capacity
        # set storage
        self.storage = new_storage
        # hash the key of every value in the old
        # storage object and insert into new storage object
        for i in range(old_capacity):
            node = old_storage[i]
            print(node)
            while node:
                # hash the key
                # hashed_key = self._hash(node.key)
                # get index
                # index = self._hash_mod(hashed_key)
                # new_storage[index] = node
                self.insert(node.key, node.value)
                # get next node
                node = node.next


if __name__ == "__main__":
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")
    # print(ht.storage)

    # print("")

    # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_1", "knuckle sandwich")
    # print(ht.retrieve('line_1'))
    # print(ht.storage)
    # ht.remove('line_1')
    # print(ht.storage)

    ht = HashTable(3)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "fish sandwich")
    ht.insert("line_3", "pork taco")
    # ht.retrieve('anana')
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
