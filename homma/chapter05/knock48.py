from knock41 import load_cabocha_iter


def main():
    for i, chunks in enumerate(load_cabocha_iter()):
        if i != 5:
            continue
        for chunk in chunks:
            if chunk.dst == -1:
                continue
            noun = [morph.surface for morph in chunk.morphs if morph.pos == '名詞']
            if not noun:
                continue
            path = chunk.normalized_surface() # 吾輩は
            current = chunk
            while current.dst != -1:
                current = chunks[current.dst]
                path += f' -> {current.normalized_surface()}' # 吾輩は -> 見た
            print(path)


if __name__ == '__main__':
    main()


''' 問
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． 
ただし，構文木上のパスは以下の仕様を満たすものとする．

* 各文節は（表層形の）形態素列で表現する
* パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

```
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
```
'''

''' 実行結果
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''

