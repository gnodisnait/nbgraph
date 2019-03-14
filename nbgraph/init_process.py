"""
nball4tree
"""
import decimal
from nbgraph.util_vec import vec_norm
from nbgraph.util_file import create_ball_file


def get_word2vector(wordsense, word2vecDic = dict()):
    """
    :param wordsense:
    :param word2vecDic:
    :return:
    """
    wd = wordsense.split('.')[0]
    if wd in word2vecDic:
        return word2vecDic[wd]
    elif wordsense.split('.')[0] in word2vecDic:
        return word2vecDic[wordsense.split('.')[0]]


def initialize_ball(root, addDim=[], L0=0.1, R0=0.1,
                    word2vecDic=dict(), wscatCodeDic=dict(), word2ballDic=dict(), outputPath=None):
    """
    :param root:
    :param addDim:
    :param L0:
    :param R0:
    :param word2vecDic:
    :param wscatCodeDic:
    :param word2ballDic:
    :param outputPath:
    :return:
    """
    w2v = [decimal.Decimal(ele*100) for ele in get_word2vector(root, word2vecDic=word2vecDic)]
    cpoint = w2v + [ele+10 for ele in wscatCodeDic[root]]+ addDim
    word2ballDic[root] = vec_norm(cpoint) + [L0, R0]
    if outputPath:
        create_ball_file(root,  outputPath=outputPath,word2ballDic=word2ballDic)
    return word2ballDic[root], word2ballDic