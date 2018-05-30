def dependency_chain(chunks, start):
    chain = []
    dst = start
    while dst > -1:
        chain.append(dst)
        dst = chunks[dst].dst
    return chain

def chain_phrase(chunks, chain, decorator=None):
    return ' -> '.join(map(lambda id: chunks[id].phrase(remove_symbol=True, decorator=decorator), chain))

if __name__ == '__main__':
    import os,sys
    sys.path.append(os.pardir)

    from chapter05.knock41 import get_neko_chunks

    chunks = get_neko_chunks(7)

    for i, chunk_i in enumerate(chunks):
        noun_i = chunk_i.morph('名詞')
        if noun_i is None:
            continue
        
        for j, chunk_j in enumerate(chunks[(i+1):], i+1):
            noun_j = chunk_j.morph('名詞')
            if noun_j is None:
                continue

            chain_i = dependency_chain(chunks, chunk_i.id)
            chain_j = dependency_chain(chunks, chunk_j.id)


            if set(chain_i) & set(chain_j) == set(chain_j):
                # Morph.surfaceの戻り値を変えるためのデコレーター
                # chunk_j は、Y に該当するものだけ出力する
                # 名詞句から名詞句のチェーンなので、Yを含む文節のうち、名詞句までを出力するため
                decorator = lambda m: \
                    'X' if m == noun_i else (\
                    'Y' if m == noun_j else (\
                    '' if m in chunk_j.morphs else\
                    m.surface))
                
                # 文節jは文節iから構文木の根に至るまでの経路上にある
                chain = chain_i[:len(chain_i) - len(chain_j) + 1]
                print(chain_phrase(chunks, chain, decorator))
            else:
                # 文節iと文節jは構文木の根に至る経路上で共通の文節kで交わる
                shared_chain = list(set(chain_i) & set(chain_j))
                chain_i_ind = chain_i[:-len(shared_chain)]
                chain_j_ind = chain_j[:-len(shared_chain)]

                # Morph.surfaceの戻り値を変えるためのデコレーター
                decorator = lambda m: 'X' if m == noun_i else ('Y' if m == noun_j else m.surface)

                parts = [chain_i_ind, chain_j_ind, shared_chain[:1]]
                phrase_parts = map(lambda chain: chain_phrase(chunks,chain,decorator), parts)

                print(' | '.join(phrase_parts))

'''
* 0 5D 0/1 -1.514009
吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ

* 1 2D 0/1 1.311423
ここ	名詞,代名詞,一般,*,*,*,ここ,ココ,ココ
で	助詞,格助詞,一般,*,*,*,で,デ,デ

* 2 3D 0/1 0.123057
始め	動詞,自立,*,*,一段,連用形,始める,ハジメ,ハジメ
て	助詞,接続助詞,*,*,*,*,て,テ,テ

* 3 4D 0/1 1.440044
人間	名詞,一般,*,*,*,*,人間,ニンゲン,ニンゲン
という	助詞,格助詞,連語,*,*,*,という,トイウ,トユウ

* 4 5D 0/1 -1.514009
もの	名詞,非自立,一般,*,*,*,もの,モノ,モノ
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ

* 5 -1D 0/1 0.000000
見	動詞,自立,*,*,一段,連用形,見る,ミ,ミ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。	記号,句点,*,*,*,*,。,。,。

EOS
'''