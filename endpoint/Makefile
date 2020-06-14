.PHONY: gateway-deploy endpoints-deploy add-invoker

gateway-deploy:
	gcloud run deploy gkeeper-gateway \
		--image "gcr.io/$(GCP_PROJECT)/endpoints-runtime-serverless:$(CLOUD_RUN_HOST_NAME)-$(CONFIG_ID)" \
		--allow-unauthenticated \
		--platform managed \
		--project $(GCP_PROJECT) \
		--region $(GCP_REGION) \
		--service-account $(GCP_SA_EMAIL)


endpoints-deploy:
	gcloud endpoints services deploy openapi.yaml \
		--project $(GCP_PROJECT)

add-invoker:
	gcloud run services add-iam-policy-binding gkeeper \
		--member "serviceAccount:$(GCP_SA_EMAIL)" \
		--role "roles/run.invoker" \
		--platform managed \
		--project $(GCP_PROJECT) \
		--region $(GCP_REGION)
