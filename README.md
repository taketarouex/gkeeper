# keep-shopping-list

![build](https://github.com/tktkc72/gkeeper/workflows/build/badge.svg?branch=master)

add item to Google Keep list

## Description

add item to Google Keep list by cloud functions.
You can get the http endpoint which can do it.

If you use IFTTT to post the http_endpoint,
you can add items to Keep by your voice.

## Install

`make install`

## Deploy

deploy to cloud run.
[git hub actions](https://github.com/taketarouex/gkeeper/actions?query=workflow%3ADelivery)

## Test

`make test`

## Requirements

- poetry
- make

## TODO

- [x] 複数リストに対応する
- [ ] アクセスポイントを保護する
- [ ] ユーザ/パスワードは環境変数じゃなくする
- [x] tokenを使用してlogin回数をへらす
