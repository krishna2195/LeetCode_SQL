class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        charWord = {}
        wordChar = {}
        
        for ch, word in zip(pattern, words):
            if ch in charWord:
                if charWord[ch] != word:
                    return False
            else:
                if word in wordChar and wordChar[word] != ch:
                    return False
                charWord[ch] = word
                wordChar[word] = ch
                
        return True