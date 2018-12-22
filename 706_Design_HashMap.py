# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap,
# update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping
# for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Example:

# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckets = 10001
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None] * self.itemsPerBuckets
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        if (not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None


class MyHashMap2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [-1] * 1000001

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.table[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.table[key]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        self.table[key] = -1


if __name__ == '__main__':
    obj = MyHashMap2()
    obj.put(1, 2)
    obj.put(1001, 21)
    print(obj.get(1))
    print(obj.get(10011))
    obj.remove(1001)
    print(obj.get(1001))
