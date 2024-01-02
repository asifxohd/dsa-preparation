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
        
    
    def contains(self, word):
        current = self.root
        for char in word:
            if char not in current.child:
                return False
            current = current.child[char]
        return current.end
    
    def prefix_search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.child:
                return False
            current = current.child[char]
            
        result = []
        self.collect_words(current, result, prefix)
        return result
            
        
    def collect_words(self, node, result, current_word):
        if node.end:
            result.append(current_word)
            
        for x, y in node.child.items():
            self.collect_words(y, result, current_word + x)
            
