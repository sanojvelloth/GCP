from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'beta', credentials=credentials)
project = 'my-project'
zone = 'my-zone'
instance = 'my-instance'
request = service.instances().stop(project=project, zone=zone, instance=instance)
response = request.execute()
pprint(response)