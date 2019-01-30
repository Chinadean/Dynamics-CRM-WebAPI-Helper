from Py365CE import *
import sys



def main():
    # Usage "test_auth.py testuser@microsoft.com password123 https://test.crm.dynamics.com test.com"
    username, password, url, tenanturl = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]    # Initialize user_context and the desired tenant. (Uses Adal Python)
    service_client = client_context(f"https://login.microsoftonline.com/{tenanturl}")
    # Lazily auths with already valid clientID.
    service_client.lazy_acquire_token_with_username_password(url, username, password)
    # Creates Record create_record object.
    cr = create_record('accounts', service_client)
    # Sets the data to create the account.
    cr.data = {'name':'Contoso'}
    # Executes the create with debug enabled. (Disables Certificate Check)
    x = service_client.execute(cr)
    print(x)




if __name__ == "__main__":
    main()
