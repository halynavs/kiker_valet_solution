from rutermextract import TermExtractor
def key_Word(corpus):
    for text in corpus:

     key_words = {}
     keys = []
     values = []
     term_extractor = TermExtractor()
     for term in term_extractor(text):
      keys.append(term.normalized)
      values.append(term.count)


      for i in keys:
       for x in values:
        key_words[i] = x

     return key_words
