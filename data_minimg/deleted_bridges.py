import pandas as pd
import text_from_html_v_1_1 as tfh


# path = "repository_path"

symptoms = pd.read_csv(path + "symptom.csv", escapechar="\\")
diseases = pd.read_csv(path + "disease.csv", escapechar="\\")


deleted_symptoms = symptoms.where(symptoms['deleted']==1)

deleted_symptoms_names = deleted_symptoms['name'].to_numpy(na_value="")
deleted_symptoms_names = deleted_symptoms_names[deleted_symptoms_names !=""]

deleted_symptoms_ids = deleted_symptoms['id'].to_numpy(na_value=0, dtype=int)
deleted_symptoms_ids = deleted_symptoms_ids[deleted_symptoms_ids !=0]

diseases['description'] = tfh.convert_list_of_html_to_string(diseases['description'])
diseases['about'] = tfh.convert_list_of_html_to_string(diseases['about'])


deleted_symptom_disease_map = pd.DataFrame(columns=["deleted_symptom_id", "disease_id"])


for i in range(deleted_symptoms_names.size):
    curr_name = deleted_symptoms_names[i].lower()
    for j in range(diseases.shape[0]):
        curr_description = diseases.at[j, 'description']
        curr_about = diseases.at[j, 'about']
        index_d = curr_description.find(curr_name)
        index_a = curr_about.find(curr_name)
        if index_d !=-1 or index_a !=-1:
            curr_frame = pd.DataFrame(
                [[deleted_symptoms_ids[i], diseases.at[j, 'id']]], 
                columns=["deleted_symptom_id", "disease_id"])
           
            deleted_symptom_disease_map = deleted_symptom_disease_map.append(curr_frame, 
                ignore_index=True)

deleted_symptom_disease_map.to_csv(path_or_buf=path + "deleted_symptom_disease_map.csv", 
index=False)
