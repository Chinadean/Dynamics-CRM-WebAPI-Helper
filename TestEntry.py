from Xrm import Xrm

def main():
    """ Authentication Test
    x = Xrm.ClientCredentials()
    x.CRMUrl = "https://colton.api.crm.dynamics.com"
    x.Password = ""
    x.Username = "admin@coltonlathrop.net"

    xx = Xrm.OrganizationServiceProxy()
    xx.ClientCredentials = x
    xx.Authenticate()

    print(xx.AccessToken)
    print(xx.AccessTokenExpiry)
    """

    entity = Xrm.Entity()
    entity.EntityType = "contact"
    entity.AddAttribute(["name", "paul"])
    print("Attributes: " + str(entity.Attributes))
    print(entity.EntityType)
    print(str(entity.GetAttributes()))
    entity.SetAttributes({"name":"test", "phone1":"test"})
    print(str(entity.GetAttributes()))

    entitycollection = Xrm.EntityCollection()
    for i in range(100):
        entitycollection.Entities.append(entity)

    for i in entitycollection.Entities:
        print(i.GetAttributes())



if __name__ == "__main__":
    main()


