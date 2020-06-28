.PHONY: endpoints-deploy build-gateway gateway-deploy add-invoker add-api-key

endpoints-deploy:
	gcloud endpoints services deploy openapi.yaml \
		--project $(GCP_PROJECT)

build-gateway:
	./gcloud_build_image -s $(GATEWAY_RUN_HOST_NAME) -c $(CONFIG_ID) -p ${GCP_PROJECT}

gateway-deploy: build-gateway
	gcloud run deploy gkeeper-gateway \
		--image "gcr.io/$(GCP_PROJECT)/endpoints-runtime-serverless:$(GATEWAY_RUN_HOST_NAME)-$(CONFIG_ID)" \
		--allow-unauthenticated \
		--platform managed \
		--project $(GCP_PROJECT) \
		--region $(GCP_REGION) \
		--service-account $(GCP_SA_EMAIL)

add-service-management-controller:
	gcloud endpoints services add-iam-policy-binding $(GATEWAY_RUN_HOST_NAME) \
		--member=serviceAccount:$(GCP_SA_EMAIL) --role=roles/servicemanagement.serviceController

add-invoker:
	gcloud run services add-iam-policy-binding gkeeper \
		--member "serviceAccount:$(GCP_SA_EMAIL)" \
		--role "roles/run.invoker" \
		--platform managed \
		--project $(GCP_PROJECT) \
		--region $(GCP_REGION)
