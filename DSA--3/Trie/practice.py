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
        
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.child:
                return False
        
            current = current.child[char]
        return current.end
    
    def startswith(self,prefix):
        current = self.root
        for char in prefix:
            if char not in current.child:
                return False
            current = current.child[char]
        else: 
            return True 
        
trie = Trie()

words_to_insert = ["apple", "app", "apricot", "banana", "bat"]
for word in words_to_insert:
    trie.insert(word)

print(trie.search("apple"))
print(trie.search("app"))
print(trie.search("apricot"))
print(trie.search("banana"))
print(trie.search("bat"))
print(trie.search("ap"))

print(trie.startswith("ap"))
print(trie.startswith("ba"))
print(trie.startswith("bat"))
print(trie.startswith("bana"))

print(trie.search("orange"))
print(trie.search("grape"))

print(trie.startswith("or"))
print(trie.startswith("gr"))
