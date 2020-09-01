import os
from os.path import join, dirname
from dotenv import load_dotenv


env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)


CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')
CHROMEDRIVER_BINARY_PATH = os.environ.get('CHROMEDRIVER_BINARY_PATH')
WANTEDLY_ID = os.environ.get('WANTEDLY_ID')
WANTEDLY_PASSWORD = os.environ.get('WANTEDLY_PASSWORD')

