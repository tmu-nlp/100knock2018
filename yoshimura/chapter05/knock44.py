import CaboCha
import pydot_ng as pydot
from knock41 import Chunk
from knock40 import Morph

# pylint: disable=E1101

def get_chunk_list():
    with open('sentence.cabocha','r') as sentence_file:
        result = []
        chunks = {} # Chunkオブジェクトのidx : Chunkオブジェクト
        for line in sentence_file:
            line = line.rstrip() #stripだと先頭の空白文字が消える

            # 係り受け情報の場合
            if line[0] == '*':

                idx = int(line.split(' ')[1]) # 文節番号 
                dst = int(line.split(' ')[2][:-1]) # 係り先の文節番号（係り先なし:-1) 

                # Chunkオブジェクトをchunksに追加
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先があって係り先のオブジェクトが存在しなければ作成してそのsrcsに文節番号を追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # 形態素情報の場合
            elif line != 'EOS' and line[:1] != '*':
                # lineの列をそれぞれリストに格納
                columm = line.split('\t')[1].split(',')
                columm.insert(0,line.split('\t')[0])
                
                # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                morpheme = {'surface': columm[0], 'base': columm[7], 'pos': columm[1], 'pos1': columm[2]}
                chunks[idx].morphs.append(Morph(**morpheme))

            # 文の終わりの場合
            elif line == 'EOS' and len(chunks) != 0:
                sentence = [chunks[i] for i in sorted(chunks.keys())] #keyでソートしてvalueを取り出す
                result.append(sentence[:]) #chunksで渡すと次の行でappendしたものが消えてしまう
                chunks.clear()

    return result

if __name__ == '__main__':

    sentence = input('文を入力してください : ')

    # Cabochaで入力文を解析して結果をファイルに保存
    with open('sentence.cabocha','w') as write_file:
        cabocha = CaboCha.Parser()
        write_file.write(cabocha.parse(sentence).toString(CaboCha.FORMAT_LATTICE))
    
    # 係り元と係り先の文節を取得
    edges = []
    for line in get_chunk_list():
        for chunk in line:
            if chunk.dst != -1:
                src = chunk.surface()
                dst = line[chunk.dst].surface()
                if src != '' and dst != '':
                    edges.append(((src, dst)))
    
    # グラフを描画
    graph = pydot.graph_from_edges(edges, directed=True)
    graph.write_png('result.png')


    # filter








