from models.ai_processor import process_text_gemini

def generate_er_diagram(user_input, complexity):
    """
    Generates a dynamic ER diagram using Gemini AI based on the complexity level.
    """
    structured_data = process_text_gemini(user_input, task="er_diagram", complexity=complexity)

    mermaid_code = "erDiagram\n"

    # ✅ Add entities
    for entity in structured_data["entities"]:
        mermaid_code += f"  {entity['name']} {{\n"
        for attr in entity["attributes"]:
            mermaid_code += f"    string {attr}\n"
        mermaid_code += "  }\n"

    # ✅ Add relationships
    for relation in structured_data["relationships"]:
        mermaid_code += f"  {relation['from']} ||--|| {relation['to']} : {relation['type']}\n"

    return mermaid_code
