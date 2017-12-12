import pandas as pd

# go to https://labrosa.ee.columbia.edu/millionsong/faq
# click on field list
# copy table

full_field_list = pd.read_clipboard()
full_field_list.to_csv('../data/full_field_list.csv')
