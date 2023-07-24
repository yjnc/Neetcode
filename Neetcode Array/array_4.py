
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #initialize to default dictionary to get rid of need to worrying about whether key alrdy exists or not
        anagrams = defaultdict(list)
        print("anagrams:", anagrams)

        #count up number of each alphabet for each str
        for s in strs:
            #26 for each alphabet
            count = [0] * 26
            #counting up number of char
            for c in s:
                #whatever value the alphabet is assigned via computer, we get correct index by subtracting it from value of "a"
                count[ord(c) - ord("a")] += 1
            
            #add the string for the corresponding count
            anagrams[tuple(count)].append(s) 
        
        #return just the values, already in correct format
        return anagrams.values()

    # alternative solution: (uses sorted method and join to turn list into one string)
    # for example: ['a', 'e', 't'] using join becomes ['aet']
    #
    #  d = {}
    #     for s in strs:
    #         sorted_s = ''.join(sorted(s))
    #         if sorted_s in d:
    #             d[sorted_s].append(s)
    #         else:
    #             d[sorted_s] = [s]
    #     return d.values()


solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))
                    

        