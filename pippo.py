import json
import weasyprint

def create_pdf(data, filename):
    html_content = f"""
    <h1>{data['manufacturer']} {data['model']}</h1>
    <p><strong>Year:</strong> {data['year']}</p>
    <h2>Description:</h2>
    <p>{data['description']}</p>
    """
    weasyprint.HTML(string=html_content).write_pdf(filename)

def main():
    # Load JSON data
    with open('truck-models-json.json', 'r') as file:
        json_data = json.load(file)

    # Process each truck model
    for i, truck in enumerate(json_data['truckModels']):
        filename = f"output_{truck['manufacturer']}_{truck['model']}.pdf"
        create_pdf(truck, filename)

if __name__ == "__main__":
    main()