from Py365CE import service
import sys
import getopt


def main():
    # Usage "test_auth.py testuser@microsoft.com password123 https://test.crm.dynamics.com"
    username, password, url = sys.argv[1], sys.argv[2], sys.argv[3]
    service_client = service(username, password, url)

    print(service_client.credentials)
    print(service_client.token_endpoint)
    print(service_client.access_token)
    print(service_client.access_token_expiry)
    print(service_client.api_url)

if __name__ == "__main__":
    main()
