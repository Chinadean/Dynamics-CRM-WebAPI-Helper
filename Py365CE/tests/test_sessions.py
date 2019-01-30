from Py365CE import *
import sys
import requests


def main():
    # Usage "test_auth.py testuser@microsoft.com password123 https://test.crm.dynamics.com test.com"
    username, password, url, tenanturl = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]    # Initialize user_context and the desired tenant. (Uses Adal Python)
    service_client = client_context(f"https://login.microsoftonline.com/{tenanturl}")
    # Lazily auths with already valid clientID.
    service_client.lazy_acquire_token_with_username_password(url, username, password)
    # Creates Record create_record object.
    token = service_client.get_auth_value('accessToken')
    r = requests.session()
    r.headers.update({'Authorization':'Bearer ' + service_client.get_auth_value('accessToken')})
    for i in range(10):
        r.get("https://coltonlathrop.crm.dynamics.com/api/data/v9.1/", verify=False)
    if r.cookies._find('ApplicationGatewayAffinit'):
        print(r.cookies._find('ApplicatiosnGatewayAffinity'))
    for i in range(10):
        r.get("https://coltonlathrop.crm.dynamics.com/api/data/v9.1/", verify=False)


if __name__ == "__main__":
    main()
