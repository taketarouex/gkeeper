.PHONY: add-invoker add-api-key

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