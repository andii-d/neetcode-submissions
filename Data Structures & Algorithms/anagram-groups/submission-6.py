class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put each word into a set of its letters 

        hashmap = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)

        return list(hashmap.values())