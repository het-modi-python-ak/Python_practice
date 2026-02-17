# 3. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

#     An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#     Constraints:

#         - 1 <= strs.length <= 104

#         - 0 <= strs[i].length <= 100

#         - strs[i] consists of lowercase English letters.

#     Example 1:

#         - Input: strs = ["eat","tea","tan","ate","nat","bat"]

#         - Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#     Example 2:

#         - Input: strs = [""]

#         - Output: [[""]]

#     Example 3:

#         - Input: strs = ["a"]

#         - Output: [["a"]]


from collections import defaultdict

w = ["eat", "tea", "tan", "ate", "nat", "bat"]


a = defaultdict(list)
for word in w:
    s = ''.join(sorted(word))  #becomes key 
    a[s].append(word) #adding value to key

res = list(a.values())
print(res)

# second approach



def groupanagrams(strs):
    anagramdict = defaultdict(list)
    
    for word in strs:
        count = [0] * 26  # 26 letters
        
        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1
        
        key = tuple(count) 
        anagramdict[key].append(word)
    
    return list(anagramdict.values())


# Example
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupanagrams(strs))