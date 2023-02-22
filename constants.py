import os
from dotenv import load_dotenv

load_dotenv()  # loads environment variables from .env file

## Database
DB_NAME = "default"
TABLE_NAME = "avocado_updated_2020"

SERVER_HOSTNAME = "adb-1258203080515991.11.azuredatabricks.net"
HTTP_PATH = "/sql/1.0/warehouses/6e12cf448c9e0bea"
ACCESS_TOKEN = "dapi72645641356b3912294e9e58fb3c02e8-2"