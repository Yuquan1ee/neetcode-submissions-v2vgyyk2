class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = {}
        self.unique_val = 0
        self.key_latest_index = {}
        self.holding_list = []
        self.counter = 0

    def get(self, key: int) -> int:
        print(self.key_value)
        if key in self.key_value:
            
            print("having key")
            self.key_latest_index[key] = len(self.holding_list)
            self.holding_list.append(key)
            return self.key_value[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key not in self.key_value:
            self.unique_val += 1
        
        self.key_value[key] = value
        self.key_latest_index[key] = len(self.holding_list)
        self.holding_list.append(key)

        
        while(self.unique_val > self.capacity):
            print("deleting")
            print(f"{self.unique_val},{self.capacity}" )
            if self.counter < self.key_latest_index[self.holding_list[self.counter]]:
                self.counter += 1
            else: 
                self.unique_val -= 1
                del self.key_latest_index[self.holding_list[self.counter]]
                del self.key_value[self.holding_list[self.counter]]
                self.counter += 1

        
       
