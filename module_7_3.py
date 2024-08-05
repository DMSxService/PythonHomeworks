class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as strings:
                string = strings.read().lower()
                punctuation = ',.=!?;:'
                result_string = ''.join(char for char in string if char not in punctuation)
                result_string = result_string.replace(' - ', ' ')
                for i in range(0, len(result_string)):
                    all_words[name] = result_string.split()
        return all_words

    def find(self, word):
        pos = {}
        search = word.lower()
        for names, words in self.get_all_words().items():
            i = 0
            for i in range(0, len(words)):
                if search == words[i]:
                    i += 1
                    break
            pos[names] = i
        return pos

    def count(self, word):
        entry = {}
        search = word.lower()
        for names, words in self.get_all_words().items():
            j = 0
            for i in range(0, len(words)):
                if search == words[i]:
                    j += 1
            entry[names] = j
        return entry


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
