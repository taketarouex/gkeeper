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
- [ ] endpointsのデプロイ自動化
  - [ ] endpoint URLをsecret化
- [ ] endpointsのログがないので調査
- [ ] レスポンスを見直す
  - [ ] login failは500エラーにする
  - [ ] requestが解釈できない場合は400
