import requests 




# 1. Unauthorized GET 

response = requests.get("https://api.github.com/user")


print(f"Status Code: {response.status_code}")



# 2. Unauthorized GET 

response = requests.get("https://api.github.com/users/octocat")


print(f"Status Code: {response.status_code}")

# 3. Headers Function

def create_auth_headers(api_key: str, auth_type: str) -> dict:
    """Return authentication headers based on the auth type."""

    if auth_type == "bearer":
        return {
            "Authorization": f"Bearer {api_key}"
        }

    elif auth_type == "api-key":
        return {
            "X-API-Key": api_key
        }

    else:
        raise ValueError("Auth type must be 'bearer' or 'api-key'.")


print(create_auth_headers("my_secret_key", "bearer"))
print(create_auth_headers("my_secret_key", "api-key"))