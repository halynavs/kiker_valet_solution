import pandas as pd
import text_from_html_v_1_1 as tfh
import numpy as np
import re
import tabula

path = "/home/alexander/Документи/Visual Studio Code/Python Proj/Doc_ua_hackathon/Doc.ua/"

def read_first_page(source_path):
    return tabula.read_pdf(source_path, pages=1, lattice=True)[2].iloc[:-2]


# def read_pdf_write_csv(path, name, pages_number, columns, skip_first, skip_page_end):


blood_pages = tabula.read_pdf(path + 'blood.pdf', pages='all', lattice=True)[2:]
blood = pd.DataFrame(columns = ['Метод', 'Образец', 'Условные\rединицы', 'Единицы\rСИ'])
blood = pd.concat([pd.DataFrame(blood_pages[i], columns=blood.columns) for i in range(len(blood_pages))], ignore_index=True)
blood = blood.dropna()


def remove_carnage(source):
    for column in source.columns:
        for row in source.index:
            source.at[row, column] = source.at[row, column].replace("\r", " ")


remove_carnage(blood)

# blood.to_csv(path_or_buf=path + "blood.csv", index=False)


likvor = read_first_page(path + "likvor.pdf")
remove_carnage(likvor)

# likvor.to_csv(path_or_buf=path + "likvor.csv", index=False)

piss_pages = tabula.read_pdf(path + 'piss.pdf', pages='all', lattice=True)[2:]
piss = pd.DataFrame(columns = ['Метод', 'Образец', 'Условные\rединицы', 'Единицы\rСИ'])
piss = pd.concat([pd.DataFrame(piss_pages[i], columns=piss.columns) for i in range(len(piss_pages))], ignore_index=True)
piss = piss.dropna()

remove_carnage(piss)
# piss.to_csv(path_or_buf=path + "piss.csv", index=False)

poop = read_first_page(path + "poop.pdf")
remove_carnage(poop)
# poop.to_csv(path_or_buf=path + "poop.csv", index=False)


reg_ex_min_max = "[0-9]+\,?[0-9]*-[0-9]+\,?[0-9]*"
reg_ex_simple = "[0-9]+\,?[0-9]*"


def build_min_max(source, column_name):
    min_max_df = pd.DataFrame(columns=['min ' + column_name, 'max ' + column_name])
    for row in source.index:
        pattern = re.compile(reg_ex_min_max)
        found = pattern.search(source.at[row, column_name])
        if found:
            min_val, max_val = found.group().split('-')
            min_max_df.at[row, 'min ' + column_name] = min_val
            min_max_df.at[row, 'max ' + column_name] = max_val
        else:
            pattern = re.compile(reg_ex_simple)
            found = pattern.search(source.at[row, column_name])
            if found:
                min_max_df.at[row, 'min ' + column_name] = found.group()
                min_max_df.at[row, 'max ' + column_name] = found.group()
            else:
                min_max_df.at[row, 'min ' + column_name] = 0.0
                min_max_df.at[row, 'max ' + column_name] = 0.0
    return min_max_df


def build_extended_data(source):
    source_u_f = build_min_max(source, 'Условные\rединицы')
    source_ci_f = build_min_max(source, 'Единицы\rСИ')
    return source.join([source_u_f, source_ci_f])


def build_extended_data_(source):
    source_u_f = build_min_max(source, 'Условные единицы')
    source_ci_f = build_min_max(source, 'Единицы СИ')
    return source.join([source_u_f, source_ci_f])


blood_extended = build_extended_data(blood)
piss_extended = build_extended_data(piss)
poop_extended = build_extended_data_(poop)
likvor_extended = build_extended_data_(likvor)

blood_extended.to_csv(path_or_buf=path + "blood_extended.csv", index=False)
piss_extended.to_csv(path_or_buf=path + "piss_extended.csv", index=False)
poop_extended.to_csv(path_or_buf=path + "poop_extended.csv", index=False)
likvor_extended.to_csv(path_or_buf=path + "likvor_extended.csv", index=False)


