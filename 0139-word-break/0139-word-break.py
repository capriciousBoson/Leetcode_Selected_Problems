class Node:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.isEndOfWord = True
    


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # words = set(wordDict)
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        memo = {}
        def dfs(idx):
            if idx >= n:
                return True
            if idx not in memo:
                memo[idx] = False
                current = trie.root

                for i in range(idx, n):
                    if s[i] in current.children:
                        current = current.children[s[i]]
                        if current.isEndOfWord:
                            found = dfs(i+1)
                            # memo[idx] = memo[idx] or dfs(i+1)
                            if found:
                                memo[idx] = True
                                return memo[idx]

                    else:
                        # memo[idx] = False
                        break
            return memo[idx]
            # return False

        return dfs(0)
                



