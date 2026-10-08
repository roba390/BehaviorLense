from fastapi import FastAPI

app = FastAPI(title="Signal API", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Signal API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}