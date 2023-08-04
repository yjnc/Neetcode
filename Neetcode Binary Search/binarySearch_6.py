from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.keyVal = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyVal[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        # res = ''
        
        # values = self.keyVal.get(key, []) 
        # l, r = 0, len(values) - 1
        
        # while l <= r:
        #     mid = (l + r) // 2
        #     # Get largest possible timestamp st prev timestamp <= timestamp
        #     if values[mid][1] <= timestamp:
        #         res = values[mid][0]
        #         l = mid + 1
        #     else:
        #         r = mid - 1
            
        # return res
    
        # Alternative get() using bisect function
        values = self.keyVal[key]
        idx = bisect.bisect_right(values, timestamp, key=lambda r: r[1])
        if idx == 0:
            return ''

        return values[idx-1][0]






obj = TimeMap()
# ["TimeMap","set","set","get","set","get","get"]
# [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]

obj.set("a","bar",1)
obj.set("x","b",3)
print(obj.get("b",3)) #''

obj.set("foo","bar2",4)
print(obj.get("foo",4)) # bar2
print(obj.get("foo",5)) # bar2