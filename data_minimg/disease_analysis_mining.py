import pandas as pd
import text_from_html_v_1_1 as tfh
import numpy as np
import re

# path = "repository_path"

analysis_tags = {'копрограма':['копрограм', 'кала'], 
                 'анализ мочи': ['моч'],
                 'анализ крови': ['кров'], 
                 'анализ ликвора': ['ликвор']}


analysis_types = ['забор', 'анализ', 'диагностика']

diseases = pd.read_csv(path + "disease.csv", escapechar="\\")

disease_analysis_map = pd.DataFrame(columns=["disease_id", "analysis_name"])

diseases['description'] = tfh.convert_list_of_html_to_string(diseases['description'])
diseases['about'] = tfh.convert_list_of_html_to_string(diseases['about'])

for j in range(diseases.shape[0]):
    curr_description = diseases.at[j, 'description']
    
    curr_about = diseases.at[j, 'about']
    
    for key in analysis_tags.keys():
        for tag in analysis_tags.get(key):
            flag = False
            curr_frame = pd.DataFrame([[diseases.at[j, 'id'], tag]], columns=["disease_id", "analysis_name"])
            
            for a_type in analysis_types:
                pattern = re.compile(tag + ".{,10}" + a_type)
                
                if pattern.search(curr_description) or pattern.search(curr_about):
                    flag = True
                    break
                else:
                    pattern = re.compile(a_type + ".{,15}" + tag)
                    if pattern.search(curr_description) or pattern.search(curr_about):
                        flag = True
                        break

            if flag==True:
                disease_analysis_map = disease_analysis_map.append(curr_frame, ignore_index=True)
                break


for key in analysis_tags.keys():
    for tag in analysis_tags.get(key):
        disease_analysis_map['analysis_name'] = disease_analysis_map.where(
            disease_analysis_map['analysis_name'] != tag, key)['analysis_name']

disease_analysis_map.to_csv(path_or_buf=path + "disease_analysis_map.csv", 
index=False)
