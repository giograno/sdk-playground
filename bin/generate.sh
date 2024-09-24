#!/bin/bash


# todo: add package name
# todo: pick only one between normal method, without preloaded content, with_http_info

# supportingFiles generates stuff like:
#   - api_client.py
#   - api_response.py
#   - configuration.py
#   - exceptions.py
#   - rest.py
# we can decide to move these outside the generated package and work on them manually.

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    --skip-validate-spec \
    -g python \
    -o /local/localstack-sdk \
    --global-property models,apis \
    -p packageName=localstack.generated \
    --template-dir /local/templates \
    --global-property apiTests=false,modelTests=false \
#    --global-property apiDocs=false
