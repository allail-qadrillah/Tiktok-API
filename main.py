from fastapi import FastAPI, Query, HTTPException
import uvicorn
from Tiktok import getUrl

app = FastAPI()

@app.get('/')
def main():
  return {'/Tiktok?url=':{
           'status' : "bool",
           'message' : "string",
            'data' : [
              {"Without watermark" : "https:...",
               "Without watermark [2]" : "https:...",
               "Without watermark [3]" : "https:...",
               "Without watermark [4]" : "https:...",
               "Download MP3" : "https:..."
              }
            ]
        }}

@app.get('/Tiktok')
async def Tiktok(url: str = Query("url")):
          try:
            response = getUrl(url)
            return response
            
          except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
            
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)




