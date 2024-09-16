class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向Trie树中插入一个单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        在Trie树中搜索一个单词
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        判断Trie树中是否存在以某个前缀开头的单词
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # 示例用法


trie = Trie()
words = ["apple", "app", "banana", "bat", "batman", "bee"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # 输出: True
print(trie.search("app"))  # 输出: True
print(trie.search("batman"))  # 输出: True
print(trie.search("batmanx"))  # 输出: False
print(trie.starts_with("bat"))  # 输出: True
print(trie.starts_with("bee"))  # 输出: True
print(trie.starts_with("ball"))  # 输出: False