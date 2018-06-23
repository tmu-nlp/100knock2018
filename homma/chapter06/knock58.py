import xml.etree.ElementTree as ET
from itertools import islice


def main():
    '''n文目までを 主語 述語 目的語 の組をタブ区切り形式で出力する'''
    root = ET.parse('knock50.txt.xml')

    for sentence in root.iterfind('./document/sentences/sentence'):
        for nsubj in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep[@type="nsubj"]'):
            for dobj in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep[@type="dobj"]'):
                if nsubj.find('governor').get('idx') != dobj.find('governor').get('idx'):
                    continue
                s = nsubj.find('dependent').text
                v = nsubj.find('governor').text
                o = dobj.find('dependent').text
                print(s, v, o, sep='\t')


if __name__ == '__main__':
    main()


''' 問
58. タプルの抽出

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．

* 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
* 主語: 述語からnsubj関係にある子（dependent）
* 目的語: 述語からdobj関係にある子（dependent）
'''

''' 実行結果
understanding   enabling        computers
others  involve generation
Turing  published       article
experiment      involved        translation
ELIZA   provided        interaction
patient exceeded        base
ELIZA   provide response
which   structured      information
underpinnings   discouraged     sort
that    underlies       approach
Some    produced        systems
which   make    decisions
systems rely    which
that    contains        errors
implementations involved        coding
algorithms      take    set
Some    produced        systems
which   make    decisions
models  have    advantage
they    express certainty
Systems have    advantages
Automatic       make    use
that    make    decisions
'''
