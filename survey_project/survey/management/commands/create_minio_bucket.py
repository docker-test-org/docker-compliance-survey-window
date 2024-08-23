import boto3
from botocore.exceptions import ClientError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a MinIO bucket if it does not exist'

    def handle(self, *args, **kwargs):
        self.create_minio_bucket()

    def create_minio_bucket(self):
        s3 = boto3.client(
            's3',
            endpoint_url='http://minio:9000',  # 이 주소가 MinIO 컨테이너의 주소임
            aws_access_key_id='minioadmin',
            aws_secret_access_key='minioadmin',
        )
        try:
            s3.head_bucket(Bucket='mybucket')
            self.stdout.write(self.style.SUCCESS('Bucket already exists.'))
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                s3.create_bucket(Bucket='mybucket')
                self.stdout.write(self.style.SUCCESS('Bucket created successfully.'))
            else:
                self.stdout.write(self.style.ERROR('Failed to create bucket: {}'.format(e)))

