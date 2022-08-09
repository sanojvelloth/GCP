from googleapiclient import discovery
def stop_vm(request):
  project = 'project-d-358613'
  zone = 'us-central1-a'
  instance = 'instance-1'
  service = discovery.build('compute', 'v1')
  request = service.instances().stop(project=project, zone=zone, instance=instance)
  response = request.execute()
  return response