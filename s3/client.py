import boto3
import logging


class S3(object):

    def __init__(self):
        # boto3.resource is more a high level service access, whereas boto3.client is a low level service access
        self.client = boto3.client('s3')

    def make_bucket(self):
        pass

    def remove_bucket(self):
        pass

    def list_buckets(self):
        self.client.list_buckets()
