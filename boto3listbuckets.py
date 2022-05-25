import boto3

#Check and list existing S3 bucket(s)
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)