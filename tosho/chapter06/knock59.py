# reference: http://pyparsing.wikispaces.com/file/view/sexpParser.py

if __name__ == '__main__':
    import sys, os
    sys.path.append(os.pardir)
    import regex as re
    from common.morph import SNode
    from common.parsers import load_corenlp_sentiment
    from pyparsing import Word, alphanums, Suppress, ZeroOrMore, Forward, Group

    #TODO: 今回はこれで良いが、実際は () 以外のシンボルはすべて入れたほうがよい
    #      ただし、`全`シンボルが自明でない。
    alphaword = Word(alphanums + '.,-\'`$?:')
    
    exp = Forward()
    LPAR, RPAR = map(Suppress, "()")
    exp << (alphaword | Group(LPAR + ZeroOrMore(exp) + RPAR))


    for s_id, s_exp in load_corenlp_sentiment('./nlp.txt.xml'):
        print(f'{s_id}: {s_exp}')

        result = exp.parseString(s_exp)[0]
        root = SNode(result)

        nodes = root.findall('NP')
        for node in nodes:
            print(node.phrase())

        print('-'*20)
        print(f'{len(nodes)} items')
        

