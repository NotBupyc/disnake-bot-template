from .models import Base
from sqlalchemy.ext.asyncio import create_async_engine

async def init_models(db_name: str = "db.db"):
    """Delete and create tables"""
    engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
