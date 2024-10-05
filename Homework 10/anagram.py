def isAnagram(word1, word2) :
    
    if sorted(word1) == sorted(word2) :
        return True
    else :
        return False
    
anagram_or_not_1 = isAnagram("silent", "listen")
anagram_or_not_2 = isAnagram("banana", "annabel")
anagram_or_not_3 = isAnagram("mace", "came")
print(anagram_or_not_1)
print(anagram_or_not_2)
print(anagram_or_not_3)