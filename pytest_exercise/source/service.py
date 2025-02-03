import requests

database = {
    1: "Amazon",
    2: "Aple",
    3: "Google",
    4: "Meta"
}


def get_from_db(user_id):
    return database.get(user_id)


# Function that fetches users from the API
def get_users_from_api():
    # Make an HTTP GET request to the placeholder API
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the response data in JSON format
        return response.json()

    # Raise an HTTPError if the request was not successful
    raise requests.HTTPError("Failed to retrieve users from the API.")
