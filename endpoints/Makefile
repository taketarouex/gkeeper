.PHONY: add-invoker add-service-management-controller add-config-editor

add-service-management-controller:
	gcloud endpoints services add-iam-policy-binding $(SERVICE_NAME) \
		--member=serviceAccount:$(GCP_SA_EMAIL) --role=roles/servicemanagement.serviceController

add-config-editor:
	gcloud endpoints services add-iam-policy-binding $(SERVICE_NAME) \
		--member=serviceAccount:$(GCP_SA_EMAIL) --role=roles/servicemanagement.configEditor

add-invoker:
	gcloud run services add-iam-policy-binding gkeeper \
		--member "serviceAccount:$(GCP_SA_EMAIL)" \
		--role "roles/run.invoker" \
		--platform managed \
		--project $(GCP_PROJECT) \
		--region $(GCP_REGION)
