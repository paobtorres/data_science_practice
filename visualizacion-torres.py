import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.ticker as mtick

# from google.colab import drive

# Montamos Google Drive
# drive.mount('/content/drive')

df = pd.read_csv ('datasets/children_anemia.csv')

# Hemoglobin = Hgb

df = df.rename( columns= {"Age in 5-year groups": "age_group", 
                        "Type of place of residence": "type_of_residence",
                        "Highest educational level": "education_level",
                        "Wealth index combined": "wealth_index_combined",
                        "Births in last five years": "births_last_five_years" ,
                        "Age of respondent at 1st birth": "age_at_1st_birth",
                        "Hemoglobin level adjusted for altitude and smoking (g/dl - 1 decimal)": "Hgb_level_adj_altitude_smoking",
                        "Anemia level": "anemia_level",
                        "Have mosquito bed net for sleeping (from household questionnaire)": "mosquito_bed_net",
                        "Smokes cigarettes": "smokes_cigarettes" ,
                        "Current marital status": "marital_status",
                        "Currently residing with husband/partner": "residing_with" ,
                        "When child put to breast": "when_child_put_to_breast",
                        "Had fever in last two weeks": "fever_in_last_2weeks",
                        "Hemoglobin level adjusted for altitude (g/dl - 1 decimal)": "Hgb_level_adj_altitude" ,
                        "Anemia level.1": "anemia_level1",
                        "Taking iron pills, sprinkles or syrup": "taking_medication"                                    })

# print (df.info())
# print (df.describe())

# age_groups_list = df['age_group'].drop_duplicates().to_list()


## Histogram 

df_age_group = df['age_group'].sort_values()

num_bins = round(1 + np.log2(len(df_age_group)))

plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(12, 4))

ax.hist(df_age_group, bins=num_bins, edgecolor='White')

ax.set_xlabel('Age group')
ax.set_ylabel('Frequency')

ax.set_title('Histogram of Child\'s mother Age in group of 5 years')


### Pie 

df_residence = df['type_of_residence'].value_counts()

fig, ax = plt.subplots(figsize=(12, 4))

ax.pie(df_residence, labels = df_residence.index, autopct='%1.1f%%')

# Agrego un título
ax.set_title('Type of residence')




### Bar 

df_education = df['education_level'].value_counts().sort_values()

fig, ax = plt.subplots(figsize=(12, 4))

x = df_education.index
y = df_education.values
ax.bar(x.astype(str),y)

ax.set_title('Highest Education level')
ax.set_xlabel('Education level')
ax.set_ylabel('Quantity')



### SEABORN 

sns.set_theme(style="whitegrid")
sns.set_color_codes("pastel")

#Hist 

fig, ax = plt.subplots(figsize=(12, 4))
sns.histplot(data=df, x='age_group',hue='type_of_residence')
plt.title('Age group and type of residence')



# Bar Plot

anemia_level = df['anemia_level'].value_counts(normalize=True).mul(100).round(1)

anemia_level= anemia_level.to_frame()

anemia_level.index.name = 'level'

print (anemia_level)

fig, ax = plt.subplots(figsize=(12, 4))
sns.barplot(data=anemia_level, x ="level", y="anemia_level",label='' )

plt.title('Anemia level')
ax.yaxis.set_major_formatter(mtick.PercentFormatter())
ax.set_ylabel('% over total amount of childrens')
ax.set_xlabel('')



# Hist


fig, ax = plt.subplots(figsize=(12, 4))
sns.histplot(data=df, x='anemia_level',hue='taking_medication')
plt.title('Frequency')

plt.show()

