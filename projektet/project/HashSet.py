from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_value = int()
        num = 1
        for i in word:
            hash_value += ord(i) ** num
            num += 1
        result = hash_value % len(self.buckets)
        return result

    # Doubles size of bucket list
    def rehash(self):
        copy_lst = list(self.buckets)
        self.buckets = [[] for i in range(len(copy_lst) * 2)]
        for lists in copy_lst:
            for content in lists:
                self.add(content)

    # Adds a word to set if not already added
    def add(self, word):
        value = self.get_hash(word)
        if word not in self.buckets[value]:
            self.buckets[value].append(word)
            self.size += 1
        if self.size == len(self.buckets):
            self.size = 0
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        string = '{ '
        for lists in self.buckets:
            for content in lists:
                string += content + " "
        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        value = self.get_hash(word)
        for content in self.buckets[value]:
            if content is word:
                return True
            else:
                return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        value = self.get_hash(word)
        for content in self.buckets[value]:
            if content is word:
                self.size -= 1
                self.buckets[value].remove(content)

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        size_max = int()
        for x in max(self.buckets, key=len):
            size_max += 1
        return size_max

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        o_buckets = int()
        for bucket in self.buckets:
            if len(bucket) == 0:
                o_buckets += 1
        ratio = round(o_buckets / self.bucket_list_size(), 2)
        return ratio
