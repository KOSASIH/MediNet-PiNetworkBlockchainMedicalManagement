import requests

def get_wearable_data(api_url: str, api_key: str) -> pd.DataFrame:
    """
    Retrieve the wearable device data from the API.

    Args:
        api_url (str): The URL of the wearable device API.
        api_key (str): The API key for authentication.

    Returns:
        pd.DataFrame: The raw wearable device data.
    """
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        data = pd.DataFrame.from_records(data['data'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')

        return data
    else:
        raise Exception(f'Error retrieving data from API: {response.status_code}')
