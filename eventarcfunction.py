import functions_framework
from googleapiclient import discovery
def hello_auditlog(data, context):
    from googleapiclient import discovery
    project = 'project-d-358613'
    zone = 'us-central1-a'
    instance = 'instance-1'
    service = discovery.build('compute', 'v1')
    request = service.instances().start(project=project, zone=zone, instance=instance)
    response = request.execute()
    return response
