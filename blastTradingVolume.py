
import requests


url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=blast-ecosystem&order=volume_desc&per_page=100&page=1&sparkline=false&locale=en"


response = requests.get(url)
data = response.json()

# List to store formatted data
formatted_data = data[2]

# # Iterate through each token data dictionary
# for token_data in data:
#     token_name = token_data.get('name', 'N/A')
#     token_price = token_data.get('current_price', 'N/A')
#     total_volume = token_data.get('total_volume', 'N/A')

#     # Append token data to formatted_data list
#     formatted_data.append({
#         'name': token_name,
#         'price': token_price,
#         'total_volume': total_volume
#     })

# Print the formatted data
print(formatted_data)
