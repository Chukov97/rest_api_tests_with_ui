from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url: str = 'https://demowebshop.tricentis.com'
    driver_name: str = 'chrome'
    load_strategy: str = 'eager'
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 10.0


config = Config()
