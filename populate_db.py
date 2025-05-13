
import docx
import json

def populate_database():
    # Read the Word document
    doc = docx.Document('attached_assets/doctors and specialties.docx')
    
    # Get all paragraphs
    content = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    
    doctors_specialties = []
    doctors_started = False
    current_index = 0
    
    # Find where doctors section starts
    for i, line in enumerate(content):
        if line.lower().startswith('doctors:'):
            doctors_started = True
            current_index = i + 1
            break
    
    # Match doctors with specialties
    if doctors_started:
        doctors = []
        specialties = []
        
        # Split content into doctors and specialties
        for line in content[current_index:]:
            if not line:  # Skip empty lines
                continue
            if ':' in line:  # Skip headers
                continue
            if len(doctors) == 0:  # First column is doctors
                doctors.append(line.strip())
            else:  # Second column is specialties
                specialties.append(line.strip())
        
        # Create doctor-specialty pairs
        for i in range(min(len(doctors), len(specialties))):
            doctors_specialties.append({
                "doctor": doctors[i],
                "specialty": specialties[i]
            })
    
    # Save to JSON file
    with open('doctors_data.json', 'w') as f:
        json.dump({"doctors_specialties": doctors_specialties}, f, indent=2)
        
    print("JSON file created successfully!")

if __name__ == "__main__":
    populate_database()
