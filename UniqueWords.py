"""
JEMAL BESHIR
"""
import re


def get_words(s):
        """ Extract a list of words from string s.

        Args:
        s (str): a string containing one or more words.

        Returns:
        list of str: a list of words from s converted to lower-case.
        """
        words = list()
        s = re.sub(r"--+", " ", s)
        for word in re.findall(r"[\w'-]+", s):
            word = word.strip("'-_")
            if len(word) > 0:
                words.append(word.lower())
        return words
class UniqueWords:
        """ Goes through text files, and finds the unique words 
        within the text files.

        Attributes:
        all_words (set): A set that contains all the words in all added files
        unique_words(set): A set contains all the unique words in one file
        words_by_file (dict): A dictionary that uses a key to store a set of words 
        extracted from the file.

        """
        def __init__(self):
            self.all_words = set()
            self.unique_words = set()
            self.words_by_file = {}
        def add_file(self, filename, key):
            """ Adds a selected file  and keeps record of the words
                in it by reading the file.
                Args:
                - Key (str) : Acts as a nickname to identify file
                - Filename (str) : Acts as a way to find/track a file, and open a file
            """
            with open(filename, "r") as file:
                whole_file = file.read()
                list_words = get_words(whole_file)
                set_of_words = set(list_words)
                self.words_by_file[key] = set_of_words
                self.unique_words -=  self.all_words & set_of_words
                new_words = set_of_words - self.all_words
                self.unique_words.update(new_words)
                self.all_words.update(new_words)
            
        def unique(self, key):
            """ Returns the words that are unique to the file, specified
            by the key.

            Args:
            - Key (str) : Acts as a nickname to identify file

            Returns:
            set: A set of words that are unique to that specified file.
            """
            return self.words_by_file[key] & self.unique_words
            


