class LRUCache:
    def __init__(self, capacity: int):
        self.dictionary = {}
        self.cap = capacity
        self.lru_keys = [] # most recent last, least recent 0th

    def get(self, key: int) -> int:
        try:
            result = self.dictionary[key]
            #check for key being in lru array, if it is remove and then add it to most recent side
            try:
                index_exists = self.lru_keys.index(key)
                del self.lru_keys[index_exists]
                self.lru_keys.append(key)
            except ValueError:
                self.lru_keys.append(key)

            return result
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        self.dictionary[key] = value
        if len(self.dictionary) > self.cap:
            del self.dictionary[self.lru_keys[0]]
            del self.lru_keys[0]
            try:
                index_exists = self.lru_keys.index(key)
                del self.lru_keys[index_exists]
                self.lru_keys.append(key)
            except ValueError:
                self.lru_keys.append(key)
        else:
            try:
                index_exists = self.lru_keys.index(key)
                del self.lru_keys[index_exists]
                self.lru_keys.append(key)
            except ValueError:
                self.lru_keys.append(key)
        return

if __name__ == '__main__':

    capacity = 2

    obj = LRUCache(capacity)
    print("null")

    obj.put(2, 1)
    print("null")

    obj.put(1, 1)
    print("null")

    obj.put(2, 3)
    print("null")

    obj.put(4, 1)
    print("null")

    param_1 = obj.get(1)
    print(param_1)

    param_1 = obj.get(2)
    print(param_1)
