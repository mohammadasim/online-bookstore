from celery import shared_task

from .helpers import create_boto3_client


@shared_task
def delete_object_from_s3(bucket_name: str, object_name: str):
    client = create_boto3_client('s3')
    response = client.delete_object(
        Bucket=bucket_name,
        Key=object_name)
    return response
