run:
	python src/main.py

test:
	pytest tests/

#########
### DOCKER LOCAL
#########

build_container_local:
	docker build --tag=$$IMAGE:dev .

run_container_local:
	docker run -it -e PORT=8000 -p 8000:8000 $$IMAGE:dev


#####
## PUSH IMAGE TO DOCKER
#####

## AUTHENTICATE DOCKER
allow_docker_push:
	gcloud auth configure-docker $$GCP_REGION-docker.pkg.dev

## CREATE ARTIFACTS REPO
create_artifacts_repo:
	gcloud artifacts repositories create $$ARTIFACTSREPO --repository-format=docker \
	--location=$$GCP_REGION --description="Repository for storing images"

## BUILD IMAGE
build_for_production:
	docker build -t  $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod .

######
## ONLY FOR MAC USERS IN ORDER TO BUILD IMAGES
######
m_chip_build_image_production:
	docker build --platform linux/amd64 -t $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod .

## PUSHING IMAGE TO DOCKER
push_image_production:
	docker push $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod


## DEPLOY TO CLOUD RUN
deploy_to_cloud_run:
	gcloud run deploy --image $$GCP_REGION-docker.pkg.dev/$$GCP_PROJECT/$$ARTIFACTSREPO/$$IMAGE:prod --memory $$MEMORY --region $$GCP_REGION

## DEPLOY TO CLOUD RUN WITH COSTOM DOMAIN
deploy_to_cloud_run_with_custom_domain:
	gcloud beta run domain-mappings create --service $$GCP_PROJECT --domain $$CUSTOM_DOMAIN

## STOP SERVICES RUNNING SERVICES TO AVOID EXTRA COSTS
cloud_run_disable_service:
	gcloud run services update $$INSTANCE --min-instances=0



############################################
########   DELETE SERVICES  ################
############################################

cloud_run_delete_service:
	gcloud run services delete $$INSTANCE

############################################

app_run:
	streamlit run src/app.py