import pandas as pd

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

#Continue from here

def check_nan_sum(df):
    return df.isna().sum()

def check_datatypes(df):
    return df.dtypes

# Prints sum of NaN values for each df
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame):  # Ensure it's a DataFrame
        print(f"NaN count in {name}:")
        print(check_nan_sum(obj))
        print("-" * 30)

# Prints datatypes 
for name, obj in list(globals().items()):
    if isinstance(obj, pd.DataFrame): 
        print(f"Datatypes in {name}:")
        print(check_datatypes(obj))
        print("-" * 30)
  


