import localstack.generated
from localstack.generated import Configuration


class BaseClient:
    host: str
    protocol: str
    configuration: Configuration
    client: localstack.generated.ApiClient

    def __init__(self, protocol: str | None = None, host: str | None = None) -> None:
        self.protocol = protocol or "http"
        self.host = host or "localhost.localstack.cloud:4566"
        self.configuration = Configuration(host=f"{self.protocol}://{self.host}")
        self.client = localstack.generated.ApiClient(configuration=self.configuration)