import os
#PATHS#
data_path = os.path.join(os.getcwd(), 'data')
texts_path = os.path.join(data_path, 'texts')
patch_path = os.path.join(data_path, 'patch')
users_path = os.path.join(data_path, 'users')
programs_path = os.path.join(data_path, 'programs')
admins_path = os.path.join(users_path, 'admins')
error_messages_path = os.path.join(data_path, 'error_messages')
last_access_path = os.path.join(users_path, 'last_access')
personalization_path = os.path.join(data_path, 'personalization')