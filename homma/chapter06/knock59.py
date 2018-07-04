import xml.etree.ElementTree as ET
import regex as re
from itertools import islice


def search_NP(s_sub, ptn, nps):
    '''1文中の名詞句をリストにして返す'''
    if s_sub.startswith('(NP '):
        nps.append(s_sub[4:-1])
    if '(NP ' in s_sub[1:-1]:
        return search_NP(ptn.search(s_sub[1:-1]).group(), ptn, nps)
    else:
        return nps


def print_NP(s_exp):
    '''S式からNPを表示する'''
    # 再帰的な()の正規表現パターン
    ptn = re.compile(r'(?<rec>\((?:[^()]+|(?&rec))*\))')
    for np in search_NP(ptn.search(s_exp).group(), ptn, []):
        print(np)


def main():
    root = ET.parse('knock50.txt.xml')
    
    for parse in root.iterfind('./document/sentences/sentence/parse'):
        s_exp = parse.text
        print_NP(s_exp)


if __name__ == '__main__':
    main()


''' 問
59. S式の解析

Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
'''

''' 実行結果
(JJ Natural) (NN language) (NN processing)
(NP (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))
(JJ Natural) (NN language) (NN processing)
(NP (JJ Many) (NNS challenges)) (PP (IN in) (NP (NN NLP)))
(JJ Many) (NNS challenges)
(NN History)
(NP (DT The) (NN history)) (PP (IN of) (NP (NNP NLP)))
(DT The) (NN history)
(NP (DT The) (NNP Georgetown) (NN experiment)) (PP (IN in) (NP (CD 1954)))
(DT The) (NNP Georgetown) (NN experiment)
(DT The) (NNS authors)
(NP (JJ Little) (JJ further) (NN research)) (PP (IN in) (NP (NN machine) (NN translation)))
(JJ Little) (JJ further) (NN research)
(NP (DT Some) (RB notably) (JJ successful) (NN NLP) (NNS systems)) (VP (VBN developed) (PP (IN in) (NP (DT the) (NNS 1960s))))
(DT Some) (RB notably) (JJ successful) (NN NLP) (NNS systems)
(NNS Examples)
(DT This)
(NP (DT Some)) (PP (IN of) (NP (NP (DT the) (JJ earliest-used) (NN machine)) (VP (VBG learning) (NP (NP (NNS algorithms)) (, ,) (PP (JJ such) (IN as) (NP (NN decision) (NNS trees))) (, ,)))))
(DT Some)
(NP (DT The) (NN cache) (NN language) (NNS models)) (PP (IN upon) (SBAR (WHNP (WDT which)) (S (NP (JJ many) (NN speech) (NN recognition) (NNS systems)) (ADVP (RB now)) (VP (VBP rely)))))
(DT The) (NN cache) (NN language) (NNS models)
(JJ Such) (NNS models)
(NP (JJ Many)) (PP (IN of) (NP (DT the) (JJ notable) (JJ early) (NNS successes)))
(JJ Many)
(DT These) (NNS systems)
(JJ Recent) (NN research)
(JJ Such) (NNS algorithms)
(NN NLP)
(NNP Modern) (NNP NLP) (NNS algorithms)
(NP (DT The) (NN paradigm)) (PP (IN of) (NP (NN machine) (NN learning)))
(DT The) (NN paradigm)
(DT The) (JJ machine-learning) (NN paradigm)
(NP (DT A) (NN corpus)) (PRN (-LRB- -LRB-) (NP (NP (NN plural)) (, ,) (NP (`` ``) (NN corpora) ('' ''))) (-RRB- -RRB-))
(DT A) (NN corpus)
(NP (JJ Many) (JJ different) (NNS classes)) (PP (IN of) (NP (NN machine) (NN learning) (NNS algorithms)))
(JJ Many) (JJ different) (NNS classes)
(DT These) (NNS algorithms)
(NP (DT Some)) (PP (IN of) (NP (DT the) (JJ earliest-used) (NNS algorithms))) (, ,) (PP (JJ such) (IN as) (NP (NN decision) (NNS trees))) (, ,)
(DT Some)
(JJ Such) (NNS models)
(NP (NNPS Systems)) (PP (VBN based) (PP (IN on) (NP (JJ machine-learning) (NNS algorithms))))
(NNPS Systems)
(NP (DT The) (NN learning) (NNS procedures)) (VP (VBN used) (PP (IN during) (NP (NN machine) (NN learning))))
(DT The) (NN learning) (NNS procedures)
(NP (NNP Automatic)) (VP (VBG learning) (NP (NNS procedures)))
(NNP Automatic)
(NP (NNPS Systems)) (VP (VBN based) (PP (IN on) (S (ADVP (RB automatically)) (VP (VBG learning) (NP (DT the) (NNS rules))))))
(NNPS Systems)
(NP (DT The) (NN subfield)) (PP (IN of) (NP (NP (NNP NLP)) (VP (VBN devoted) (PP (IN to) (S (VP (VBG learning) (SBAR (S (S (NP (NNS approaches)) (VP (VBZ is) (VP (VBN known) (PP (IN as) (NP (NP (JJ Natural) (NN Language) (NNP Learning)) (PRN (-LRB- -LRB-) (NP (NNP NLL)) (-RRB- -RRB-))))))) (CC and) (S (NP (PRP$ its) (NN conference) (NN CoNLL) (CC and) (NN peak) (NN body)) (NP (NNP SIGNLL)))))))))))
(DT The) (NN subfield)
'''
