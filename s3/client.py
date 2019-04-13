import boto3


class S3(object):

    def __init__(self):
        # boto3.resource is more a high level service access, whereas boto3.client is a low level service access
        # you can still access the client from the resource through resource.meta.client
        self.resource = boto3.resource('s3')
        self.session = boto3.session.Session()

    def make_bucket(self, name, region=None, enable_versioning=False):
        """Creates a new bucket in the specified region. If the region
        is not provided, the default region on the session will be used.

        Args:
            name (str): name of the bucket to create
            region (str): where to create the bucket
            enable_versioning (bool): if enabled, then multiple versions of one file
                can be stored.

        Returns:
            boto3.resources.factory.s3.Bucket
        """
        if region is None:
            region = self.session.region_name
        bucket_config = {'LocationConstraint': region}
        bucket = self.resource.create_bucket(Bucket=name, CreateBucketConfiguration=bucket_config)
        if enable_versioning:
            versioning_bucket = self.resource.BucketVersioning(name)
            versioning_bucket.enable()
        return bucket

    def remove_bucket(self, name):
        """Delete a bucket.

        Args:
            name (str):
        """
        self.resource.meta.client.delete_bucket(Bucket=name)

    def list_buckets(self):
        self.client.list_buckets()
