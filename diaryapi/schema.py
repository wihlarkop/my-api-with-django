from pydantic import BaseModel, validator


class DiaryPostSchema(BaseModel):
    title: str
    content: str

    @validator('title')
    def validate_title(cls, v):
        if v == '' or None:
            raise ValueError('Title is required')

        return v

    @validator('content')
    def validate_content(cls, v):
        if v == '' or None:
            raise ValueError('Content is required')

        return v
