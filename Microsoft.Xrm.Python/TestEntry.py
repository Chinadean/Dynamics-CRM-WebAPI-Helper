from Xrm import Xrm


x = Xrm.ClientCredentials()
x.CRMUrl = "https://colton.api.crm.dynamics.com"
x.Password = "Fargoctslabs!"
x.Username = "admin@coltonlathrop.net"

xx = Xrm.OrganizationServiceProxy()
xx.ClientCredentials = x
xx.Authenticate()

print(xx.CheckToken())

