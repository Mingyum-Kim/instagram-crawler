from fastapi import FastAPI

app = FastAPI(title="Instagram Organizer API", version="0.1.0")


@app.get("/")
def root():
    return {"service": "instagram-organizer-api", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "ok"}
