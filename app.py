from decouple import Config, Csv

config = Config()

SECRET_KEY = config.get('SECRET_KEY')
API_KEY = config.get('API_KEY')
DEBUG = config.getboolean('DEBUG')

print("SECRET_KEY:", SECRET_KEY)
print("API_KEY:", API_KEY)
print("DEBUG:", DEBUG)

