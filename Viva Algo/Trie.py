class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        for i in range(len(word)):
            curr_node = self.root
            for i in word:
                if i not in curr_node.children:
                    curr_node.children[i] = TrieNode()

                curr_node = curr_node.children[i]
                curr_node.isWord = True

            word = word[1:]

    def search(self, word):
        curr_node = self.root

        for i in word:
            if i not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[i]

        return curr_node.isWord


trie = Trie()
trie.addWord("algorithmisfun")
print(trie.search("fun"))
