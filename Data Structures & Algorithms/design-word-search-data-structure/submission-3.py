class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for index, char in enumerate(word): 
            if char == '.':
                for child_char in curr.children:
                    if self.search(word[:index] + child_char + word[index + 1:]):
                        return True
                return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return curr.word
