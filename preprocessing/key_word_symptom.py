def get_symptom_from_message(key_word_dict,table):
    keys = list(key_word_dict.keys())
    for key in keys:
        if key in list(table['name']):
            return key
        else: return None