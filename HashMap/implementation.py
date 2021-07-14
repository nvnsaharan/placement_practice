# dictionary dict
# map
# hash table
# associative array


class HashMap:
    def __init__(self):
        self.size = None  # A VERY Big number
        self.map = [None] * self.size

    def get_hash(self, key):
        # convert key into a large distinct number
        pass

    def add(self, key, value):
        key_hash = self.get_hash(key)
        # store value in key_hash we get if no value before
        if self.map[key_hash] is None:
            self.map[key_hash] = value
            return True
        else:
            # key already assigned
            return False

    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash]:
            return self.map[key_hash]
        return None

    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            return False
        else:
            self.map[key_hash] = None
            return True

    def print(self):
        for i in self.map:
            print(i, end=" ")
