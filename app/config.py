from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    nvidia_api_key: str = Field(default="", alias="NVIDIA_API_KEY")
    nvidia_base_url: str = Field(default="https://integrate.api.nvidia.com/v1", alias="NVIDIA_BASE_URL")
    nvidia_model: str = Field(default="nvidia/llama-3.1-nemotron-70b-instruct", alias="NVIDIA_MODEL")

    canvas_base_url: str = Field(default="https://menlo.instructure.com", alias="CANVAS_BASE_URL")
    canvas_api_token: str = Field(default="", alias="CANVAS_API_TOKEN")
    canvas_course_id: str = Field(default="", alias="CANVAS_COURSE_ID")
    use_mock_canvas: bool = Field(default=True, alias="USE_MOCK_CANVAS")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
