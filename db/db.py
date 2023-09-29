import typing

from sqlalchemy import (
    select, 
    and_, 
    update)

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from disnake import (
    Member as DisnakeMember, 
    User as DisnakeUser, 
    Guild as DisnakeGuild)

from .models import (
    Base,
    Guild,
    User)


class GuildDb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_server(self, server: DisnakeGuild) -> None:
        """Add server in db"""
        async with self.session() as s:
            guild = Guild(
                guild_id=server.id)
            
            s.add(guild)
            await s.commit()

    async def delete_server(self, server_id: int) -> None:
        """Delete server from db"""
        async with self.session() as s:
            q = select(Guild).where(Guild. guild_id == server_id)
            guild = (await s.execute(q)).scalar()
            # user = user.scalar()
            s.delete(guild)
            await s.commit()

    async def get_server(self, server_id: int) -> typing.Optional[Guild]:
        """Get server info from db"""
        async with self.session() as s:
            q = select(Guild).where(Guild.guild_id == server_id)
            guild = await s.execute(q)
            try:
                return guild.fetchone()[0]
            except TypeError:
                return None


class UserBd:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )
    async def create_user(self, user: typing.Union[DisnakeMember, DisnakeUser]) -> None:
        """Add user in db"""
        async with self.session() as s:
           
            us = User(
                user_id=user.id,
                username=user.name,
                )
            s.add(us)
            await s.commit()

    async def delete_user(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.session() as s:
            q = select(User).where(User.user_id == user_id)
            
            us = (s.execute(q)).scalar()
            # user = user.scalar()
            s.delete(us)
            await s.commit()

    async def get_user(self, user_id: int) -> typing.Optional[User]:
        """Get info a user from db"""
        async with self.session(expire_on_commit=False) as s:
            q = select(User).where(User.user_id == user_id)
            
            us = await s.execute(q)
            try:
                return us.fetchone()[0]
            except TypeError:
                return None
        
