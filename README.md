## WIP
```bash
export PROJECT_ID=hello-world-418507
export IMAGE_NAME=hello-fastapi
export REPO=test-tobedeleted

docker tag ${IMAGE_NAME} ${REPO}/${PROJECT_ID}/${IMAGE_NAME}
docker push ${REPO}/${PROJECT_ID}/${IMAGE_NAME}

docker tag ${IMAGE_NAME} us-central1-docker.pkg.dev/hello-world-418507/test-tobedeleted/hello-fastapi
```

## Deploy
```bash
export PROJECT_ID=hello-world-418507
gcloud config set project ${PROJECT_ID}

gcloud auth configure-docker

# Option 1
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-fastapi \
  --gcs-source-staging-dir="gs://2025-cloudrun/staging"


gcloud run deploy hello-fastapi \
  --image gcr.io/${PROJECT_ID}/hello-fastapi \
  --region us-central1 \
  --platform managed \
  --no-allow-unauthenticated

# Option 2
gcloud builds submit --config cloudbuild.yaml \
  --gcs-source-staging-dir="gs://2025-cloudrun/staging"


# Option 3
export IMAGE_NAME=hello-fastapi
export PROJECT_ID=hello-world-418507

gcloud auth configure-docker

docker build -t ${IMAGE_NAME} .
docker tag ${IMAGE_NAME} gcr.io/${PROJECT_ID}/${IMAGE_NAME}
docker push gcr.io/${PROJECT_ID}/${IMAGE_NAME}

```

## Get URL
```bash
gcloud run services describe hello-fastapi \
  --region=us-central1 \
  --format='value(status.url)'
```

## Proxy
```bash
gcloud run services proxy hello-fastapi
```

## Test

```bash
curl https://hello-fastapi-671247654914.us-central1.run.app
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" https://hello-fastapi-671247654914.us-central1.run.app
```

## Delete
```bash
gcloud run services delete hello-fastapi
```

## Learning

- When ingress=internal, the following services can access cloud run endpoint
    - Compute engine (OK)
    - Cloud Shell (404 error, cant see endpoint)
