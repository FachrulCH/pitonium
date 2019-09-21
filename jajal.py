from configs import env

print(env.get('ANDROID_HOME'))
print(env.get('sesuatu', 'aduh gada sesuatu'))
print(env.get('ANDROID_DEVICE_NAME'))