from knock41 import get_sentences
import pydot_ng as pydot

if __name__ == "__main__":
	sentences = get_sentences()
	chunks = sentences[5]
	edges = []
	for idx, chunk in enumerate(chunks):
		if chunk.dst != -1 and chunk.morphs[0].pos != "記号":
			src_surface = chunk.surface
			dst_surface = chunks[chunk.dst].surface
			edges.append((src_surface, dst_surface))

	g = pydot.graph_from_edges(edges)
	g.write_png('knock44.png', prog='dot')
