import MeCab
import sys

sentence=[]
kari={}
words=[]
"""
def morph_analysis(infile, outfile) : # infileの文章を解析して，結果をoutfileに出力
    t = MeCab.Tagger(' '.join(sys.argv)) # 形態素解析器の変数（オブジェクト）を作成
    fin = open(infile, 'r') # 解析対象のファイルを開く
    fout = open(outfile, 'w') # 解析結果を書き出すファイルを開く
    fout.write(t.parse(fin.read())) # 読み込んで解析して書き出し
    fin.close() # ファイルを閉じる
    fout.close()
    return outfile

morph_analysis('neko.txt', 'neko_m.txt')
"""
lines = open("neko_m.txt").readlines()
for line in lines:
  kari={}
  if "EOS" in line:
    break
  line= line.split("\t")
  line2=line[1].split(",")
  line.pop()
  line.extend(line2)
  if "。" in line[0]:
    sentence.append(words)
    words=[]
  kari["surface"]=line[0]
  kari["pos"]=line[1]
  kari["pos1"]=line[2]
  kari["base"]=line[7]
  words.append(kari)
for j in sentence:
    for i in j:
        print(i["surface"])
