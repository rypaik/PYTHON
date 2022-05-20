import os
from dotenv import load_dotenv


# TODO: test in jupyter lab... jupyter lab uses differ 
# %load_ext dotenv
# %dotenv relative/or/absolute/path/to/.env
# -o to override , -v for verbose


# dotenv_path = join(dirname(__file__), '.env')
#load_dotenv(dotenv_path)
load_dotenv()
mysql_db = os.environ.get("MYSQL_DATABASE_DB")
print(mysql_db)
print(type(mysql_db))
