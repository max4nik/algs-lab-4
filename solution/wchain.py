class WChain:
    def count_chains(self, file):
        """
        finds the longest possible length of a word chain taken from file
        :param file: name of file to read data from
        :return: the longest possible length of a word chain
        """
        word_chains_len = {word: 1 for word in self._read_words_from_file(file)}
        words = list(word_chains_len.keys())
        for word in words:
            if len(word) == 1:
                continue
            for iterator in range(len(word)):
                word_to_check = word.replace(word[iterator], '', 1)
                if word_to_check in words:
                    word_chains_len[word] = max(word_chains_len[word], word_chains_len[word_to_check] + 1)
        return max(word_chains_len.values())

    def _read_words_from_file(self, filename):
        """
        puts all words from file .in into array and sort it
        :param filename: name of file to read data from
        :return: list of words in file
        """
        words = []
        with open(filename, "r") as file:
            number_of_words = int(file.readline())
            for line in range(number_of_words):
                words.append(file.readline().strip())
        return sorted(words, key=len)
