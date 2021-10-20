# Hash map implementation in Python

class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_map = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_map[hashed_key]
        found = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found = True
                break
        
        if found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_map[hashed_key]
        found = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found = True
                break
        
        if found:
            return record_val
        else:
            return "No key found"

    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_map[hashed_key]
        found = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found = True
                break
        
        if found:
            bucket.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hash_map)

hash_table = HashMap(50)
  
# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()
  
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
  
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
  
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)