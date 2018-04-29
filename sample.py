import string

class Sample():

    data = []
    freq = {}

    def set_sample_from_file(self, path):
        file = open(path)
        self.data = file.read()

    def set_sample_from_string(self, sample):
        self.data = sample

    def get_word_count(self):
        words = self.data.split()
        return len(words)

    def get_word_appearances(self, word):
        words = self.data.split()
        return words.count(word)

    def get_alphanum_count(self):
        alphanum_count = 0
        for char in self.data:
            if char.isalnum():
                alphanum_count += 1
        return alphanum_count

    def get_char_count(self):
        char_count = 0
        for char in self.data:
            char_count += 1;
        return char_count

    def get_char_appearances(self, char):
        return self.data.count(char)

    def get_avg_word_len(self):
        word_count = self.get_word_count()
        alphanum_count = self.get_alphanum_count()
        return (alphanum_count / word_count)

    def get_alphanum_percentage(self):
        char_count = self.get_char_count()
        alphanum_count = self.get_alphanum_count()
        return (alphanum_count / char_count) * 100

    def get_letter_frequencies(self):
        freq = {}
        buff = self.data
        for char in string.ascii_uppercase:
            freq[char] = 0
        for char in buff:
            if char.isalnum():
                freq[char.upper()] = buff.count(char)
            buff.replace(char, '')
        return freq

    def get_word_frequencies(self):
        freq = {}
        words = self.data.split()
        for word in words:
            freq[word] = words.count(word)
        return freq
