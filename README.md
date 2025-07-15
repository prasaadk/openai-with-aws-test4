# OpenAI with AWS Test 4

This example uses Terraform to create an S3 bucket, Lambda function and API Gateway. GitHub Actions deploys the Terraform configuration using an AWS role.

## Terraform
- Creates an S3 bucket `ontoscale-create-with-openai-codex`.
- Packages a Python Lambda that writes a file into the bucket and exposes it via HTTP API Gateway.
- Remote state is stored in `ontoscale-terraform-backend` S3 bucket.

## GitHub Actions
- `deploy.yml` runs `terraform apply` on pushes to `main` (i.e. after PR merge).
- `destroy.yml` can be triggered manually to teardown the resources.
- Both workflows use `AWS_ROLE` secret for OIDC access.
