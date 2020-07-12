# gkeeper endpoint

To protect gkeeper endpoint,
add [Cloud Endpoints](https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run?hl=ja)

You need api key to access gkeeper endpoint.

## deploy

Auto deploy when update files in `endpoints` dir.
Refer [github actions](../.github/workflows/endpoints.yml)

First, you need to deploy ESP on Cloud run.
Refer [Cloud Endpoints for cloud Run](https://cloud.google.com/endpoints/docs/openapi/get-started-cloud-run?hl=ja)

Set your endpoints host on Cloud Run to github secrets ENDPOINTS_HOST

Add service management controller to your CI service account.
`GCP_SA_EMAIL=[your CI service account] ENDPOINTS_HOST=[endpoints host] make add-service-management-controller`

### API Gateway

`make gateway-deploy`

### Cloud Endpoints

`make endpoints-deploy`

### API key

create API key at [GCP credentials](https://console.cloud.google.com/apis/credentials?hl=ja&project=tktkc-243513).
and add it to your request query `key=APIKEY`
