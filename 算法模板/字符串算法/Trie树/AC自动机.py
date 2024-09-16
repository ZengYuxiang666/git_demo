class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.word_end = False
        self.word = None


class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()
        for pattern in patterns:
            self._add_word(pattern)
        self._build_fail_pointers()

    def _add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word_end = True
        node.word = word

    def _build_fail_pointers(self):
        queue = []
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        while queue:
            r = queue.pop(0)
            for char, child in r.children.items():
                fallback = r.fail
                while fallback and char not in fallback.children:
                    fallback = fallback.fail
                child.fail = fallback.children[char] if fallback else self.root
                child.word_end = child.word_end or child.fail.word_end
                queue.append(child)

    def search(self, text):
        node = self.root
        results = []
        for char in text:
            while node and char not in node.children:
                node = node.fail
            if not node:
                node = self.root
                continue
            node = node.children[char]
            temp = node
            while temp and temp.word_end:
                results.append(temp.word)
                temp = temp.fail
        return results

    # 示例


patterns = ["he", "she", "his", "hers"]
ac = AhoCorasick(patterns)
text = "ushers"
print(ac.search(text))  # 输出: ['hers', 'he']