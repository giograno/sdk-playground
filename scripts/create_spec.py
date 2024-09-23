# This script is used to fetch all possible OpenAPI schemas we ship with LocalStack
# packages and aggregate them in a single one.
from pathlib import Path

from localstack.utils.openapi import get_localstack_openapi_spec
import yaml
import os

openapi_path = Path(os.path.dirname(__file__)) / '..' / "openapi.yaml"


def main():
    spec = get_localstack_openapi_spec()
    with open(openapi_path, 'w') as f:
        yaml.dump(spec, f, sort_keys=False)


if __name__ == "__main__":
    main()
