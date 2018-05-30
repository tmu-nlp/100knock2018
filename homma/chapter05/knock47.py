from knock41 import load_cabocha_iter


def main():
    with open('out3.txt', 'w', encoding='utf8') as f:
        for chunks in load_cabocha_iter():
            for i, chunk in enumerate(chunks):
                # 係り元のチェック
                if not chunk.srcs:
                    continue

                # 動詞の基本形
                verbs = [morph.base for morph in chunk.morphs if morph.pos == '動詞']
                if not verbs:
                    continue

                # 助詞を含む係り元の文節
                particle_phrases = [chunks[src] for src in chunk.srcs[i] if sum(1 for m in chunks[src].morphs if m.pos == '助詞')]
                if not particle_phrases:
                    continue

                # 「サ変接続名詞 ＋ を」 をチェックしてparticle_phrasesから除く
                # print([a.normalized_surface() for a in particle_phrases])
                predicate = ''
                for phrase in particle_phrases:
                    for i in range(len(phrase.morphs) - 1):
                        if phrase.morphs[i].pos1 == 'サ変接続' and phrase.morphs[i+1].surface == 'を':
                            predicate = f'{phrase.morphs[i].surface}を{verbs[0]}'
                            particle_phrases.remove(phrase)
                            break
                    else:
                        continue
                    break
                else:
                    continue

                # [(助詞, 文節), (助詞, 文節),...]
                particles_phrases = []
                for phrase in particle_phrases:
                    for morph in phrase.morphs:
                        if morph.pos == '助詞':
                            particles_phrases.append((morph.surface, phrase.normalized_surface()))
                            break

                pp = sorted(particles_phrases)
                f.write(f'{predicate}\t{" ".join([p[0] for p in pp])}\t{" ".join([p[1] for p in pp])}\n')


if __name__ == '__main__':
    main()


''' 問
47. 機能動詞構文のマイニング

動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

* 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
* 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
* 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
* 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

```
返事をする      と に は        及ばんさと 手紙に 主人は
```

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

* コーパス中で頻出する述語（サ変接続名詞+を+動詞）
* コーパス中で頻出する述語と助詞パターン
'''

''' 実行結果
cut out3.txt -f1 | sort | uniq --count | sort --numeric-sort --reverse | head -n10

     30 返事をする
     21 挨拶をする
     16 話をする
     14 真似をする
     13 喧嘩をする
      8 質問をする
      7 運動をする
      6 話を聞く
      6 注意をする
      6 昼寝をする

cut out3.txt -f1,2 | grep -E "^.*\s.+" | sort | uniq --count | sort --numeric-sort --reverse | head -n10

      4 返事をする      と
      4 挨拶をする      から
      3 返事をする      と は
      3 喧嘩をする      と
      3 挨拶をする      と
      2 返事をする      から と
      2 同情を表する    て と は
      2 質問をする      が
      2 質問をかける    と は
      2 講義をする      で
'''

