from knock41 import load_cabocha_iter


def main():
    with open('out2.txt', 'w', encoding='utf8') as f:
        for chunks in load_cabocha_iter():
            case_patterns = {}
            # {id: [動詞の基本形, [(助詞, 文節), (助詞, 文節),...]]}
            for chunk in chunks:
                if chunk.dst == -1:
                    continue
                particles = [morph.surface for morph in chunk.morphs if morph.pos == '助詞']
                verbs = [morph.base for morph in chunks[chunk.dst].morphs if morph.pos == '動詞']
                if not particles or not verbs:
                    continue
                if chunk.dst not in case_patterns:
                    case_patterns[chunk.dst] = [verbs[0], [(particles[0], chunk.normalized_surface())]]
                else:
                    case_patterns[chunk.dst][1].append((particles[0], chunk.normalized_surface()))
            for value in case_patterns.values():
                frames = sorted(value[1])
                # print(f'{value[0]}\t{" ".join([frame[0] for frame in frames])}\t{" ".join([frame[1] for frame in frames])}')
                f.write(f'{value[0]}\t{" ".join([frame[0] for frame in frames])}\t{" ".join([frame[1] for frame in frames])}\n')


if __name__ == '__main__':
    main()


''' 問
46. 動詞の格フレーム情報の抽出

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．

* 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
* 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

```
始める  で      ここで
見る    は を   吾輩は ものを
```
'''

''' 実行結果
head out2.txt -n10

生れる  で      どこで
つく    か が   生れたか 見当が
泣く    で      所で
する    だけ て いた事だけは 泣いて
見る    は を   吾輩は ものを
始める  で      ここで
聞く    で      あとで
捕える  を      我々を
煮る    て      捕えて
食う    て      煮て
'''

