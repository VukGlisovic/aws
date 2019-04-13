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
        """Lists the names of all buckets.

        Returns:
            list
        """
        response = self.resource.meta.client.list_buckets()
        bucket_names = [b['Name'] for b in response['Buckets']]
        return bucket_names

    def upload_to_bucket_from_file(self, bucket_name, s3_path, filename):
        """Upload a local file to an s3 bucket.

        Args:
            bucket_name (str): the bucket where to upload to
            s3_path (str): path within the bucket to upload to
            filename (str): local file path indicating the file to upload
        """
        bucket = self.resource.Bucket(name=bucket_name)
        bucket.upload_file(Filename=filename, Key=s3_path)

    def download_file(self, bucket_name, s3_path, filename):
        """Downloads file from an s3 bucket.

        Args:
            bucket_name (str):
            s3_path (str):
            filename (str):
        """
        bucket = self.resource.Bucket(name=bucket_name)
        bucket.download_file(Filename=filename, Key=s3_path)

    def delete_object(self, bucket_name, s3_path):
        """Deletes a file (object) from an s3 bucket.

        Args:
            bucket_name (str): bucket name
            s3_path (str): file path to delete in the bucket
        """
        self.resource.Object(bucket_name, s3_path).delete()
