import xml.etree.ElementTree as ET
import pydot
from itertools import islice


def main(n=0):
    '''n文目の係り受け解析結果をグラフで表示する'''
    root = ET.parse('knock50.txt.xml')

    graph = pydot.Dot(graph_type='digraph')
    graph.set_node_defaults(fontname='Sans Not-Rotated 12')

    for sentence in islice(root.iterfind('./document/sentences/sentence'), n, n+1):
        for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
            if dep.get('type') == 'punct':
                continue
            governor = dep.find('./governor')
            dependent = dep.find('./dependent')
            gove_text = f"{governor.text}({governor.get('idx')})"
            depe_text = f"{dependent.text}({dependent.get('idx')})"
            graph.add_edge(pydot.Edge(gove_text, depe_text))

    # グラフ描画
    graph.write('graph.png', format='png', encoding='utf8')


if __name__ == '__main__':
    main(3)


''' 問
57. 係り受け解析

Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

''' 実行結果
略
'''
