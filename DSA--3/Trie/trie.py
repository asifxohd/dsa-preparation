class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.end = False
        

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.child:
                current.child[char] = TrieNode()
            current = current.child[char]
        current.end = True
        
    
    def search (self, word):
        current = self.root
        for char in word:
            if char not in current.child:
                return False
            current = current.child[char]
        return current.end
    
    
    def startswith(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.child:
                return False
            current = current.child[char]
        return True
    
    