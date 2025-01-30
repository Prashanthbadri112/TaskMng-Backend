import pusher
#from pusher.aiohttp import AsyncIOBackend
from dotenv import load_dotenv
import os

load_dotenv()
pusher_client = pusher.Pusher(
  app_id=os.getenv("APP_ID"),
  key=os.getenv("KEY"),
  secret=os.getenv("SECRECT"),
  cluster=os.getenv("CLUSTER"),
  ssl=True,
  #backend=AsyncIOBackend
)