# Design a HashSet without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Example:

# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBucket = 1001
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if not self.table[hashkey]:
            self.table[hashkey] = [0] * self.itemsPerBucket
        self.table[hashkey][self.pos(key)] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        hashkey = self.hash(key)
        if self.table[hashkey]:
            self.table[hashkey][self.pos(key)] = 0

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        hashkey = self.hash(key)
        return (self.table[hashkey] != []) and (self.table[hashkey][self.pos(key)] == 1)


if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(12)
    obj.add(1002)
    print(obj.contains(12))
    print(obj.contains(133))
    obj.add(12)
    print(obj.contains(12))
    obj.remove(1002)
    print(obj.contains(1002))
