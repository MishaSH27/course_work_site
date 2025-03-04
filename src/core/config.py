from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class Settings(BaseSettings):
    # model_config = SettingsConfigDict(
    #     env_file=(".env.template", ".env"),
    #     case_sensitive=False,
    #     env_nested_delimiter="__",
    #     env_prefix="APP_CONFIG__",
    # )
    run: RunConfig = RunConfig()
    # api_prefix: ApiPrefix = ApiPrefix()
    # db: DatabaseConfig
    # access_token: AccessToken
    # sqlal: SqlAlchemySettings


settings = Settings()
