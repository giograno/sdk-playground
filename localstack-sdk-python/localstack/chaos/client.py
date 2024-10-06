from localstack.clients import BaseClient
from localstack.api.chaos_api import ChaosApi
from localstack.models import FaultRule, NetworkEffectsConfig


class Client(BaseClient):
    def __init__(self, protocol: str | None = None, host: str | None = None) -> None:
        super().__init__(protocol, host)
        self._api = ChaosApi(self.client)

    def set_fault_rules(self, fault_rules: list[FaultRule]) -> list[FaultRule]:
        return self._api.set_fault_rules(fault_rule=fault_rules)

    def add_fault_rules(
        self, fault_rules: list[FaultRule]) -> list[FaultRule]:
        return self._api.add_fault_rules(fault_rule=fault_rules)

    def delete_fault_rules(self, fault_rules: list[FaultRule]) -> list[FaultRule]:
        return self._api.delete_fault_rules(fault_rule=fault_rules)

    def get_fault_rules(self) -> list[FaultRule]:
        return self._api.get_fault_rules()

    def get_network_effects(self) -> NetworkEffectsConfig:
        return self._api.get_network_effects()

    def set_network_effects(
        self, network_effects_config: NetworkEffectsConfig
    ) -> NetworkEffectsConfig:
        return self._api.set_network_effects(
            network_effects_config=network_effects_config
        )

