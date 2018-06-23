import xml.etree.ElementTree as ET
import pydot



def make_corenlp_tree(data_in_path, data_out_path, num_sentence):
    tree = ET.parse(data_in_path)
    root = tree.getroot()
    graph = pydot.Dot()
    graph.set_type('digraph')

    sentence = root.find(".//sentences/sentence[@id='{}']".format(num_sentence))
    for dep in sentence.find(".//dependencies[@type='collapsed-dependencies']"):
        from_edge = dep.find('governor').text + ' _ ' + dep.find('governor').get('idx')
        to_edge = dep.find('dependent').text + ' _ ' + dep.find('dependent').get('idx')
        graph.add_edge(pydot.Edge(from_edge, to_edge))
    graph.write_jpeg(data_out_path)


if __name__ == '__main__':
    data_in_path = '../data/knock50.txt.xml'
    data_out_path = './result/knock57.jpg'
    make_corenlp_tree(data_in_path, data_out_path, 4)
