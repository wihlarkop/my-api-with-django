def user_directory_path_media(instance, filename):
    return f'user_{instance.user.username}/{filename}'
