#!/bin/bash


# todo: add package name
# todo: pick only one between normal method, without preloaded content, with_http_info

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    --skip-validate-spec \
    -g python \
    -o /local/localstack-sdk \
    --global-property models,apis \
    -p packageName=localstack.generated \
    --global-property apiTests=false \
    --global-property apiDocs=false
