import datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from jobs.load import load_sales_data
from jobs.transform import transform_sales_data


job1 = FastAPI(description="JSON load job")
job2 = FastAPI(description="AVRO transformation job")


class JSONJobRequest(BaseModel):
    date: datetime.date
    raw_dir: str
    total: Optional[bool] = False


class AVROJobRequest(BaseModel):
    raw_dir: str
    stg_dir: str


@job1.post("/", status_code=201)
async def load(body: JSONJobRequest):
    load_sales_data(sales_date=body.date, raw_dir=body.raw_dir, total=body.total)
    return {"hello": "World!"}


@job2.post("/")
async def transform(body: AVROJobRequest):
    transform_sales_data(source_path=body.raw_dir, dest_path=body.stg_dir)
    return {"hello": "world"}
