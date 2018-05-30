from knock41 import get_sentences

def output_path(path_words_x, path_words_y):
	path_x = sorted(set(path_words_x) - set(path_words_y), key=path_words_x.index)
	path_y = sorted(set(path_words_y) - set(path_words_x), key=path_words_y.index)
	path_z = sorted(set(path_words_x) & set(path_words_y), key=path_words_x.index)
	path_x[0] = "X"
	if len(path_y) == 0:
		path_z[0] = "Y"
		return f"{'->'.join(path_x)}->{path_z[0]}"
	else:
		path_y[0] = "Y"
		return f"{'->'.join(path_x)} | {'->'.join(path_y)} | {'->'.join(path_z)}"


if __name__ == "__main__":
	sentences = get_sentences()
	chunks = sentences[5]
	for ci, chunk in enumerate(chunks):
		# 名詞句Xをsearch
		if chunk.morphs[0].pos == "名詞":
			next_id_x = chunk.dst
			path_words_x = [chunk.surface]
			# 名詞句Xのパスを抽出
			while chunks[next_id_x].dst != -1:
				path_words_x.append(chunks[next_id_x].surface)
				next_id_x = chunks[next_id_x].dst
			else:
				path_words_x.append(chunks[next_id_x].surface)

			for nci, next_chunk in enumerate(chunks[ci+1:]):
				# 名詞句Yをsearch
				if next_chunk.morphs[0].pos == "名詞":
					path_words_y = [next_chunk.surface]
					next_id_y = next_chunk.dst
					# 名詞句Yのパスを抽出
					while chunks[next_id_y].dst != -1:
						path_words_y.append(chunks[next_id_y].surface)
						next_id_y = chunks[next_id_y].dst
					else:
						path_words_y.append(chunks[next_id_y].surface)
					print(output_path(path_words_x, path_words_y))
