class Trie:
    head = {}

    def add(self, word, i):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]

        cur['*'] = i

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                print("Pattern not found")
                return False
            cur = cur[ch]
        if '*' in cur:
            print("Pattern found at index", cur["*"])
            return True
        else:
            print("Pattern not found")
            return False

    def load_string(self, string):
        for index in range(len(string)):
            for i in range(len(string)):
                self.add(string[index:len(string)-i], index)




trie = Trie()

trie.load_string("algorithmisfun")
trie.search("fun")
