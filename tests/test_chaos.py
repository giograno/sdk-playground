from localstack.generated import FaultRule
from localstack.sdk.clients import ChaosClient


class TestLocalStackClient:
    client = ChaosClient()

    def test_rules_crud(self):
        rule_one = FaultRule(region="us-east-1", service="s3")
        rules = self.client.add_fault_rules(fault_rules=[rule_one])
        assert len(rules) == 1
        assert rules[0].region == "us-east-1"
        assert rules[0].service == "s3"
        rules = self.client.get_fault_rules()
        assert len(rules) == 1
        assert rules[0].region == "us-east-1"
        assert rules[0].service == "s3"

        rule_two = FaultRule(region="us-east-1", service="dynamodb")
        rules = self.client.add_fault_rules(fault_rules=[rule_two])
        assert len(rules) == 2

        rules = self.client.delete_fault_rules(fault_rules=[rule_one])
        assert len(rules) == 1
        assert rules[0].region == "us-east-1"
        assert rules[0].service == "dynamodb"

        rules = self.client.set_fault_rules(fault_rule=[])
        assert not rules
