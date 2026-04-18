from django.core.management.base import BaseCommand
from academics.models import Professor


PROFESSORS = [
    {
        "name": "Shruti Shantiling Phutke",
        "designation": "Assistant Professor",
        "research_interests": "Artificial Intelligence, Machine Learning, Deep Learning, Computer Vision for Healthcare, Agriculture, Medical Image Analysis, EEG Signal Processing, Image and Video Inpainting, Underwater and Aerial Image Enhancement",
        "degree": "PhD, IIT Ropar, India",
        "email": "ssphutke@iitg.ac.in",
        "phone": "+91-361-258-2301",
    },
    {
        "name": "Arijit Sur",
        "designation": "Associate Professor",
        "research_interests": "Multimedia Security, Digital Watermarking, Steganography, Computer Vision, Image Processing",
        "degree": "PhD, IIT Kharagpur, India",
        "email": "arijit@iitg.ac.in",
        "phone": "+91-361-258-2302",
    },
    {
        "name": "Prithwijit Guha",
        "designation": "Associate Professor",
        "research_interests": "Computer Vision, Video Surveillance, Human Activity Recognition, Object Detection and Tracking",
        "degree": "PhD, IIT Kharagpur, India",
        "email": "pguha@iitg.ac.in",
        "phone": "+91-361-258-2303",
    },
    {
        "name": "Bhogeswar Borah",
        "designation": "Professor",
        "research_interests": "Data Mining, Machine Learning, Pattern Recognition, Bioinformatics, Natural Language Processing",
        "degree": "PhD, Gauhati University, India",
        "email": "bborah@iitg.ac.in",
        "phone": "+91-361-258-2304",
    },
    {
        "name": "Rashmi Dutta Baruah",
        "designation": "Associate Professor",
        "research_interests": "Computational Intelligence, Fuzzy Systems, Neural Networks, Pattern Recognition, Smart Grid",
        "degree": "PhD, IIT Guwahati, India",
        "email": "rashmi@iitg.ac.in",
        "phone": "+91-361-258-2305",
    },
    {
        "name": "Sarat Kumar Patra",
        "designation": "Professor",
        "research_interests": "Signal Processing, VLSI Design, Wireless Communications, Adaptive Filtering, Biomedical Signal Processing",
        "degree": "PhD, IIT Kharagpur, India",
        "email": "skpatra@iitg.ac.in",
        "phone": "+91-361-258-2306",
    },
    {
        "name": "Deepak Mishra",
        "designation": "Assistant Professor",
        "research_interests": "Remote Sensing, Image Processing, Deep Learning, Hyperspectral Imaging, Satellite Data Analysis",
        "degree": "PhD, IIT Bombay, India",
        "email": "deepak.mishra@iitg.ac.in",
        "phone": "+91-361-258-2307",
    },
]


class Command(BaseCommand):
    help = "Populate the database with professor data"

    def handle(self, *args, **kwargs):
        Professor.objects.all().delete()
        self.stdout.write("Cleared existing professor records.")

        for data in PROFESSORS:
            Professor.objects.create(**data)
            self.stdout.write(f"  ✓ Added: {data['name']}")

        self.stdout.write(self.style.SUCCESS(
            f"\nDone! {len(PROFESSORS)} professors added successfully."
        ))