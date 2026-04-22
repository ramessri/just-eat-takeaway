import requests


def get_restaurants(postcode, limit=10):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, headers=headers)
    restaurants = response.json()["restaurants"][:limit]
    answer = []
    for r in restaurants:
        name = r['name']
        cuisines = [c['name'] for c in r['cuisines']]
        rating = r['rating']['starRating']
        address = r['address']['firstLine']
        city = r['address']['city']
        postalCode = r['address']['postalCode']


        answer.append({
            'name': name,
            'cuisines': cuisines,
            'rating': rating,
            'address': address,
            'city': city,
            'postalCode': postalCode
            })

    return answer



