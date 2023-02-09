import os
import yaml
from utilities.baseUtility import BaseUtility

if os.path.exists(BaseUtility().ROOT_PATH + "/yml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()
    CONFIG = yaml.safe_load(open(BaseUtility().ROOT_PATH + "/yml/config.yml", 'r'))
else:
    raise "config.yml does not exists"

application_urls = (CONFIG['application_urls'])
