from dotenv import load_dotenv
load_dotenv()

from typing import Optional, List
from fastapi import FastAPI, Query
from enum import Enum
import os
import uvicorn

import thpost


app = FastAPI()


class Courier(str, Enum):
    thpost = "thpost"


@app.get("/")
def read_root():
    return "order tracking works"


@app.get("/trackbybarcodes/{courier}")
def thpost_track_by_barcodes(courier: Courier, barcodes: List[str] = Query(...)):
    if courier == Courier.thpost:
        return thpost.track_by_barcodes(barcodes)


if __name__ == "__main__":
    uvicorn.run("main:app", port=3003, reload=True)
