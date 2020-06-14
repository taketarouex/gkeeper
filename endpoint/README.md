# gkeeper endpoint

gkeeperのエンドポイントを保護するため、
[Cloud Endpoints](https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run?hl=ja)を設定する

## deploy

### API Gateway

`make gateway-deploy GCP_PROJECT=YOUR_PROJECT GCP_REGION=YOUR_REGION`

### Cloud Endpoints

`make endpoints-deploy GCP_PROJECT=YOUR_PROJECT`
