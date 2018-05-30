from knock41 import get_sentences

if __name__ == "__main__":
	sentences = get_sentences()
	chunks = sentences[5]
	for chunk in chunks:
		if chunk.morphs[0].pos == "名詞":
			next_idx = chunk.dst
			path_words = [chunk.surface]
			while chunks[next_idx].dst != -1:
				path_words.append(chunks[next_idx].surface)
				next_idx = chunks[next_idx].dst
			else:
				path_words.append(chunks[next_idx].surface)
			print(" -> ".join(path_words))