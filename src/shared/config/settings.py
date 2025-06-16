from pydantic_settings import BaseSettings  

class Settings(BaseSettings):

    #Para la conexión a la base de datos
    DATABASE_URL: str
    
    DATABASE_SERVER: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    
    #Para la configuración de seguridad y autenticación
    SECURITY_SECRET_KEY: str
    SECURITY_ALGORITHM: str
    TOKEN_EXPIRE_MINUTES: int
    
    BACKEND_HOST: str
    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()