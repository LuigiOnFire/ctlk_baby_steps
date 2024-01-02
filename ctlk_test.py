from cltk.corpus.utils.importer import CorpusImporter
corpus_importer = CorpusImporter("latin")
print(corpus_importer.list_corpora)
corpus_importer.import_corpus("latin_models_cltk")
