from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from  ...config.settings import settings
from .Base import Base


class DatabaseConnection:
    _instance = None #Atributo de clase, lo que significa que es compartido por todas las instancias de la clase
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.__initialized()
        return cls._instance
    
    def __initialized(self):
         
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_SERVER}/{settings.DATABASE_NAME}",
            pool_size=5,
            max_overflow=15,
            pool_timeout=30,
            pool_pre_ping=True,     
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )
        

        
        print("Connected to database")
        

    
    async def init_models(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
 
    
db = DatabaseConnection()