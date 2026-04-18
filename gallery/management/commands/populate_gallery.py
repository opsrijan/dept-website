from django.core.management.base import BaseCommand
from gallery.models import GalleryImage

IMAGES = [
    {"title": "Annual Tech Fest 2024",     "image_url": "https://picsum.photos/seed/techfest/800/600",     "year": 2024, "category": "Events"},
    {"title": "Graduation Ceremony 2024",  "image_url": "https://picsum.photos/seed/graduation/800/600",   "year": 2024, "category": "Academics"},
    {"title": "Research Lab Session",      "image_url": "https://picsum.photos/seed/researchlab/800/600",  "year": 2024, "category": "Research"},
    {"title": "Sports Day 2024",           "image_url": "https://picsum.photos/seed/sportsday/800/600",    "year": 2024, "category": "Sports"},
    {"title": "Cultural Night 2024",       "image_url": "https://picsum.photos/seed/cultural/800/600",     "year": 2024, "category": "Cultural"},
    {"title": "Workshop on AI",            "image_url": "https://picsum.photos/seed/aiworkshop/800/600",   "year": 2024, "category": "Academics"},
    {"title": "Hackathon 2023",            "image_url": "https://picsum.photos/seed/hackathon/800/600",    "year": 2023, "category": "Events"},
    {"title": "Convocation 2023",          "image_url": "https://picsum.photos/seed/convocation/800/600",  "year": 2023, "category": "Academics"},
    {"title": "Industry Visit 2023",       "image_url": "https://picsum.photos/seed/industry/800/600",     "year": 2023, "category": "Industry"},
    {"title": "Freshers Welcome 2023",     "image_url": "https://picsum.photos/seed/freshers/800/600",     "year": 2023, "category": "Cultural"},
    {"title": "Cricket Tournament 2023",   "image_url": "https://picsum.photos/seed/cricket/800/600",      "year": 2023, "category": "Sports"},
    {"title": "Guest Lecture 2023",        "image_url": "https://picsum.photos/seed/lecture/800/600",      "year": 2023, "category": "Academics"},
    {"title": "Annual Day 2022",           "image_url": "https://picsum.photos/seed/annualday/800/600",    "year": 2022, "category": "Events"},
    {"title": "Project Exhibition 2022",   "image_url": "https://picsum.photos/seed/exhibition/800/600",   "year": 2022, "category": "Research"},
    {"title": "Farewell 2022",             "image_url": "https://picsum.photos/seed/farewell/800/600",     "year": 2022, "category": "Cultural"},
]

class Command(BaseCommand):
    help = "Populate gallery with sample images"

    def handle(self, *args, **kwargs):
        GalleryImage.objects.all().delete()
        for item in IMAGES:
            GalleryImage.objects.create(**item)
            self.stdout.write(f"  ✓ {item['title']}")
        self.stdout.write(self.style.SUCCESS(f"\nAdded {len(IMAGES)} images."))