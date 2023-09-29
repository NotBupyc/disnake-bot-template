from db.create_tables import init_models
from config import PATH_TO_DB
import asyncio

if __name__ == '__main__':
    asyncio.run(init_models(PATH_TO_DB))