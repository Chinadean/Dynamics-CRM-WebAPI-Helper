from Py365CE import *
import sys



def main():
    # Usage "test_auth.py testuser@microsoft.com password123 https://test.crm.dynamics.com test.com"
    username, password, url, tenanturl = sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4],
    service_client = user_context(f"https://login.microsoftonline.com/{tenanturl}")
    service_client.lazy_acquire_token_with_username_password(url, username, password)
    print(service_client.is_authed)
    print(service_client.default_headers)
    x = create_record('accounts', service_client)
    x.data = {'name':'test accounts boi'}
    v = x.execute(debug=True)
    print(v.status_code)
    print(v.elapsed.microseconds/1000)


if __name__ == "__main__":
    main()
