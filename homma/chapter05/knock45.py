from knock41 import load_cabocha_iter


def main():
    with open('out.txt', 'w', encoding='utf8') as f:
        for chunks in load_cabocha_iter():
            case_patterns = {}
            # {id: [動詞の基本形, [助詞, 助詞,...]]}
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                particles = [morph.surface for morph in chunk.morphs if morph.pos == '助詞']
                verbs = [morph.base for morph in chunks[chunk.dst].morphs if morph.pos == '動詞']
                if not particles or not verbs:
                    continue
                if chunk.dst not in case_patterns:
                    case_patterns[chunk.dst] = [verbs[0], particles]
                else:
                    case_patterns[chunk.dst][1].extend(particles)
            for value in case_patterns.values():
                f.write(f'{value[0]}\t{" ".join(sorted(value[1]))}\n')


if __name__ == '__main__':
    main()


''' 問
45. 動詞の格パターンの抽出

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
ただし，出力は以下の仕様を満たすようにせよ．

* 動詞を含む文節において，最左の動詞の基本形を述語とする
* 述語に係る助詞を格とする
* 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

```
始める  で
見る    は を
```

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

* コーパス中で頻出する述語と格パターンの組み合わせ
* 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''

''' 実行結果
sort out.txt | uniq --count | sort --numeric-sort --reverse | head -n10
    565 云う    と
    438 する    を
    251 思う    と
    197 ある    が
    191 なる    に
    175 する    に
    174 見る    て
    126 する    と
    117 する    が
    105 する    に を

grep "^する\s" out.txt | sort | uniq --count | sort --numeric-sort --reverse | head -n10
    438 する    を
    175 する    に
    126 する    と
    117 する    が
    105 する    に を
     88 する    て を
     59 する    は
     58 する    て
     58 する    が を
     48 する    から

grep "^見る\s" out.txt | sort | uniq --count | sort --numeric-sort --reverse | head -n10
    174 見る    て
     94 見る    を
     21 見る    て て
     20 見る    から
     18 見る    て を
     14 見る    と
     12 見る    で
     11 見る    て は
     11 見る    から て
      8 見る    に

grep "^与える\s" out.txt | sort | uniq --count | sort --numeric-sort --reverse | head -n10
      3 与える  に を
      2 与える  て に は を
      1 与える  ば を
      1 与える  に に対して のみ は は も
      1 与える  て も を
      1 与える  て に を
      1 与える  て に に は を
      1 与える  だけ で に を
      1 与える  たり て に を
      1 与える  けれども に は を
'''

