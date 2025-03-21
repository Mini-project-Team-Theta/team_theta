import pandas as pd
import os
from glob import glob

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

data_dir = CURR_DIR_PATH + "/Raw_data/"
target_dir = CURR_DIR_PATH + "/target/"

# Function to get the data from needed global solar radiation measurement spot.
def get_radiation_measurements(radiation_point):
    radiation_paths = glob(data_dir + "*_global_*")
    file_path = [i for i in radiation_paths if radiation_point in i]
    file = pd.read_csv(file_path[0], sep=";", na_values=['-'])
    file["Date"] = pd.to_datetime(file[["Year", "Month", "Day"]])
    file = file.drop(["Observation station", "Year", "Month", "Day"], axis=1)

    return file

# Read weather data from files for needed venue place.
def read_weather_data(venue_name):
    #Cloud data
    cloud_file_path = glob(data_dir + venue_name + "cloud_*")
    venue_cloud = pd.read_csv(cloud_file_path[0], na_values=['-'], encoding="ISO-8859-1")
    venue_cloud["Date"] = pd.to_datetime(venue_cloud[["Year", "Month", "Day"]])
    venue_cloud["cloud_code"] = venue_cloud["Cloud cover [1/8]"].fillna("")
    venue_cloud["cloud_code"] = (
    venue_cloud["cloud_code"]
    .astype(str)  # Convert to string in case of mixed types
    .str.extract(r"(\d+)/\d+")  # Extract the first number before "/"
    .astype(float)  # Convert to float
    )
    venue_cloud = venue_cloud.drop(["Observation station", "Year", "Month", "Day","Time [Local time]", "Cloud cover [1/8]"], axis=1)
    #Snow data
    snow_file_path = glob(data_dir + venue_name + "snow_*")
    venue_snow = pd.read_csv(snow_file_path[0], na_values=['-'], encoding="ISO-8859-1")
    venue_snow["Date"] = pd.to_datetime(venue_snow[["Year", "Month", "Day"]])
    venue_snow = venue_snow.drop(["Time [Local time]"], axis=1)
    #Temperature data
    avg_file_path = glob(data_dir + venue_name + "avg_*")
    venue_avg = pd.read_csv(avg_file_path[0], na_values=['-'], encoding="ISO-8859-1")
    venue_avg["Date"] = pd.to_datetime(venue_avg[["Year", "Month", "Day"]])
    venue_avg = venue_avg.drop(["Observation station", "Year", "Month", "Day","Time [Local time]"], axis=1)

    return venue_cloud, venue_snow, venue_avg

city = input("city: ").capitalize()
radiation_point = input("Which radiation measure is used? (Helsinki/Sodankylä/Sotkamo): ").capitalize()
file_name = city + "_"

radiation = get_radiation_measurements(radiation_point)
venue_cloud, venue_snow, venue_avg = read_weather_data(file_name)

# Merge data to final version and import as csv.
merged_columns = venue_snow.merge(venue_avg, on="Date", how="left").merge(venue_cloud, on="Date", how="left").merge(radiation, on="Date", how="left")
merged_columns = merged_columns.drop_duplicates()
merged_columns.to_csv(target_dir + f"zip/{file_name}weather.csv", index=False)