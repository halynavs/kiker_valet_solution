import re
import numpy as np
from rutermextract import TermExtractor

def key_Word(text):


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

def remove_special_characters(text):
    text = re.sub(r'[^а-яА-ЯёЁ\s]', '', text, re.I | re.A)
    return text
from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()

def remove_repeated_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)')
    match_substitution = r'\1\2\3'

    def replace(old_word):
        if wikiwordnet.get_synsets(old_word):
            return old_word
        new_word = repeat_pattern.sub(match_substitution, old_word)
        return replace(new_word) if new_word != old_word else new_word

    correct_tokens = [replace(word) for word in tokens]
    text = ' '.join(correct_tokens)
    return text

def lemmatisaze_document(doc):

    nlp = StanzaLanguage(snlp)
    doc = nlp(doc)

    filtered_tokens = [token.lemma_ for token in doc]
    doc = ' '.join(filtered_tokens)
    return doc

def input_to_key_word(message):
    doc = message
    # remove extra newlines
    doc = doc.translate(doc.maketrans("\n\t\r", "   "))

    # remove extra whitespace
    doc = re.sub(' +', ' ', doc)
    doc = doc.strip()

    # remove punct, special characters\whitespaces
    doc = remove_special_characters(doc)

    # lowercase the text
    doc = doc.lower()

    # remove repeated characters
    tokens = tokenizer.tokenize(doc)
    doc = remove_repeated_characters(tokens)

    # lemmatize text
    lemmatisaze_corpus = np.vectorize(lemmatisaze_document)
    doc = lemmatisaze_corpus(doc)

    key_words_dict = key_Word(doc)

    return key_words_dict
