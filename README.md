
```bash
export PROJECT_ID=hello-world-418507
gcloud config set project ${PROJECT_ID}

# Option 1
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-fastapi
gcloud run deploy hello-fastapi \
  --image gcr.io/${PROJECT_ID}/hello-fastapi \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated


# Option 2
gcloud builds submit --config cloudbuild.yaml

```