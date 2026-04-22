import requests

def get_restaurants(postcode, limit=10):
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {"user-agent": "my-app/0.0.1"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        restaurants = response.json()["restaurants"][:limit]
    except requests.exceptions.RequestException:
        return []

    answer = []
    for r in restaurants:
        name = r['name']
        cuisines = [c['name'] for c in r['cuisines']]
        rating = r['rating']['starRating']
        address = r['address']['firstLine']
        city = r['address']['city']
        postalCode = r['address']['postalCode']
        logo = r.get('logoUrl')


        answer.append({
            'name': name,
            'cuisines': cuisines,
            'rating': rating,
            'address': address,
            'city': city,
            'postalCode': postalCode,
            'logo': logo,
            })

    return answer



