from knock41 import load_cabocha_iter
from itertools import combinations


def obtain_direct_path(chunks, paths, i, j):
    '''
    名詞句ペア（文節番号がiとj）のパスを得る
    （文節iから構文木の根に至る経路上に文節jが存在する場合）
    '''
    path_str = chunks[i].xy_surface('X') + ' -> '
    for p in paths[i]:
        if p == j:
            path_str += 'Y' # 問題文の実行結果に合わせる
            break
        else:
            path_str += chunks[p].normalized_surface() + ' -> '
    return path_str


def obtain_indirect_path(chunks, paths, i, j):
    '''
    名詞句ペア（文節番号がiとj）のパスを得る
    （文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合）
    '''
    # 文節iから文節kの直前までのパス
    path_str = chunks[i].xy_surface('X')
    for p in paths[i]:
        if p not in paths[j]:
            path_str += ' -> ' + chunks[p].normalized_surface()
            continue
        # 文節kに到達，文節jから文節kの直前までのパス
        path_str += ' | ' + chunks[j].xy_surface('Y')
        for q in paths[j]:
            if p != q:
                path_str += ' -> ' + chunks[q].normalized_surface()
                continue
            # 文節kの内容
            path_str += ' | ' + chunks[p].normalized_surface()
            return path_str


def obtain_path_str(chunks, paths, i, j):
    '''
    名詞句ペア（文節番号がiとj）のパスの文字列を得る
    '''
    if j in paths[i]:
        return obtain_direct_path(chunks, paths, i, j)
    elif i in paths[j]:
        return obtain_direct_path(chunks, paths, j, i)
    else:
        return obtain_indirect_path(chunks, paths, i, j)


def main():
    for i, chunks in enumerate(load_cabocha_iter()):
        if i != 5:
            continue
        paths = {} # ex) {0: [5], 1: [2, 3, 4, 5], 3: [4, 5], 4: [5]}
        for j, chunk in enumerate(chunks):
            if chunk.dst == -1:
                continue
            noun = [morph.surface for morph in chunk.morphs if morph.pos == '名詞']
            if not noun:
                continue
            current = chunk
            paths[j] = []
            while current.dst != -1:
                paths[j].append(current.dst)
                current = chunks[current.dst]
        print(paths)
        for k, l in combinations(paths.keys(), 2):
            print(obtain_path_str(chunks, paths, k, l))


if __name__ == '__main__':
    main()


''' 問
49. 名詞間の係り受けパスの抽出

文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiとj（i<j）のとき，
係り受けパスは以下の仕様を満たすものとする．

* 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
  （表層形の形態素列）を"->"で連結して表現する
* 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する

また，係り受けパスの形状は，以下の2通りが考えられる．

* 文節iから構文木の根に至る経路上に文節jが存在する場合:
    文節iから文節jのパスを表示
* 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
    文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，
    文節kの内容を"|"で連結して表示

例えば，「吾輩はここで始めて人間というものを見た。」という文
（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

```
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
```
'''

''' 実行結果
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
'''
