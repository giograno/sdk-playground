import localstack.generated
from localstack.generated import Configuration, FaultRule, NetworkEffectsConfig


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


class ChaosClient(BaseClient):
    def __init__(self, protocol: str | None = None, host: str | None = None) -> None:
        super().__init__(protocol, host)
        self._api = localstack.generated.ChaosApi(self.client)

    def set_fault_rules(self, fault_rule: list[FaultRule], **kwargs) -> list[FaultRule]:
        return self._api.set_fault_rules(fault_rule=fault_rule)

    def add_fault_rules(
        self, fault_rules: list[FaultRule], **kwargs
    ) -> list[FaultRule]:
        return self._api.add_fault_rules(fault_rule=fault_rules)

    def delete_fault_rules(
        self, fault_rules: list[FaultRule], **kwargs
    ) -> list[FaultRule]:
        return self._api.delete_fault_rules(fault_rule=fault_rules)

    def get_fault_rules(self, **kwargs) -> list[FaultRule]:
        return self._api.get_fault_rules()

    def get_network_effects(self) -> NetworkEffectsConfig:
        return self._api.get_network_effects()

    def set_network_effects(
        self, network_effects_config: NetworkEffectsConfig
    ) -> NetworkEffectsConfig:
        return self._api.set_network_effects(
            network_effects_config=network_effects_config
        )


class LocalStackClient(BaseClient):
    def __init__(self, protocol: str | None = None, host: str | None = None) -> None:
        super().__init__(protocol, host)
        self._api = localstack.generated.LocalstackApi(self.client)

    def get_features_and_services(self):
        return self._api.get_features_and_services()
