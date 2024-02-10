from fastapi import FastAPI



app=FastAPI()

food_items = {
    'indian':["samosa", "Dosa"],
    'american':["Hot Dog", "Apple Pie"],
    'italiana':["Ravioli","Pizza"]
}

@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine)