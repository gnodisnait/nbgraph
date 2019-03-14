import os
import codecs
from nltk.corpus import wordnet as wn
from nbgraph.util_vec import is_float


def create_vocabulary(w2vFile='', vocFile='', encode="latin-1"):
    """
    :param w2vFile: input pre-trained word2vec file
    :param vocFile: output vocabulary file, one word a line
    :return: vocabulary size
    """
    if not os.path.isfile(w2vFile):
        print('file does not exist:', w2vFile)
        return ' '.join(['file does not exist:', w2vFile])
    with codecs.open(w2vFile, 'r', encode) as w2v:
        wlst = []
        for line in w2v.readlines():
            if len(line.strip().split())>1:
                word, *lst = line.strip().split()
                if word.isalnum() and all(is_float(ele) for ele in lst) and len(lst) > 1:
                    print(line)
                    wlst.append(line.strip().split()[0])
    with codecs.open(vocFile, 'w+', encode) as fh:
        fh.write("\n".join(wlst))
    return len(wlst)


def get_voc_list(vocFile, encode="latin-1"):
    """
    :param vocFile: output vocabulary file, one word a line
    :return: voc list
    """
    if not os.path.isfile(vocFile):
        print('file does not exist:', vocFile)
        return ' '.join(['file does not exist:',vocFile])
    with codecs.open(vocFile, 'r', encode) as w2v:
        wlst = []
        for line in w2v.readlines():
            print(line)
            wlst.append(line.strip().split()[0])
    return wlst


def create_word_sense_file(vocFile='', wsFile='', encode="latin-1"):
    """
    :param vocFile:
    :param wsFile:
    :return:
    """
    if not os.path.isfile(vocFile):
        print('file does not exist:', vocFile)
        return ' '.join(['file does not exist:',vocFile])
    wslst = []
    with codecs.open(vocFile, 'r', encode) as w2v:
        for line in w2v.readlines():
            word = line.strip().split()[0]
            for syns in wn.synsets(word):
                if syns.name() not in wslst:
                    wslst.append(syns.name())
    with codecs.open(wsFile, 'w+', encode) as ofh:
        ofh.write("\n".join(wslst))
    return len(wslst)