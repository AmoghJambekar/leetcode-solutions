class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            if not(key in groups):
                groups[key] = [word]
            else:
                groups[key].append(word)
        return groups.values()
