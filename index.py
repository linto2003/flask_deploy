from flask import Flask,request
from flask_smorest import abort
from ocr import Ocr
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.post("/get-ocr")
def send_ocr_res():
    req_data=request.get_json()
    try:
        
        url=req_data['url']
        ocr=Ocr.get_ocr(url)
        return {"message":ocr}
    except:
        return {"message":"error"}


@app.get("/get-ocr")
def hello():
    return {"message":"hoi"}


if __name__== '__main__':
    from pyngrok import ngrok
    port = 5000
    public_url = ngrok.connect(port, bind_tls=True).public_url
    print(public_url+'/get-ocr')

    app.run(port=port)
