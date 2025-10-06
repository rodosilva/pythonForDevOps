import boto3

# Create an S3 client
s3 = boto.client('s3')

# List all the buckets
buckets = s3.list_buckets()

# Print all the Buckets
for i in buckets["Buckets"]:
    print(i["Name"])


