from Py365CE import *
import sys
import getopt


def main():
    # Usage "test_auth.py testuser@microsoft.com password123 https://test.crm.dynamics.com"
    #username, password, url = sys.argv[1], sys.argv[2], sys.argv[3]

    print(service_client.cache._cache)
if __name__ == "__main__":
    main()
