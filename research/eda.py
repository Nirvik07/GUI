from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('C:/Users/sumat/Downloads/crimes_against_women_2001-2014.csv')

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

# df['STATE/UT'].unique()


def helper1(all_cases):
    for i in list(df.columns)[2:]:
        all_cases[i] = df.groupby(['Year'])[i].sum()

    return all_cases


all_cases = pd.DataFrame()
all_cases = helper1(all_cases)
# all_cases


def helper1(state_data):
    for i in list(df.columns)[2:]:
        state_data[i] = df.groupby(['STATE/UT'])[i].sum()

    return state_data


state_data = pd.DataFrame()
state_data = helper1(state_data)


co_list = list(state_data)
state_data['Total'] = state_data[co_list].sum(axis=1)
all_crimes = state_data

# finding the mean of crimes
m = all_crimes['Total'].mean()

# finding the quantiles
q = np.quantile(all_crimes['Total'], [0.25, 0.75])

# copying the state_all_crmes to a new dataframe to normalise value and predict
df_kmeans = all_crimes.iloc[:, all_crimes.columns != "STATE/UT"]


output = []
for i in df_kmeans['Total']:
    if i >= m:
        output.append(1)  # unsafe
    elif m > i:
        output.append(0)  # safe


all_crimes['output'] = output
df_kmeans_y = all_crimes['output']

cols = df_kmeans.columns

ms = MinMaxScaler()
df_kmeans = ms.fit_transform(df_kmeans)
df_kmeans = pd.DataFrame(df_kmeans, columns=[cols])


kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(df_kmeans)

labels = kmeans.labels_

correct_labels = sum(df_kmeans_y == labels)

print('labels:', labels)
print('df_kmeans output:', df_kmeans_y)
print("Result: %d out of %d samples were correctly labeled." %
      (correct_labels, df_kmeans_y.size))


final = []
for i in range(len(labels)):
    state = all_crimes['output'][i]
    label = labels[i]
    if label == 1:
        final.append([state, 'unsafe'])

    else:
        final.append([state, 'safe'])


final_df = pd.DataFrame(final, columns=['STATE/UT', 'SAFE/UNSAFE'])


df_UP = df[df['STATE/UT'] == 'UTTAR PRADESH']
df_UP.drop(df.columns.difference(['Year', 'Dowry Deaths']), 1, inplace=True)
X = df_UP.groupby(['Year'], sort=True).sum()
df_UP = pd.DataFrame(X)
df_UP = df_UP.reset_index()

plt.plot(df_UP)
plt.show()