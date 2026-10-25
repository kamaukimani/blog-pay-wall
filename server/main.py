from app import create_app 

app=create_app()

@app.route('/')
def index():
    return {"message":"Welcome to Blog-Pay-Wall API"},200


if __name__=="__main__":
    app.run(port=5555,debug=True)