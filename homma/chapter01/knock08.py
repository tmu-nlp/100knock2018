def cipher(s):
    return ''.join([chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s])

plain = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
encrypted = cipher(plain)
decrypted = cipher(encrypted)

print(plain)
print(encrypted)
print(decrypted)

# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# - 英小文字ならば(219 - 文字コード)の文字に置換
# - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# 実行結果
# Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might
# Also Sign Peace Security Clause. Arthur King Can.
# Hr Hv Lrvw Bvxzfhv Blilm Clfow Nlg Ocrwrav Foflirmv. Nvd Nzgrlmh Mrtsg Aohl Srtm Pvzxv Svxfirgb Cozfhv. Aigsfi Krmt Czm.
# Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.
