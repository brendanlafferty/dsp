# Q1: import numpy and pandas
import numpy as np
import pandas as pd

# Q2: Set options in pandas so it displays 30 `max_rows`
#                                 no limit on `max_columns`
#                                 precision is 3
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 25)
pd.set_option('display.precision', 3)


# Q3: assign the versions of pandas and numpy to variables below
pd_version = pd.__version__
np_version = np.__version__

# Q4: Read in the csv file "olive.csv" with pandas.
#     The filename is stored in the variable `olive_path`
#     Assign it to variable `df`
df = pd.read_csv('./data/olive.csv')

# The fields are:

# Unnamed: 0
# region
# area
# palmitic
# palmitoleic
# stearic
# oleic
# linoleic
# linolenic
# arachidic
# eicosenoic



# Q5: How many rows and columns are there in `df`? Put your answer in a variable `df_shape`.
df_shape = df.shape

# Q6: assign the first 2 rows of `df` to `df_first_two`
df_first_two = df.head(2)

# Q7: How many distinct data types are there in `df`?
df_data_types_count = len(df.dtypes.unique())   # this should be an integer

# Q8: In `df`, create a new column 'sub_region_raw', which will be a copy of the column 'Unnamed: 0'
df['sub_region_raw'] = df['Unnamed: 0'].copy()

# Q9: In `df`, rename 'Unnamed: 0' to 'sub_region_desc'
df.rename(columns={'Unnamed: 0': 'sub_region_desc'}, inplace=True)

# Q10: In `df`, rename the column 'area' to: 'sub_region'
df.rename(columns={'area': 'sub_region'}, inplace=True)

# Q11: In `df`, get the unique values of the field 'region'
region_unique = df['region'].unique()

# Q12: In `df`, how many unique values of the field 'sub_region' are there?
sub_region_unique_count = len(df['sub_region'].unique())  # should be an integer

# Q13: Lets take a look at the field `sub_region_desc`:

# >>> df['sub_region_desc'].head(5)
# 0    1.North-Apulia
# 1    2.North-Apulia
# 2    3.North-Apulia
# 3    4.North-Apulia
# 4    5.North-Apulia

# Looks like 'sub_region_desc' has line numbers attached to the beginning of region name. Remove those and get the unique values in that field, assign it to `srd_unique`
srd_unique = [desc.split('.')[1] for desc in df['sub_region_desc']]

action = sys.stdin.readline().strip()
if not action.startswith('_q'):
    var = globals()[action]
    print(var)

elif action == '_q1':
    assert (any('numpy' in str(val) for k, val in globals().items())), 'numpy is not imported'
    assert (any('pandas' in str(val) for k, val in globals().items())), 'pandas is not imported'

elif action == '_q2':
    assert pd.options.display.max_rows == 30, 'max rows is not set to 30'
    assert pd.options.display.max_columns is None, 'max columns is not set to None'
    assert pd.options.display.precision == 3, 'precision is not set to 3'

elif action == '_q3':
    import pandas as pd
    import numpy as np

    ans = pd.__version__
    assert ans == pd_version, 'pandas version different?'
    ans = np.__version__
    assert ans == np_version, 'numpy version different?'

elif action == '_q4':
    assert len(df) == 572
    pass
    # FIXME: these checks does not work bc df is altered
    # ans = (572, 11)
    # assert ans == df.shape
    # ans = {'Unnamed: 0', 'arachidic', 'area', 'eicosenoic', 'linoleic', 'linolenic', 'oleic', 'palmitic', 'palmitoleic', 'region', 'stearic'}
    # assert ans == set(df.columns)

elif action == '_q5':
    ans = (572, 11)
    assert ans == df_shape

elif action == '_q6':
    ans = {'Unnamed: 0', 'arachidic', 'area', 'eicosenoic', 'linoleic', 'linolenic', 'oleic', 'palmitic', 'palmitoleic',
           'region', 'stearic'}
    assert set(df_first_two.columns) == ans
    assert list(df_first_two.index) == [0, 1]

elif action == '_q7':
    ans = len(df.dtypes.unique())
    assert df_data_types_count == ans

elif action == '_q8':
    ans = [i.split(',')[0] for i in olive.split('\n')[1:]]
    assert all(i == j for i, j in zip(ans, df['sub_region_raw'].map(str).values))

elif action == '_q9':
    assert 'Unnamed: 0' not in df.columns, '"Unnamed: 0" is still in the dataframe'

elif action == '_q10':
    assert 'area' not in df.columns, '"area" still in df'
    ans = [i.split(',')[2] for i in olive.split('\n')[1:]]
    assert all(i == j for i, j in zip(ans, df.sub_region.map(str)))

elif action == '_q11':
    ans = {1, 2, 3}
    assert set(region_unique) == ans

elif action == '_q12':
    ans = 9
    assert sub_region_unique_count == ans

elif action == '_q13':
    ans = {'Calabria', 'Coast-Sardinia', 'East-Liguria', 'Inland-Sardinia', 'North-Apulia', 'Sicily', 'South-Apulia',
           'Umbria', 'West-Liguria'}
    assert set(srd_unique) == ans

print(1)

# ---------------------- SOLUTIONS BELOW ------------
# ---------------------- SOLUTIONS BELOW ------------
# ---------------------- SOLUTIONS BELOW ------------
# ---------------------- SOLUTIONS BELOW ------------
# ---------------------- SOLUTIONS BELOW ------------

# WARNING: If you close your browser, your work will be LOST!
#
# # Q1: import numpy and pandas
# import pandas as pd
# import numpy as np
#
# # Q2: Set options in pandas so it displays 10 `max_rows`
# #                                 no limit on `max_columns`
# #                                 precision is 3
# pd.options.display.max_rows = 30
# pd.options.display.max_columns = None
# pd.options.display.precision = 3
#
#
# # Q3: assign the versions of pandas and numpy to variables below
# pd_version = pd.__version__
# np_version = np.__version__
#
# # Q4: Read in the csv file "olive.csv" with pandas.
# #     Assign it to variable `df`
# df = pd.read_csv('olive.csv')
#
# # The fields are:
#
# # Unnamed: 0
# # region
# # area
# # palmitic
# # palmitoleic
# # stearic
# # oleic
# # linoleic
# # linolenic
# # arachidic
# # eicosenoic
#
#
# # Q5: How many rows and columns are there in `df`? Put your answer in a variable `df_shape`.
# df_shape = df.shape
#
# # Q6: assign the first 2 rows of `df` to `df_first_2`
# df_first_two = df.head(2)
#
# # Q7: How many distinct data types are there in `df`?
# df_data_types_count = len(df.dtypes.unique())   # this should be an integer
#
# # Q8: In `df`, create a new column 'sub_region_raw', which will be a copy of the column 'Unnamed: 0'
# df['sub_region_raw'] = df['Unnamed: 0']
#
# # Q9: In `df`, rename 'Unnamed: 0' to 'sub_region_desc'
# df.rename(columns={'Unnamed: 0': 'sub_region_desc'}, inplace=1)
#
# # Q10: In `df`, rename the column 'area' to: 'sub_region'
# df.rename(columns={'area': 'sub_region'}, inplace=1)
#
# # Q11: In `df`, get the unique values of the field 'region'
# region_unique = df['region'].unique()
#
# # Q12: In `df`, how many unique values of the field 'sub_region' are there?
# sub_region_unique_count = len(df['sub_region'].unique())  # should be an integer
#
# # Q13: Lets take a look at the field `sub_region_desc`:
#
# # >>> df['sub_region_desc'].head(5)
# # 0    1.North-Apulia
# # 1    2.North-Apulia
# # 2    3.North-Apulia
# # 3    4.North-Apulia
# # 4    5.North-Apulia
#
# # Looks like 'sub_region_desc' has line numbers attached to the beginning of region name. Remove those and get the unique values in that field, assign it to `srd_unique`
# srd_unique = df['sub_region_desc'].map(lambda r: r.split('.')[-1]).unique()