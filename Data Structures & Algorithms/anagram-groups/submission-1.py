class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        
        '''
        1.
        [0] * 26 -> counter
        2.
        using HM (defaultdict(list)) if sorted(word) == key; include word
        '''
        res = defaultdict(list)
        for word in words:
            frequencyCount = [0] * 26
            for char in word:
                frequencyCount[ord(char) - ord('a')] += 1
            res[tuple(frequencyCount)].append(word)
        return list(res.values())
            
                