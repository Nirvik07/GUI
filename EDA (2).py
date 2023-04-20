from ast import increment_lineno
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

df = pd.read_csv('data/crimes_against_women_2001-2014.csv')

# removing the unnamed column
df.drop('Unnamed: 0', axis=1, inplace=True)

df.drop(['DISTRICT'], axis=1, inplace=True)


def case_consistency(row):
    row = row['STATE/UT'].strip()
    row = row.upper()
    return row


df['STATE/UT'] = df.apply(case_consistency, axis=1)

df['STATE/UT'].replace('A&N ISLANDS', 'A & N ISLANDS', inplace=True)
df['STATE/UT'].replace('D&N HAVELI', 'D & N HAVELI', inplace=True)
df['STATE/UT'].replace('DELHI UT', 'DELHI', inplace=True)

df['STATE/UT'].unique()


def up_graph():
    df_UP = df[df['STATE/UT'] == 'UTTAR PRADESH']
    df_UP.drop(df.columns.difference(
        ['Year', 'Dowry Deaths']), 1, inplace=True)
    X = df_UP.groupby(['Year'], sort=True).sum()
    df_UP = pd.DataFrame(X)
    df_UP = df_UP.reset_index()
    df_UP.index = df_UP.Year
    df_UP.drop("Year", axis=1, inplace=True)
    dict = df_UP.to_dict()
    return dict['Dowry Deaths']


# YEAR-WISE CRIME ANALYSIS
def helper1(all_cases):
    for i in list(df.columns)[2:]:
        all_cases[i] = df.groupby(['Year'])[i].sum()

    return all_cases


all_cases = pd.DataFrame()
all_cases = helper1(all_cases)


def bar_graph_allcases():
    df1 = pd.DataFrame(all_cases.sum(axis=1), columns=["Total no of crimes"])
    dict1 = df1.to_dict()
    return dict1['Total no of crimes']


def piechart_crime():
    df2 = pd.DataFrame(all_cases.sum(axis=0), columns=[
                       'Count']).sort_values(by='Count', ascending=False)
    dict2 = df2.to_dict()
    return dict2['Count']


def bar_graph_rape():
    df3 = all_cases['Rape']
    dict3 = df3.to_dict()
    return dict3


def bar_graph_Kidnapping_and_Abduction():
    df4 = all_cases['Kidnapping and Abduction']
    dict4 = df4.to_dict()
    return dict4
