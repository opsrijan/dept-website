from django.core.management.base import BaseCommand
from alumni.models import Alumni

ALUMNI = [
    {
        "name": "Abhist Yadav",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Gupta",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Suryawanshi",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Anant Kacholia",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ankita Anand",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aryan Lath",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aryan Singh",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Borra Lakshya",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Devansh Bhardwaj",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Harsh Raj",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Katta Srikar Reddy",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nishchay Nilabh",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Palthiya Laanith Chouhan",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pokala Rithuraj",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shubhi Agarwal",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Subhash Patel",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sunanda K H",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Thanish Bolla",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Varun Nagpal",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nityam Pareek",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shivam Kumar Singh",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Chaudhari Shantanu Ujwal",
        "batch": 2025,
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    }
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