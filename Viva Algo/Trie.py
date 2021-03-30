class TrieNode:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = []

    def contains(self, letter):
        letters = [child.letter for child in self.children]
        if letter in letters:
            return True
        else:
            return False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        for i in range(len(word)):
            curr_node = self.root
            for i in word:
                if not curr_node.contains(i):
                    curr_node.children.append(TrieNode(letter=i))
                curr_node = list(
                    filter(lambda child: child.letter == i, curr_node.children))[0]
            word = word[1:]

    def search(self, word):
        curr_node = self.root
        found = False
        for i in word:
            if not curr_node.contains(i):
                found = False
            else:
                curr_node = list(
                    filter(lambda child: child.letter == i, curr_node.children))[0]
                found = True
        return found


trie = Trie()
trie.addWord("algorithmisfun")
print(trie.search("fun"))
