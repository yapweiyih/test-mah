# Cloud Run Management Commands

## Delete Cloud Run Service

### Basic Delete Command
```bash
# Delete a Cloud Run service
gcloud run services delete SERVICE_NAME --region=REGION
```

### For your specific service (hello-fastapi-2)
```bash
# Delete the hello-fastapi-2 service in us-central1
gcloud run services delete hello-fastapi-2 --region=us-central1
```

### Delete with automatic confirmation (no prompt)
```bash
# Add --quiet flag to skip confirmation prompt
gcloud run services delete hello-fastapi-2 --region=us-central1 --quiet
```

## List Cloud Run Services

### List all services in a region
```bash
# List services in specific region
gcloud run services list --region=us-central1

# List services in all regions
gcloud run services list
```

## Other Useful Cloud Run Commands

### Describe a service
```bash
gcloud run services describe hello-fastapi-2 --region=us-central1
```

### Update traffic allocation
```bash
# Send all traffic to latest revision
gcloud run services update-traffic hello-fastapi-2 --to-latest --region=us-central1
```

### Get service URL
```bash
gcloud run services describe hello-fastapi-2 --region=us-central1 --format='value(status.url)'
```

### Delete multiple services at once
```bash
# Delete multiple services
for service in hello-fastapi hello-fastapi-2; do
  gcloud run services delete $service --region=us-central1 --quiet
done
```

## Important Notes

1. **Region is required**: Always specify the `--region` flag when deleting services
2. **Confirmation prompt**: By default, gcloud will ask for confirmation. Use `--quiet` to skip
3. **Permissions**: You need the `run.services.delete` permission to delete services
4. **Irreversible**: Deleting a service is permanent and cannot be undone
