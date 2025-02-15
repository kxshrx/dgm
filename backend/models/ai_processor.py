import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("🚨 ERROR: Google Gemini API Key is missing! Add it to backend/.env")

genai.configure(api_key=GEMINI_API_KEY)

def process_text_gemini(user_input, task="general", complexity="basic"):
    """
    Uses Google Gemini AI to process user input and return structured data.
    
    - `task="class_diagram"`: Extracts class diagram details.
    - `task="er_diagram"`: Extracts ER diagram details.
    - `complexity`: "basic", "intermediate", or "advanced".
    """

    prompt = f"""
    Task: {task}
    Complexity Level: {complexity}

    Process the following user input and return structured data:
    "{user_input}"

    Expected Output:
    If `task="class_diagram"`, return:
    {{
      "entities": [
        {{"name": "Class1", "attributes": ["attr1", "attr2"]}},
        {{"name": "Class2", "attributes": ["attr1", "attr2"]}}
      ],
      "relationships": [
        {{"from": "Class1", "to": "Class2", "type": "inherits/composes/etc."}}
      ]
    }}

    If `task="er_diagram"`, return:
    {{
      "entities": [
        {{"name": "Entity1", "attributes": ["attr1", "attr2"]}},
        {{"name": "Entity2", "attributes": ["attr1", "attr2"]}}
      ],
      "relationships": [
        {{"from": "Entity1", "to": "Entity2", "type": "relationship_name"}}
      ]
    }}

    - For **Basic**, include **only essential entities and attributes**.
    - For **Intermediate**, add **more attributes and relationships**.
    - For **Advanced**, include **all possible attributes, constraints, optional fields**.
    """

    model = genai.GenerativeModel("gemini-pro")
    
    response = model.generate_content(prompt)
    
    try:
        structured_data = json.loads(response.text)  # Convert response to JSON
        return structured_data
    except json.JSONDecodeError:
        print("🚨 ERROR: AI response is not in valid JSON format.")
        return {"entities": [], "relationships": []}
