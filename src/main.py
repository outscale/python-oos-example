import os
import string
import random
import sys
import boto3
from botocore.client import ClientError

# This is a small example of using Outscale Object Storage using Boto3 library
#
# Check boto3 documentation regarding s3 actions for more details
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client
def demo():
    try:
        s3 = s3_client()
        bucket_name = "bucket-test-" + random_name(4)
        print("creating private bucket named %s..." % bucket_name)
        s3.create_bucket(ACL='private', Bucket=bucket_name)
        print("bucket %s created" % bucket_name)

        object_name = "my-data"
        print("writing 'Hello World' to public %s object..." % object_name)
        s3.put_object(ACL='public-read', Body=b'Hello World', Bucket=bucket_name, Key=object_name)
        print("writed to %s object" % bucket_name)

        print("reading %s object..." % object_name)
        obj = s3.get_object(Bucket=bucket_name, Key=object_name)
        print("read object ok: %s" % obj['Body'].read())

        print("deleting %s object..." % object_name)
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print("deleted %s object" % object_name)

        print("deleting bucket named %s..." % bucket_name)
        bucket = s3.delete_bucket(Bucket=bucket_name)
        print("bucket %s deleted" % bucket_name)
    except ClientError as error:
        print(error, file=sys.stderr)
        sys.exit(1)

def s3_client():
    access_key = os.environ['OSC_ACCESS_KEY']
    secret_key = os.environ['OSC_SECRET_KEY']
    region = os.environ['OSC_REGION']
    endpoint = 'https://oos.%s.outscale.com' % region
    s3_client = boto3.client(service_name='s3', region_name=region, use_ssl=True, endpoint_url=endpoint, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    return s3_client

def random_name(size):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(size))
    return name

if __name__ == "__main__":
    demo()