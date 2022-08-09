from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'project-d-358613'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-central1-a'  # TODO: Update placeholder value.

# Name of the instance resource to start.
instance = 'instance-1'  # TODO: Update placeholder value.

request = service.instances().start(project=project, zone=zone, instance=instance)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)