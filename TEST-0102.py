from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_data():
    return {
        "id" : 1,
        "Riddle": {
            "Quote" : ["I am a vow made in freezing waters", "a promise never to let go of a memory or a love", "even as the depths pull one of us down." ],
            "Hint" : "A massive ship, an iceberg, and a door that probably had room for two people.",
            "Reward" : "A magic poop of a dog"

        }
    
    }