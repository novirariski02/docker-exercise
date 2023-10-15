# Import necessary libraries
import requests
import pandas as pd

# URL for the Open Cage API
url = 'https://api.opencagedata.com/geocode/v1/json'

# API key for Open Cage
api_key = 'a34768ccd55d49cfa29fb5753e2d1486'

# Extract the list of countries from the DataFrame
countries = df['country'].tolist()

# Create a dictionary of the components data for each country
components_list = []

# Loop through each country and make a request to the Open Cage API
for country in countries:
    # Create the API request parameters
    params = {'q': country, 'key': api_key}

    # Send a request to the API
    response = requests.get(url, params=params)

    # Parse the JSON response
    json_data = response.json()

    # Extract the components data from the JSON response
    components = json_data['results'][0]['components']

    # Create a dictionary of the components data for this country
    country_components = {'country': country,
                          'country_code': components.get('country_code', ''),
                          'latitude': json_data['results'][0]['geometry']['lat'],
                          'longitude': json_data['results'][0]['geometry']['lng']}

    # Append the dictionary to a list of dictionaries
    components_list.append(country_components)

# Create a DataFrame for the components data
components_df = pd.DataFrame(components_list)
components_df