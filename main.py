from simple_salesforce import Salesforce, SalesforceLogin, SFType

username = 'jbaird@resilient-moose-iiply3.com'
password = 'Samsung1990!'
security_token = 'hEBlBiBOBMCmeLlOdvWcvKy1'
domain = 'login' # or test

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)

# sf.Contact.create({'FirstName': 'Jane', 'LastName':'Henderson','Email':'example@example.com'})


querySOQL = """
            SELECT ContentDocumentId FROM ContentDocumentLink WHERE LinkedEntityId = '0018d000003M7qkAAC'

            """

response = sf.query(querySOQL)


instance_name = sf.sf_instance

for x in response.get('records'):
    url = x['ContentDocumentId']

    querySOQL2 = f"""SELECT LatestPublishedVersionId FROM ContentDocument WHERE Id = '{url}'"""

    individual_document_query = sf.query(querySOQL2)

    doc_id = individual_document_query["records"][0]["LatestPublishedVersionId"]

    endPoint = f"""/services/data/v52.0/sobjects/ContentVersion/{doc_id}/VersionData"""

    doc_request = sf.session.get('https://{0}{1}'.format(instance_name, endPoint), headers=sf.headers)

    print(doc_request.content.decode("latin"))

#####################################################


# querying a single doc
# example = "/services/data/v52.0/sobjects/ContentVersion/0688d000000iDbAAAU/VersionData"
# request = sf.session.get('https://{0}{1}'.format(instance_name, example), headers=sf.headers)
# print(request.content)
# print(request.content.decode("latin"))
