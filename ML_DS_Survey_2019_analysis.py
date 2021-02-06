# shorkeys
# alt+shift+e - run oneline of code
# ctrl + / - comment block of code


# Packages
import numpy as np
import pandas as pd

# low_memory=False

# Import data
survey_schema = pd.read_csv('C:/Users/marci/Desktop/GitHub/ML_DS_Survey_2019/survey_schema.csv', low_memory=False)
survey = pd.read_csv('C:/Users/marci/Desktop/GitHub/ML_DS_Survey_2019/multiple_choice_responses.csv', low_memory=False)
survey.shape
survey.info()
survey.describe()
survey.head(n=50)


import re

# mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
# print(mylist)
# r = re.compile(".*cat")
# newlist = list(filter(r.match, mylist)) # Read Note
# print(newlist)
#
# col = list(survey.columns)
# print(col)
# r = re.compile(".*TEXT.*")
# t = list(filter(r.match, col)) # Read Note
# print(t)
#
# df = pd.DataFrame(survey)
# new_df = df[df.columns.difference(t)]
# new_df.columns
#
# df = df[df.columns.difference(t)]
# df.columns

r = re.compile(".*TEXT.*")
col_TEXT = list(filter(r.match, col))
print(col_TEXT)
survey = survey[survey.columns.difference(col_TEXT)]
survey.columns

survey.drop(survey.index[0])