import os
from dotenv import load_dotenv
from model_data.auth_model import Credentials

load_dotenv()
VALID_CREDENTIALS = Credentials(Email=os.getenv('LOGIN'), Password=os.getenv('PASSWORD'))
