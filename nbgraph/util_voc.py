import os
import codecs
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nbgraph.util_vec import is_float


def check_file_exist(f):
    if not os.path.isfile(f):
        print('file does not exist:', f)
        return ' '.join(['file does not exist:', f])


def create_vocabulary(w2vFile='', vocFile='', encode="latin-1"):
    """
    :param w2vFile: input pre-trained word2vec file
    :param vocFile: output vocabulary file, one word a line
    :return: vocabulary size
    """
    check_file_exist(w2vFile)
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
    check_file_exist(vocFile)
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
    check_file_exist(vocFile)
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


def create_ws_struc_txts(wsFile='', vocFile='', hypernymsFile='', hyponymsFile='', pathsFile='', encoding="latin-1"):
    """
    :param wsFile:
    :param vocFile:
    :param hypernymsFile:
    :param hyponymsFile:
    :param pathsFile:
    :param encoding:
    :return:
    """
    check_file_exist(wsFile)
    check_file_exist(vocFile)
    hyperDic = defaultdict(list)
    hypoDic = defaultdict(list)
    hyperlst = []
    hypolst = []
    pathlst = []
    with codecs.open(wsFile, 'r', encoding) as fh:
        wsLst = fh.read().splitlines()
    with codecs.open(vocFile, 'r', encoding) as fh:
        vocLst = fh.read().splitlines()

    for ws in wsLst:
        pathLine = ws
        wsIns = wn.synset(ws)
        for synChain in wsIns.hypernym_paths():
            hyperNames = [hyper.name() for hyper in synChain if hyper.name().split(".")[0] in vocLst]
            pathLine += "#" + " ".join(hyperNames[:-1])

            for parent, child in zip(hyperNames[:-1], hyperNames[1:]):
                if child not in hypoDic[parent]:
                    hypoDic[parent].append(child)
                if parent not in hyperDic[child]:
                    hyperDic[child].append(parent)
        pathlst.append(pathLine)
    for key, values in hyperDic.items():
        hyperlst.append(' '.join([key]+values))
    for key, values in hypoDic.items():
        hypolst.append(' '.join([key]+values))

    open(pathsFile, 'w+')
    with codecs.open(pathsFile, 'a+', encoding=encoding) as ofh:
        ofh.write("\n".join(pathlst))

    open(hypernymsFile, 'w+')
    with codecs.open(hypernymsFile, 'a+', encoding=encoding) as ofh:
        ofh.write("\n".join(hyperlst))

    open(hyponymsFile, 'w+')
    with codecs.open(hyponymsFile, 'a+', encoding=encoding) as ofh:
        ofh.write("\n".join(hypolst))

    return 0
