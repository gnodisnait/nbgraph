"""
given an embedding file of words, we extract all words from this file, and save them in a new file
"""
from nbgraph.config import FileWord2Vec, FileVoc, FileWS, TestFWord2Vec, TestFVoc, TestFWS
from nbgraph.util_voc import create_vocabulary, get_voc_list, create_word_sense_file
import unittest


class VocTest(unittest.TestCase):

    def test_create_vocabulary_file(self):
        self.assertEqual(create_vocabulary(w2vFile='asdf', vocFile=''), 'file does not exist: asdf')
        self.assertEqual(create_vocabulary(w2vFile=TestFWord2Vec, vocFile=TestFVoc), 2)
        if create_vocabulary(w2vFile=TestFWord2Vec, vocFile=TestFVoc) == 2 and False:
            create_vocabulary(w2vFile=FileWord2Vec, vocFile= FileVoc)

    def test_get_voc_list(self):
        self.assertEqual(get_voc_list("asdf"), 'file does not exist: asdf')
        self.assertEqual(get_voc_list(TestFVoc), ['apple', 'cat'])
        if get_voc_list(TestFVoc) == ['apple', 'cat'] and False:
            vlst = get_voc_list(FileVoc)
            print(len(vlst))

    def test_create_word_sense_file(self):
        self.assertEqual(create_word_sense_file(vocFile='asdf', wsFile=''), 'file does not exist: asdf')
        self.assertEqual(create_word_sense_file(vocFile=TestFVoc, wsFile=TestFWS), 12)
        if create_word_sense_file(vocFile=TestFVoc, wsFile=TestFWS) == 12 and False:
            create_word_sense_file(vocFile=FileVoc, wsFile=FileWS)


if __name__ == "__main__":
    unittest.main()

