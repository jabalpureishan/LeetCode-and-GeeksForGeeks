class MyHashMap:

    def __init__(self):
        global d
        d = {}
        
        

    def put(self, key: int, value: int) -> None:
        d[key] = value
        

    def get(self, key: int) -> int:
        return d.get(key,-1)
        

    def remove(self, key: int) -> None:
        if key in d:
            d.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)