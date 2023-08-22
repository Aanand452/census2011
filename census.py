import numpy as np
import pandas as pd


def census():

    census_df = pd.read_csv("/Users/anandkumar/Downloads/data/census.csv")

    print(census_df)

    # Before Analyzing the data we should explore data

    # It shows number of rows and columns in the data frame
    print(census_df.shape)

    # it shows number of null values in the dataframe
    print(census_df.count())

    # it shows all the whole data frame
    print(census_df.value_counts())

    # how will you hide index from dataframe
    print(census_df.style.hide())

    # how can we set the caption/heading on the dataframe
    print(census_df.style.set_caption('census of india 2011'))

    # show me the record related with distritcs-NEWdELHI,lUCKNIW,jAIPUR

    print(census_df[census_df['District_name'].isin(
        ['New Delhi', 'Lucknow', 'Jaipur'])])

    # show me the total population

    print(census_df.groupby('State_name').Population.sum().sort_values(ascending=False))

    # show me the total population with differen religions
    print(census_df.groupby('State_name')[
          ['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains']].sum().sort_values(by='Christians'))

    # How many male workers were there in Maharashtra state?
    print(census_df[census_df.State_name ==
          'MAHARASHTRA']['Male_Workers'].sum())

    # How to set a index as column
    print(census_df.set_index('District_code'))

    # Add a sufix to the column names
    print(census_df.add_suffix("Anand"))

    # Add a prefix to the column names
    print(census_df.add_prefix("Anand"))


census()
