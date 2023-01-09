from fastapi import FastAPI

app = FastAPI('Referral System')


#add root route
@app.get('/')
async def root():
    return {'message':'Welcome to the referral system'}