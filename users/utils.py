def user_directory_path(instance, filename): #created a this fuction with the name which will get intance and a filename as a prop
    return 'user_{0}/{1}'.format(instance.user.id, filename)  # this line of code will return a path to where the images should be placed
# so here the image was placed under a folder for the user, and then it should be the name of the actual user {0} followed by the name of the file {1}
# the .format() wil help us format strings in python which will help us write arguments to explain what each {} mean to us