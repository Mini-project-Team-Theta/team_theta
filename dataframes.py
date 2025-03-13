import pandas as pd
import os

#Csv files urls
isosyote_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Isosyote_weather.csv'
kittila_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Kittila_weather.csv'
kuusamo_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Kuusamo_weather.csv'
lahti_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Lahti_weather.csv'
pyha_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Pyha_weather.csv'
salla_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Salla_weather.csv'
tahko_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Tahko_weather.csv'
turku_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Turku_weather.csv'
vuokatti_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/target/zip/Vuokatti_weather.csv'

#Dataframes 
isosyote_df = pd.read_csv(isosyote_url)
kittila_df = pd.read_csv(kittila_url)
kuusamo_df = pd.read_csv(kuusamo_url)
lahti_df = pd.read_csv(lahti_url)
pyha_df = pd.read_csv(pyha_url)
salla_df = pd.read_csv(salla_url)
tahko_df = pd.read_csv(tahko_url)
turku_df = pd.read_csv(turku_url)
vuokatti_url = pd.read_csv(vuokatti_url)

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Functions
def check_nan_sum(df):
    return df.isna().sum()

def check_datatypes(df):
    return df.dtypes

def replace_comma(df):
    for col in df.columns:
        if df[col].dtype == 'object':  
            df[col] = df[col].str.replace(",", ".", regex=False)  
            try:
                df[col] = df[col].astype(float)  
            except ValueError:
                pass

def change_column_name_celcius(df):
    for col in df.columns:
        if col.startswith('Average temperature'):
            df.rename(columns={col: 'Average temperature [°C]'}, inplace=True)

def drop_column_localtime(df):
    for col in df.columns:
        if 'Time [Local time]' in col:
            df.drop(columns='Time [Local time]', inplace=True)

def reorder_columns_all_dfs(column_order):
    for name, obj in list(globals().items()):  
        if isinstance(obj, pd.DataFrame):  
            obj = obj[column_order]
            globals()[name] = obj

def change_column_name_snowdepth(df):
    for col in df.columns:
        if col.startswith('Snow depth'):
            df.rename(columns={col: 'Snow depth mean [cm]'}, inplace=True) 

#Convert to csv files
def save_dfs_to_csv(target_dir='csv_files'):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    for name, obj in list(globals().items()):  
        if isinstance(obj, pd.DataFrame):  
            file_path = os.path.join(target_dir, f"{name}.csv")
            obj.to_csv(file_path, index=False)
            print(f"Saved {name} to {file_path}")

# deletes local time columns
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        drop_column_localtime(obj)

# Modifies average temp column names to [°C]
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        change_column_name_celcius(obj)

# Modifies snow depth column name to identicals
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        change_column_name_snowdepth(obj)

# Replaces comma in Global radiation mean [W/m2] column and changes type to float
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        replace_comma(obj)

# Define the desired column order
columns_order = ['Observation station', 'Year', 'Month', 'Day', 'Date', 'Snow depth mean [cm]', 'Average temperature [°C]', 'cloud_code', 'Global radiation mean [W/m2]']
reorder_columns_all_dfs(columns_order)

save_dfs_to_csv(target_dir='final')

# Use this to check data
'''
# Prints sum of NaN values for each df
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        print(f"NaN count in {name}:")
        print(check_nan_sum(obj))
        print("-" * 30)

# Prints datatypes 
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame): 
        print(f"Datatypes in {name}:")
        print(check_datatypes(obj))
        print("-" * 30)
'''
# Prints sample      
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):
        print(obj.sample(5))
        print("-" * 30)

