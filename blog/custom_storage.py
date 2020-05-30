from storages.backends.s3boto3 import S3Boto3Storage


class PublicImageStorage(S3Boto3Storage):
    bucket_name = "post-images"
    custom_domain = "{}.s3.amazonaws.com".format(bucket_name)


class MediaStorage(S3Boto3Storage):
    bucket_name = "post-images"
    custom_domain = "{}.s3.amazonaws.com".format(bucket_name)


class StaticStorage(S3Boto3Storage):
    bucket_name = "eduzen-bucket"
    location = "static"
