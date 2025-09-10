# Fix for gcloud builds submit Error

## Problem
The error `wrong collection: expected [storage.buckets], got [storage.objects]` occurs because the `--gcs-source-staging-dir` parameter is not correctly formatted or the bucket doesn't exist.

## Solutions

### Solution 1: Create the bucket first (if it doesn't exist)
```bash
# Create the bucket
gsutil mb gs://2025-cloudrun

# Then run the build command
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-fastapi \
  --gcs-source-staging-dir="gs://2025-cloudrun/staging"
```

### Solution 2: Use a different staging directory format
```bash
# Option A: Add a subdirectory path
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-fastapi \
  --gcs-source-staging-dir="gs://2025-cloudrun/builds"

# Option B: Use a different bucket that already exists
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-fastapi \
  --gcs-source-staging-dir="gs://${PROJECT_ID}_cloudbuild/source"
```

### Solution 3: Use cloudbuild.yaml directly (recommended)
Since you have a cloudbuild.yaml file, you can use it directly without specifying the tag:

```bash
# This will use the cloudbuild.yaml configuration
gcloud builds submit --gcs-source-staging-dir="gs://2025-cloudrun/staging"
```

Or even simpler, let Cloud Build create its own staging bucket:

```bash
# Cloud Build will automatically create and use a default bucket
gcloud builds submit
```

## Important Notes

1. **Image name mismatch**: Your command line uses `hello-fastapi` but cloudbuild.yaml uses `hello-fastapi-2`. Make sure these match or update one of them.

2. **Bucket permissions**: Ensure your service account has the necessary permissions to write to the bucket:
```bash
# Grant Cloud Build service account storage admin permissions
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member="serviceAccount:${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  --role="roles/storage.admin"
```

3. **Check if bucket exists**:
```bash
gsutil ls gs://2025-cloudrun
```

## Recommended Fix

The simplest solution is to let Cloud Build handle the staging automatically:

```bash
# This will use cloudbuild.yaml and auto-create staging bucket
gcloud builds submit
```

This command will:
- Use your cloudbuild.yaml configuration
- Automatically create a staging bucket if needed
- Build and push the image as defined in cloudbuild.yaml
- Deploy to Cloud Run as specified
