#!/bin/bash

#  openapi-generator generate -i localstack-pro-core/localstack/pro/core/openapi.yaml -g python --skip-validate-spec -o /tmp/test/

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    --skip-validate-spec \
    -g python \
    -o /local/localstack-sdk/localstack/gen \
    --global-property models,apis \
    -p sourceFolder=localstack