from knock41 import get_sentences

if __name__ == "__main__":
	sentences = get_sentences()
	chunks = sentences[5]
	for idx, chunk in enumerate(chunks):
		if chunk.dst != -1 and chunk.morphs[0].pos != "記号":
			print(f"{chunk.surface}\t{chunks[chunk.dst].surface}")