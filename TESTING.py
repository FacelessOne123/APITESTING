from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_data():
    return {
        "id": 1,
        "message": {
            "array": ["P", "U", "T", "A", "N", "G", "I", "N", "A", "M", "O"],
            "hint": "bwakanangshit ka"
        }
    }
