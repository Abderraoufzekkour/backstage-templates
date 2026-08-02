from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Service": "${{ values.name }}", "Status": "Running via GitOps!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
