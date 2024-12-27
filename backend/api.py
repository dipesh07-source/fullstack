from fastapi import FastAPI
from fastapi.responses import FileResponse
# Create a FastAPI app instance
app = FastAPI()

# Define a route that returns a string
@app.get("/facebook/profile")
def profile():
    return "profile"

@app.get("/facebook/chat")
def chat():
    return "chat"

                    
@app.get("/add")
def add(a:int,b:int):
    return(a+b)                                                                            

@app.get("/getname")
def getname(name:str,cast:str):
    return(name+" "+cast)
    

@app.get("/image")
def image():
    path= "2019.jpg"
    return FileResponse(path) 
    

@app.get("/music")
def music():
    path= "me.mp3"
    

    return FileResponse(path, media_type="audio/mpeg", headers={"Content-Disposition": "inline; filename=file.mp3"})
