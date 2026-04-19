from django.core.management.base import BaseCommand
from alumni.models import Alumni

ALUMNI = [
    {
        "name": "Aarav Sharma",
        "batch": 2024,
        "email": "aarav.sharma@gmail.com",
        "phone": "+91-98765-43210",
        "github": "https://github.com/aaravsharma",
        "linkedin": "https://linkedin.com/in/aaravsharma",
        "company": "Google",
        "role": "Software Engineer",
    },
    {
        "name": "Priya Nair",
        "batch": 2024,
        "email": "priya.nair@outlook.com",
        "phone": "+91-91234-56789",
        "github": "https://github.com/priyanair",
        "linkedin": "https://linkedin.com/in/priyanair",
        "company": "Microsoft",
        "role": "Data Scientist",
    },
    {
        "name": "Rohan Das",
        "batch": 2023,
        "email": "rohan.das@gmail.com",
        "phone": "+91-99887-76655",
        "github": "https://github.com/rohandas",
        "linkedin": "https://linkedin.com/in/rohandas",
        "company": "Amazon",
        "role": "ML Engineer",
    },
    {
        "name": "Sneha Gupta",
        "batch": 2023,
        "email": "sneha.gupta@gmail.com",
        "phone": "+91-97654-32100",
        "github": "https://github.com/snehagupta",
        "linkedin": "https://linkedin.com/in/snehagupta",
        "company": "Flipkart",
        "role": "Backend Developer",
    },
    {
        "name": "Kiran Mehta",
        "batch": 2022,
        "email": "kiran.mehta@yahoo.com",
        "phone": "+91-93456-78901",
        "github": "https://github.com/kiranmehta",
        "linkedin": "https://linkedin.com/in/kiranmehta",
        "company": "Infosys",
        "role": "Systems Analyst",
    },
    {
        "name": "Divya Bose",
        "batch": 2022,
        "email": "divya.bose@gmail.com",
        "phone": "+91-90123-45678",
        "github": "https://github.com/divyabose",
        "linkedin": "https://linkedin.com/in/divyabose",
        "company": "Wipro",
        "role": "Cloud Engineer",
    },
    {
        "name": "Arjun Pillai",
        "batch": 2021,
        "email": "arjun.pillai@gmail.com",
        "phone": "+91-88765-43219",
        "github": "https://github.com/arjunpillai",
        "linkedin": "https://linkedin.com/in/arjunpillai",
        "company": "TCS",
        "role": "Full Stack Developer",
    },
    {
        "name": "Meera Iyer",
        "batch": 2021,
        "email": "meera.iyer@gmail.com",
        "phone": "+91-87654-32198",
        "github": "https://github.com/meeraiyer",
        "linkedin": "https://linkedin.com/in/meeraiyer",
        "company": "Accenture",
        "role": "AI Researcher",
    },
    {
        "name": "Nikhil Joshi",
        "batch": 2020,
        "email": "nikhil.joshi@gmail.com",
        "phone": "+91-86543-21987",
        "github": "https://github.com/nikhiljoshi",
        "linkedin": "https://linkedin.com/in/nikhiljoshi",
        "company": "Samsung R&D",
        "role": "Embedded Systems Engineer",
    },
    {
        "name": "Tanvi Reddy",
        "batch": 2020,
        "email": "tanvi.reddy@gmail.com",
        "phone": "+91-85432-10976",
        "github": "https://github.com/tanvireddy",
        "linkedin": "https://linkedin.com/in/tanvireddy",
        "company": "Qualcomm",
        "role": "VLSI Design Engineer",
    },
]


class Command(BaseCommand):
    help = "Populate alumni data"

    def handle(self, *args, **kwargs):
        Alumni.objects.all().delete()
        self.stdout.write("Cleared existing alumni records.")
        for person in ALUMNI:
            Alumni.objects.create(**person)
            self.stdout.write(f"  ✓ {person['name']} — Batch {person['batch']}")
        self.stdout.write(self.style.SUCCESS(
            f"\nDone! {len(ALUMNI)} alumni added."
        ))