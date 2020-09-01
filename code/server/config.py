import os
from os.path import join, dirname
from dotenv import load_dotenv


env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)


CHROMEDRIVER = os.environ.get('CHROMEDRIVER')
CHROMEDRIVER_BINARY = os.environ.get('CHROMEDRIVER_BINARY')
WANTEDLY_ID = os.environ.get('WANTEDLY_ID')
WANTEDLY_PASSWORD = os.environ.get('WANTEDLY_PASSWORD')

