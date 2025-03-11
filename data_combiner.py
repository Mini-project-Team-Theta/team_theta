import pandas as pd
import os
from glob import glob

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

data_dir = CURR_DIR_PATH + "/Raw_data/"
target_dir = CURR_DIR_PATH + "/target/"

def read_weather_data(venue_name):
    #Cloud data
    cloud_file_path = glob(data_dir + venue_name + "cloud_*")
    venue_cloud = pd.read_csv(cloud_file_path[0])
    venue_cloud["Date"] = pd.to_datetime(venue_cloud[["Year", "Month", "Day"]])
    venue_cloud = venue_cloud.drop(["Observation station", "Year", "Month", "Day","Time [Local time]"], axis=1)
    #Snow data
    snow_file_path = glob(data_dir + venue_name + "snow_*")
    venue_snow = pd.read_csv(snow_file_path[0])
    venue_snow["Date"] = pd.to_datetime(venue_snow[["Year", "Month", "Day"]])
    #Temperature data
    avg_file_path = glob(data_dir + venue_name + "avg_*")
    venue_avg = pd.read_csv(avg_file_path[0])
    venue_avg["Date"] = pd.to_datetime(venue_avg[["Year", "Month", "Day"]])
    venue_avg = venue_avg.drop(["Observation station", "Year", "Month", "Day","Time [Local time]"], axis=1)

    return venue_cloud, venue_snow, venue_avg

city = input("city: ").capitalize()
file_name = city + "_"

venue_cloud, venue_snow, venue_avg = read_weather_data(file_name)

merged_columns = venue_snow.merge(venue_avg, on="Date").merge(venue_cloud, on="Date")

merged_columns = merged_columns.drop_duplicates()

merged_columns.to_csv(target_dir + f"zip/{file_name}weather.csv", index=False)