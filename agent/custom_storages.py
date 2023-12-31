from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage


    class MediaStorage(FileSystemStorage):
        # location = settings.MEDIA_LOCATION
        file_overwrite = False
        default_acl = 'public-read'

else:
    from storages.backends.s3boto3 import S3Boto3Storage


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIA_LOCATION
        file_overwrite = False
        default_acl = 'public-read'
