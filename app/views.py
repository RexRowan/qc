from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

sections = [
    ("So you have heard of quantum technology and how it is going to revolutionize, well, everything. How do we know that and how does it work? Jump in here to find out!", "qc.png"),
    ("This skill introduces the superposition principle. You'll gain insight into where this principle comes from, why it is necessary, and what you can do with it.", "superposition.jpg"),
    ("Start with some fundamentals in how we represent information and by the end of this skill you'll understand how we can encode and process information using quantum physics!", "qubits.jpg"),
    ("Measurement the destructor. What does it mean to measure something in general? What does it mean to measure something in quantum physics? Discover the dirty secrets about measurement in quantum computing.", "measurement.png"),
    ("How do we represent the programs to be run on quantum computers? After this skill you'll be able to decipher some of the cool diagrams you see in the field.", "circuit.png"),
    ("Einstein called it 'spooky action at a distance.' It's not so spooky, but it may be extremely useful! Discover the most quintessential concept in quantum physics.", "entanglement.jpg"),
    ("Why don't we have useful quantum computers yet? Learn what's holding us back through an understanding of how noise and interference affect quantum computers.", "noise.jpg"),
    ("Learn all about quantum control and how it is used to create quantum gates and combat noise.", "control.jpg"),
    ("Are you ready for the trenches? Begin to get to grips with the challenges of programming a real quantum computer.", "program.jpg")
]

def section(request, num):
    # Ensure num is an integer and within the range of the sections list
    if 1 <= num <= len(sections):
        # Get the text and image filename for the given section
        text, image_filename = sections[num - 1]
        image_path = os.path.join(settings.STATIC_URL, 'images', image_filename)
        # Create the full response with text and image path
        response_content = f"<img src='{image_path}' alt='Section Image' class='section-image'><p>{text}</p>"
        return HttpResponse(response_content)
    else:
        # If num is out of range, raise a 404 error
        raise Http404("No such section")
