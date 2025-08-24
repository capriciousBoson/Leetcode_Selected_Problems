from string import ascii_lowercase
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        letters = list(ascii_lowercase)
        words = set(wordList)
        if endWord not in words: return 0
        k = len(beginWord)

        Q = collections.deque()
        Q.append((beginWord, 1))

        while Q:
            wrd, l = Q.popleft()
            
            for i in range(k):
                for char in letters:
                    new_wrd = wrd[0:i]+char+wrd[i+1:]

                    if new_wrd == endWord:
                        return l+1
                    if new_wrd in words:
                        Q.append((new_wrd,l+1))
                        words.remove(new_wrd)
        return 0

        
        