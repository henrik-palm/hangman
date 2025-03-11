import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.words = set()

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.length_index = collections.defaultdict(set)
    
    def insert(self, word):
        """Insert a word into the Trie and index it by length."""
        node = self.root
        self.length_index[len(word)].add(word)
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.add(word)
        node.is_end_of_word = True
    
    def search_pattern(self, pattern, guessed):
        """Returns words matching the current pattern with exact letter positions, considering word length."""
        possible_words = self.length_index[len(pattern)]
        return [word for word in possible_words if self._matches_pattern(word, pattern, guessed)]
    
    def _matches_pattern(self, word, pattern, guessed):
        """Check if a word matches the given pattern and guessed letters."""
        for w, p in zip(word, pattern):
            if p != "_" and p != w:
                return False
            if p == "_" and w in guessed:
                return False
        return True

def build_trie(words):
    """Build a Trie from a list of words."""
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie