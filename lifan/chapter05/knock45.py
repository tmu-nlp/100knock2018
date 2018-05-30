from knock41 import get_sentences

if __name__ == "__main__":
	sentences = get_sentences()
	chunks = sentences[5]
	for chunk in chunks:
		if chunk.morphs[0].pos == "動詞":
			verb_base = chunk.morphs[0].base
			particles = []
			for idx in chunk.srcs:
				for morph in chunks[idx].morphs:
					if morph.pos == "助詞":
						particles.append(morph.base)
			print(f'{verb_base}\t{" ".join(particles)}')