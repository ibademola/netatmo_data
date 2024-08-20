import time
import requests
from netatmo_data.utility import (
    get_ids,
    save_netatmo_data_to_csv,
    load_device_and_module_ids_from_csv,
    get_historical_measurements_batch,
    convert_to_unix_timestamp
)

def get_access_token(client_id, client_secret, refresh_token):
    # URL for token endpoint
    token_url = "https://api.netatmo.com/oauth2/token"

    # Parameters for token request
    params = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret
    }

    # Send POST request to get access token
    response = requests.post(token_url, data=params)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        token_data = response.json()
        # Access token
        access_token = token_data["access_token"]
        return access_token
    else:
        print("Error:", response.status_code, response.text)
        return None


def fetch_station_ids(access_token, lat_ne, lon_ne, lat_sw, lon_sw, csv_file):
    ids = get_ids(access_token, lat_ne, lon_ne, lat_sw, lon_sw)
    save_netatmo_data_to_csv(ids, csv_file)
    return ids

def fetch_temperature_data(access_token, csv_file, start_date_stamp, start_time_stamp, end_date_stamp, end_time_stamp):

    # Load device IDs and module IDs from the CSV file
    device_module_ids = load_device_and_module_ids_from_csv(csv_file)
    
    # Iterate through each device ID and module ID pair
    for device_id, module_id in device_module_ids:
        scale = "1day"  # Change according to your requirement
        types = "Temperature"  # Fetch only temperature data
        date_begin = convert_to_unix_timestamp(start_date_stamp, start_time_stamp)
        date_end = convert_to_unix_timestamp(end_date_stamp, end_time_stamp)
        limit = 1024

        # Fetch historical measurements for the current device ID and module ID pair
        measurements = get_historical_measurements_batch(access_token, device_id, module_id, scale, types, date_begin, date_end, limit)
        print(f'--------Temperature data for {device_id}, {module_id} completely downloaded----------')