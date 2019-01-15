def GenerateConfig(context):
  """Generate YAML resource configuration."""

  cluster_name = context.properties['test cluster']
  cluster_zone = context.properties['europe-west4-a']
  number_of_nodes = context.properties['2']

  resources = []
  resources.append({
      'name': cluster_name,
      'type': 'container.v1.cluster',
      'properties': {
          'zone': cluster_zone,
          'cluster': {
              'name': cluster_name,
              'initialNodeCount': number_of_nodes,
              'nodeConfig': {
                  'oauthScopes': [
                      'https://www.googleapis.com/auth/' + scope
                      for scope in [
                          'compute',
                          'devstorage.read_only',
                          'logging.write',
                          'monitoring'
                        ]
                    ]
                }
            }
        }
    })
  outputs.append({
        'name': 'endpoint',
        'value': '$(ref.' + cluster_name + '.endpoint)'
    })
  return {'resources': resources, 'outputs': outputs}