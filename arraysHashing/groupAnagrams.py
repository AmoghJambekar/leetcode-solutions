class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}
        
        if strs < 0:
            return [""]

        for word in strs:
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return groups.values()

    
        