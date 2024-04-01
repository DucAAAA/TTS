import boto3

aws_access_key_id = 'DO00XMARRJU8BPPFTY3U'
aws_secret_access_key = '8g+7oI4V4zIR6v1QIUY8+2p2EnN7TtUvb9xW0ogYTN4'
region_name = 'nyc3'
s3 = boto3.client(
    's3',
    endpoint_url='https://nyc3.digitaloceanspaces.com',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

def upload_file(file_path, bucket_name, key):
    s3.upload_file(file_path, bucket_name, key, ExtraArgs={'ACL': 'public-read'})