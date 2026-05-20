class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #sorted_string: list of words
        res = []

        for i in strs:
            s = "".join(sorted(i))
            if s in hashmap:
                hashmap[s].append(i)
            else:
                hashmap[s] = [i]


        for key, value in hashmap.items():
            res.append(value)

        return res            


        