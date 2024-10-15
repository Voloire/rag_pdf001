import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame

def create_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    styles = getSampleStyleSheet()
    
    # Set up the frame
    frame = Frame(50, 50, width - 100, height - 100, showBoundary=0)
    
    story = []
    
    # Add manufacturer and model as title
    title = f"{data['manufacturer']} {data['model']}"
    story.append(Paragraph(title, styles['Title']))
    
    # Add year
    story.append(Paragraph(f"Year: {data['year']}", styles['Normal']))
    
    # Add description
    story.append(Paragraph("Description:", styles['Heading2']))
    story.append(Paragraph(data['description'], styles['Normal']))
    
    # Draw the story
    frame.addFromList(story, c)
    
    c.save()
    print(f"Created PDF: {filename}")

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