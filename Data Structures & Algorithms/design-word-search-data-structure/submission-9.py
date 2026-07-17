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
            if char != '.' and char not in curr.children:
                return False
            if char != '.' and char in curr.children:
                curr = curr.children[char]
            if char == '.':
                for child in curr.children:
                    if self.search(word[:index] + child + word[index + 1:]):
                        return True
                return False
        return curr.word
