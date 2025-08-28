class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndofWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isEndofWord = True
        return 
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_set = set(words)
        trie_ = Trie()
        for word in words:
            trie_.insert(word)

        rows, cols = len(board), len(board[0])

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        res = []

        def dfs(r, c, node, w):

            char = board[r][c]
            # if char=="#": return
            
            if char in node.children:
                if node.children[char].isEndofWord:
                    res.append(w+char)
                    node.children[char].isEndofWord = False

                
                board[r][c] = "#"

                for dx, dy in dirs:
                    x,y = r+dx, c+dy
                    if 0<=x<rows and 0<=y<cols and board[x][y]!="#":
                        dfs(x,y, node.children[char],w+char)
                
                board[r][c] = char
            else:
                return
        for i in range(rows):
            for j in range(cols):
                dfs(i,j, trie_.root, "" )
        return res






        