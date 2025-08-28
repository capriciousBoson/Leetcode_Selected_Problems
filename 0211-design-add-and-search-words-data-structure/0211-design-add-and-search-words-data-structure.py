class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEndofWord = True
        return
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i==len(word):
                return node.isEndofWord
            char = word[i]

            if char == ".":
                found = False
                for c in node.children:
                    found = found or dfs(i+1, node.children[c])
                return found

            if char in node.children:
                return dfs(i+1, node.children[char])
            else:
                return False
        
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)