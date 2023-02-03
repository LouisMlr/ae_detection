from pydantic import BaseSettings, BaseModel

class Settings(BaseSettings):
    OPENAI_API_KEY: str

# specify .env file location as Config attribute
    class Config:
        env_file = ".env"

class EntitiesOut(BaseModel):
    input_text: str
    entities: str
