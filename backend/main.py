from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from diagram_generators.class_diagram import generate_class_diagram
from diagram_generators.er_diagram import generate_er_diagram

# ✅ Load environment variables
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("🚨 ERROR: Google Gemini API Key is missing! Add it to backend/.env")

app = FastAPI()

# ✅ Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define Request Models
class DiagramRequest(BaseModel):
    text: str
    diagram_type: str  # "class" or "er"
    complexity: str  # "basic", "intermediate", "advanced"

# ✅ Add a default root endpoint to prevent 404 errors on "/"
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Diagram Generator API!"}

@app.post("/generate-diagram")
def generate_diagram(request: DiagramRequest):
    """
    Generates a diagram based on user input with selected complexity level.
    """
    if request.diagram_type == "er":
        mermaid_code = generate_er_diagram(request.text, request.complexity)
    else:
        mermaid_code = generate_class_diagram(request.text, request.complexity)

    return {"diagram": mermaid_code}
