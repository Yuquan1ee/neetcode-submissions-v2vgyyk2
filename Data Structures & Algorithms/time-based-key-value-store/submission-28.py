class TimeMap:

    def __init__(self):
        self.dict_map = {} # {key:[(timestamp, value)]}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict_map:
            self.dict_map[key] = []
        self.dict_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_map:
            return ""
        elif timestamp<self.dict_map[key][0][0]:
            return ""
        start_index = 0
        print(f"{key},{self.dict_map[key]}")
        end_index = len(self.dict_map[key]) - 1
        while(start_index <= end_index):
            mid_index = (start_index + end_index)//2
            if self.dict_map[key][mid_index][0] == timestamp:
                return self.dict_map[key][mid_index][1]
            elif self.dict_map[key][mid_index][0] > timestamp:
                end_index = mid_index -1
            elif self.dict_map[key][mid_index][0] < timestamp:
                start_index = mid_index + 1
        
        
        return self.dict_map[key][end_index][1]