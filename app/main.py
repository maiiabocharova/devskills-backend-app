from fastapi import FastAPI, HTTPException
from databases import Database
import aiohttp
import uvicorn

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

from send_request import send_request
from model import credits_table

database = Database('sqlite:///credit.db')
app = FastAPI()

@app.on_event("startup")
async def startup():
    global session
    session = aiohttp.ClientSession()
    # connect to db and create a session when the application is starting
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # disconnect from db and close the session upon closing the application
    await database.disconnect()
    await session.close()


@app.get("/ping")
def ping():
    return {
        "description": "The service is up and running."
    }


@app.get("/credit-data/{ssn}")
async def aggregate_data(ssn: str):
    # check if person already in db
    print(ssn)
    query = f"SELECT * FROM credits WHERE ssn='{ssn}'"
    query_result = await database.fetch_one(query=query)

    if not query_result:
        data = await send_request(ssn=ssn, session=session)
        if data:
            query = credits_table.insert()
            data['ssn'] = ssn
            await database.execute(query=query, values=data)
            del data['ssn']
            return data
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    else:
        return {
            "first_name": query_result["first_name"],
            "last_name": query_result["last_name"],
            "address": query_result["address"],
            "assessed_income": query_result["assessed_income"],
            "balance_of_debt": query_result["balance_of_debt"],
            "complaints": bool(query_result["complaints"])
        }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)