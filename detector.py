import pandas as pd
import re
import os.path

base = os.path.dirname(os.path.abspath(__file__))

df_male_names = pd.read_csv(f"{base}/data/male_names.csv", sep=";")
df_female_names = pd.read_csv(f"{base}/data/female_names.csv", sep=";")

df_names = pd.merge(df_male_names, df_female_names, on="name",
                    how="outer", suffixes=[".male", ".female"])

df_names["frequency.male"] = df_names["frequency.male"].fillna(0)
df_names["frequency.female"] = df_names["frequency.female"].fillna(0)

df_names["frequency"] = df_names.apply(
    lambda row: row["frequency.male"] + row["frequency.female"], axis=1)
df_names["length"] = df_names.apply(
    lambda row: len(row["name"]), axis=1)

df_names = df_names.sort_values(by=["length", "frequency"], ascending=False)

def get_gender(name):
    if type(name) == float:
        return None

    # We remove all strange characters
    # BUT we leave diacritics!
    name = re.sub(r"[^a-zà-üÀ-Ü]", "", name, flags=re.IGNORECASE)

    if len(name) == 0:
        return

    df_search_space = df_names.loc[df_names["length"] <= len(name)]

    for index, row in df_search_space.iterrows():
        tested_name = row["name"]

        name_detected = re.match(f"^{tested_name}", name, flags=re.IGNORECASE)

        if name_detected:
            return "male" if row["frequency.male"] > row["frequency.female"] else "female"
        
    return None