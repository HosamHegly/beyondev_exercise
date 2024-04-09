class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


    def hashFunc(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        i = self.hashFunc(key)
        if self.table[i] is None:
            self.table[i] = Node(key, value)
            self.size += 1
        else:
            current = self.table[i]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            n = Node(key, value)
            n.next = self.table[i]
            self.table[i] = n
            self.size += 1


    def delete(self, key):
        if self.table[self.hashFunc(key)] is None:
            print("error in key ", key)
            return

        current = self.table[self.hashFunc(key)]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[self.hashFunc(key)] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        print("error in key " ,key)

    def search(self, key):


        current = self.table[self.hashFunc(key)]

        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        print("error key not found", key)


if __name__ == "__main__":
    new_hash = Hashtable(5)
    new_hash.insert("hello","world")
    new_hash.insert("1",1)
    new_hash.insert("2",2)
    new_hash.insert("hosam",True)

    print(new_hash.search("hello"))

    print(new_hash.search("1"))
    print(new_hash.search("2"))
    print(new_hash.search("hosam"))

    new_hash.delete("1")
    print(new_hash.search("1"))


