import boto3

# use Amazon S3
client = boto3.client('s3')

# delete a bucket
bucket_name = 'halil-boto3-bucket'
response = client.delete_bucket(Bucket=bucket_name)

# listing buckets
response2 = client.list_buckets()
for bucket in response2['Buckets']:
    print(bucket['Name'])

