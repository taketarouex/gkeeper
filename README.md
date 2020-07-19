# keep-shopping-list

![test](https://github.com/tktkc72/gkeeper/workflows/test/badge.svg?branch=master)
![delivery](https://github.com/tktkc72/gkeeper/workflows/delivery/badge.svg?branch=master)

add item to Google Keep list

## Description

add item to Google Keep list by GCP cloud run.
You can get the http endpoint which can do it.

If you use IFTTT to post the http_endpoint,
you can add items to Keep by your voice.

## Install

`make install`

## Deploy

If master branch merged, deploy to cloud run.
[git hub actions](https://github.com/tktkc72/gkeeper/actions?query=workflow%3Adelivery)

you must set below github secrets.

- KEEP_USER
  - your google user ID
- KEEP_PASSWORD
  - your google password
- GCP_PROJECT
  - where you deploy
- GCP_REGION
  - where you deploy
- GCP_SA_EMAIL
  - run gkeeper
  - need below
    - roles/servicemanagement.serviceController
    - roles/run.invoker
- GCP_CI_SA_KEY
  - key of service account deploy gkeeper
  - need below
    - roles/servicemanagement.configEditor
    - roles/run.admin
    - roles/storage.objectAdmin
- SERVICE_NAME
  - used to name of gkeeper cloud run
- GATEWAY_NAME
  - used to name of ESPv2 Cloud Run
- ENDPOINTS_HOST
  - ESPv2 Cloud Run host name
- BACKEND_ADDRESS
  - gkeeper Cloud Run URL

## Protect endpoint

You need API Key to use API.
API Endpoint is protected by ESPv2.
Refer to [endpoint readme](endpoints/README.md)

## Test

`make test`

### e2e-test

`./e2e_test.sh`

need to crate a keep list named `test_gkeeper`

## Requirements

- poetry
- make

## TODO

- [x] 複数リストに対応する
- [x] アクセスポイントを保護する
- [x] tokenを使用してlogin回数をへらす
- [x] endpointsのデプロイ自動化
  - [x] endpoint URLをsecret化
