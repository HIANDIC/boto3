import boto3

s3 = boto3.resource('s3')

data = open("test.txt", "rb")

s3.Bucket("halil-boto3-bucket").put_object(Key="test.txt", Body=data)

