from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="IT Asset Management API", version="2.0")

class Asset(BaseModel):
    id: int
    device_type: str
    model: str
    status: str


inventory = [
    {"id": 1, "device_type": "Laptop", "model": "Dell XPS 15", "status": "Active"},
    {"id": 2, "device_type": "Router", "model": "Cisco Catalyst 9000", "status": "In Storage"}
]




@app.get("/")
def home():
    return {"message": "Welcome to the IT Asset Management System"}


@app.get("/assets")
def get_all_assets():
    return {"total_assets": len(inventory), "data": inventory}


@app.get("/assets/{asset_id}")
def get_asset_by_id(asset_id: int):
    for item in inventory:
        if item["id"] == asset_id:
            return item
    
    raise HTTPException(status_code=404, detail="Asset not found")


@app.post("/assets", status_code=201)
def add_new_asset(new_asset: Asset):
    
    inventory.append(new_asset.dict())
    return {"message": "New IT asset successfully added!", "added_asset": new_asset}