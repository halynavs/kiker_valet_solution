import pandas as pd
import numpy as np
import re
hackathon_order = pd.read_csv('C:/Users/user/Jupyter/Hakaton/hackathon_order_fix2.csv', escapechar = '\\')
#print(hackathon_order['comment'])

from wiki_ru_wordnet import WikiWordnet
wikiwordnet = WikiWordnet()

from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()


from spacy_stanza import StanzaLanguage
import stanza

stanza.download('ru')
stanza_nlp = stanza.Pipeline('ru')
snlp = stanza.Pipeline(lang="ru")
nlp = StanzaLanguage(snlp)

def remove_special_characters(text):
    text = re.sub(r'[^а-яА-ЯёЁ\s]', '', text, re.I | re.A)
    return text


def lemmatisaze_document(doc):

    nlp = StanzaLanguage(snlp)
    doc = nlp(doc)

    filtered_tokens = [token.lemma_ for token in doc]
    doc = ' '.join(filtered_tokens)
    return doc



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

def normalize_corpus(corpus,text_lemmatization=True, special_char_removal=True, text_lower_case=True, repeated_characters_remover=True):

    normalized_corpus = []
    list_of_emoji = []
    timecode_list = []
    timecodes = []
    emoji = []
    for doc in corpus:
        # remove extra newlines
        doc = doc.translate(doc.maketrans("\n\t\r", "   "))

        # remove extra whitespace
        doc = re.sub(' +', ' ', doc)
        doc = doc.strip()


        # remove punct, special characters\whitespaces
        if special_char_removal:
            doc = remove_special_characters(doc)

        # lowercase the text
        if text_lower_case:
            doc = doc.lower()

        # remove repeated characters
        if repeated_characters_remover:
            tokens = tokenizer.tokenize(doc)
            doc = remove_repeated_characters(tokens)

        # lemmatize text
        if text_lemmatization:
            lemmatisaze_corpus = np.vectorize(lemmatisaze_document)
            doc = lemmatisaze_corpus(doc)

        normalized_corpus.append(doc)
    return normalized_corpus

norm_corpus= normalize_corpus(corpus=hackathon_order['comment'])
hackathon_order['Clean_Comment'] = norm_corpus

#print(hackathon_order['Clean_Comment'])
out_path = r'C:\Users\user\Jupyter\Hakaton\hackathon_order_fix_processed.csv'
hackathon_order.to_csv(out_path, index = False, header = True)

#
# body_symptom_disease = pd.read_csv('C:/Users/user/Jupyter/Hakaton/body_symptom_disease.csv')
#
#
#
# norm_corpus2 = normalize_corpus(corpus=body_symptom_disease['name_symptom'])
# body_symptom_disease['clean_symptom'] = norm_corpus2
# print(body_symptom_disease['clean_symptom'] )
#
# out_path = r'C:\Users\user\Jupyter\Hakaton\body_symptom_disease_processed.csv'
# body_symptom_disease.to_csv(out_path, index = False, header = True)