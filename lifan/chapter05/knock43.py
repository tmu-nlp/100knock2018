from knock41 import get_sentences

if __name__ == "__main__":
	sentences = get_sentences()
	for chunks in sentences:
		for idx, chunk in enumerate(chunks):
			if chunk.dst != -1 and chunk.morphs[0].pos != "記号":
				src_pos = chunk.morphs[-1].pos
				dst_pos = chunks[chunk.dst].morphs[-1].pos
				if (src_pos == "名詞" and dst_pos == "動詞") or (src_pos == "動詞" and dst_pos == "名詞"):
					print(f"{chunk.surface}\t{chunks[chunk.dst].surface}")