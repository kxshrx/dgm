from models.ai_processor import process_text_gemini

def generate_class_diagram(user_input, complexity):
    """
    Generates a dynamic Class diagram using Gemini AI based on complexity level.
    """
    structured_data = process_text_gemini(user_input, task="class_diagram", complexity=complexity)

    mermaid_code = "classDiagram\n"

    # ✅ Add classes
    for entity in structured_data["entities"]:
        mermaid_code += f"  class {entity['name']} {{\n"
        for attr in entity["attributes"]:
            mermaid_code += f"    +{attr}\n"
        mermaid_code += "  }\n"

    # ✅ Add relationships
    for relation in structured_data["relationships"]:
        mermaid_code += f"  {relation['from']} --> {relation['to']} : {relation['type']}\n"

    return mermaid_code
