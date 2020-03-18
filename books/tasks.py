import os
from time import gmtime, strftime

import boto3
from celery import shared_task

client = boto3.client('s3',
                      aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                      aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
                      )

time = strftime('%Y%m%d%H%M%S', gmtime())
bucket_name = os.environ.get('AWS_S3_BUCKET_NAME')


@shared_task
def upload_cover_to_s3(cover_path, book_title_slug):
    file_name = cover_path.split('/')
    file_name = '{}/{}/{}'.format(time, book_title_slug, file_name[-1])
    print(file_name)
