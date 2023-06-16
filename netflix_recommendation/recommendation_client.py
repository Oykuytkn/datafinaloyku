import requests
import json

# Prepare the user input data
user = {
    'Country': 'South Korea',
    'Title': 'Black Mirror',
    'Date Watched': '2022-02-11',
    'Percentage Watched': 90,
    'Rating': 'Rating_TV-Y7'
}
# Send a POST request to the recommendation endpoint
response = requests.post('http://oykuuu.pythonanywhere.com', json=user)

# Parse the response JSON
recommendations = json.loads(response.text)

# Process the recommendations as needed
print(recommendations)
