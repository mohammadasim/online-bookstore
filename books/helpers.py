import os
from time import gmtime, strftime

import boto3
from django.utils.deconstruct import deconstructible


@deconstructible
class UniqueFilePath(object):
    """
    A class to create unique file name for
    the file that is uploaded and stored in s3 bucket
    """

    def __call__(self, slug, filename):
        time = strftime('%Y%m%d', gmtime())
        return '{}/{}/{}'.format(time, slug, filename)


def create_boto3_client(aws_resource_name: str) -> boto3.client:
    """
    A helper function that will return a boto3 client
    for the AWS resources provided as input
    """
    client = boto3.client(
        aws_resource_name,
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
    )
    return client
