def user_directory_path_media(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
