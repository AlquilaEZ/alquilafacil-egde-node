from pydantic_settings import BaseSettings  

class Settings(BaseSettings):

    #Para la configuración de seguridad y autenticación


    BACKEND_API_BASE_URL: str
    TOKEN_EXPIRATION_SECONDS: int
    AUTHENTICATION_EMAIL: str
    AUTHENTICATION_PASSWORD: str
    LOCAL_ID: int


    
    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()