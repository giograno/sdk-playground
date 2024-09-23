#!/bin/bash

#  openapi-generator generate -i localstack-pro-core/localstack/pro/core/openapi.yaml -g python --skip-validate-spec -o /tmp/test/

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i openapi.yaml \
    --skip-validate-spec \
    -g python \
    -o /local/out/python \
    -p sourceFolder=localstack