import localstack.generated
from localstack.generated import Configuration

class PodClient:

    def __init__(self):
        pass


class LocalStackClient():
    configuration: Configuration

    def __init__(self):
        self.configuration = Configuration(host="http://localhost.localstack.cloud:4566")

    def delete_ddb_items(self):
        with localstack.generated.ApiClient(self.configuration) as client:
            api_instance = localstack.generated.AwsApi(client)
            resp = api_instance.delete_ddb_expired_items
            return resp


