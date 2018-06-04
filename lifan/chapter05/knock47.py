from knock41 import get_sentences

if __name__ == "__main__":
	sentences = get_sentences()

	for i,chunks in enumerate(sentences):
		is_ok = False
		for chunk in chunks:
			# 条件該当するか判定
			if chunk.morphs[0].pos == "動詞":
				verb_base = chunk.morphs[0].base
				for idx in chunk.srcs:
					for morph in chunks[idx].morphs:
						if chunks[idx].morphs[-1].surface == "を":
							if morph.pos1 == "サ変接続":
								main_verb = chunks[idx].surface + verb_base
								main_srcs = chunk.srcs
								is_ok = True

			# 該当のchunkを抽出
			if is_ok:
				particles = []
				full_particles = {}
				for main_idx in main_srcs:
					for main_morph in chunks[main_idx].morphs:
						if main_morph.pos == "助詞" and main_morph.surface != "を":
							particles.append(main_morph.base)
							full_particles[main_idx] = chunks[main_idx].surface
				print(f'{i}:{main_verb}\t{" ".join(particles)}\t{" ".join(full_particles.values())}')
				break