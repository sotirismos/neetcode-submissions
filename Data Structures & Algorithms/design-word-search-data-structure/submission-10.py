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

    def search(self, word: str, curr: TrieNode | None = None) -> bool:
        if not curr:
            curr = self.root
        for index, char in enumerate(word):
            if char != '.' and char in curr.children:
                curr = curr.children[char]

            elif char != '.' and char not in curr.children:
                return False

            else:
                for child in curr.children.values():
                    if self.search(word[index + 1:], curr = child):
                        return True
                return False

        return curr.word  
