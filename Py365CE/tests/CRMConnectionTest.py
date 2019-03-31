from Py365CE import CRMConnection

conn = CRMConnection('https://login.microsoftonline.com/coltonlathrop.net')
conn.lazy_acquire_token_with_username_password('https://coltonlathrop.crm.dynamics.com', 'admin@coltonlathrop.net','Fargoctslabs!')

print(list(conn.cache._cache.values())[0]['expiresOn'])
print('x')

