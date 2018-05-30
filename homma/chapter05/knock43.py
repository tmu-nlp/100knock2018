from knock41 import load_cabocha_iter


def main():
    cnt = 0
    for chunks in load_cabocha_iter():
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            if not '名詞' in (morph.pos for morph in chunk.morphs):
                continue
            if not '動詞' in (morph.pos for morph in chunks[chunk.dst].morphs):
                continue
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if not src or not dst:
                continue
            print(f'{src}\t{dst}')
            cnt += 1
            if cnt == 20:
                return


if __name__ == '__main__':
    main()


''' 問
43. 名詞を含む文節が動詞を含む文節に係るものを抽出

名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

''' 実行結果
どこで  生れたか
見当が  つかぬ
所で    泣いて
ニャーニャー    泣いて
いた事だけは    記憶している
吾輩は  見た
ここで  始めて
ものを  見た
あとで  聞くと
我々を  捕えて
掌に    載せられて
スーと  持ち上げられた
時      フワフワした
感じが  あったばかりである
上で    落ちついて
顔を    見たのが
ものの  見始であろう
ものだと        思った
感じが  残っている
今でも  残っている
'''

