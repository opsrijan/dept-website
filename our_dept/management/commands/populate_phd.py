from django.core.management.base import BaseCommand
from our_dept.models import PhDStudent

PHD_STUDENTS = [
    {
        "batch": "Dec 2021",
        "name": "Anupam Kumar",
        "interests": "NLP",
        "email": "anupam.kumar@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2021",
        "name": "Avantika Sahu",
        "interests": "Time-Series Data Analysis, NLP, Statistical Signal Processing and\n\t\t\t\t\t\t\t\t\t\tModelling",
        "email": "s.avantika@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2021",
        "name": "Kamal Kumar",
        "interests": "Computer Vision, Machine Learning, Deep Learning",
        "email": "kkamal@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2021",
        "name": "Tanmoy Mandal",
        "interests": "Cryptography, Abstract Algebra",
        "email": "m.tanmoy@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2022",
        "name": "Pallapu Mohan Krishna",
        "interests": "Video Understanding, Sign Language Understanding, Deep Learning for Computer Vision, Multimodal AI",
        "email": "k.pallapu@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2022",
        "name": "Rahul Bhardwaj",
        "interests": "Deep Learning for Computer Vision, Machine Learning, Medical Image Analysis",
        "email": "r.bhardwaj@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2022",
        "name": "Shania H",
        "interests": "Machine Learning, Deep Learning, Signal Processing",
        "email": "h.shania@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2022",
        "name": "Vikky Masih",
        "interests": "Stochastic System Optimization and Control, Internet of Things, Reinforcement Learning, Decision Making under Uncertainty, Reliability based Design, Agent based Systems, High Risk Systems",
        "email": "m.vikky@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2022",
        "name": "Omendra Gangwar",
        "interests": "Statistical Signal Processing, Bayesian Inference, Uncertainty Quantification, and Time Series Forecasting",
        "email": "o.gangwar@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2022",
        "name": "Prakhar Kumar Sonkar",
        "interests": "Machine Learning, Deep Learning, Audio Signal Processing",
        "email": "p.sonkar@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2023",
        "name": "Gautam Singha",
        "interests": "Deep Learning, Machine Learning, Computer Vision, Flood Monitoring and Assessment",
        "email": "g.singha@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2023",
        "name": "Jyotishman Bora",
        "interests": "Computer Vision, Natural Language Processing, Multi-modal Analysis",
        "email": "j.bora@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2023",
        "name": "Kartikay Agrawal",
        "interests": "Deep Learning, State Space Models, Continual learning, Spiking Neural Networks, Computational Neuroscience",
        "email": "a.kartikay@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2023",
        "name": "Bipul Kumar Das",
        "interests": "Machine Learning, Deep Learning",
        "email": "d.bipul@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2023",
        "name": "Nikhil Jaiswal",
        "interests": "Machine Learning, Deep Learning, Natural Language Processing, Computer Vision, Statistics",
        "email": "j.nikhil@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Nishi Chaudhary",
        "interests": "Computer Vision, Deep Learning, Machine Learning, Depth Estimation and 3D Reconstruction",
        "email": "c.nishi@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Naveen Varshney",
        "interests": "Computer Vision, Statistical Learning",
        "email": "n.varshney@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Ayushi Pandey",
        "interests": "Reliability Analysis, Phased Mission Systems",
        "email": "ayushi.pandey@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Kishan Chakraborty",
        "interests": "Reinforcement Learning, Multi-armed Bandit, Graph Theory",
        "email": "c.kishan@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Vaishnavi N",
        "interests": "Continual Learning, LifeLong Learning, Deep Learning, NeuroAI",
        "email": "n.vaishnavi@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Sourav Mondal",
        "interests": "Statistical Inference, Reliability Analysis, Multiple Hypothesis Testing",
        "email": "souravm0006@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Sapna Sachan",
        "interests": "Computer Vision, Medical Image Analysis",
        "email": "s.sapna@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2024",
        "name": "Surojit Karmakar",
        "interests": "Multi-Modal Learning, Computer Vision",
        "email": "k.surojit@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2024",
        "name": "Sushodhan Sudhir Vaishampayan",
        "interests": "Anomaly Detection, Time-Series Analysis, Causal Discovery, Explainable AI",
        "email": "v.sushodhan@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2024",
        "name": "Aishwarya S Murthy",
        "interests": "Computer Vision, Quantum Computing for Deep Learning",
        "email": "a.murthy@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2024",
        "name": "Rachibe Liegise",
        "interests": "LLMs, Image processing,  CNN, fairness, text captioning, SNN",
        "email": "l.rachibe@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Dec 2024",
        "name": "Abhas Kumar Sinha",
        "interests": "Computer Vision, Structure-from-Motion, 3D Generation, Point Cloud Analysis, Photogrammetry, Depth Estimation",
        "email": "s.abhas@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Diptarka Mandal",
        "interests": "Medical Imaging, Multi Modal Data Fusion, Sustainable Solutions, Medical Rehabilitation Devices",
        "email": "m.diptarka@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Gajendra Chaudhary",
        "interests": "Statistical Signal Processing, Machine Learning, Deep Learning, Time series analysis",
        "email": "c.gajendra@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Gourish Majumdar",
        "interests": "Deep Learning, Privacy and Security in Deep Learning, Physics inspired Deep Learning",
        "email": "m.gourish@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Kalyani Prashant Kolte",
        "interests": "Multi-Modal Learning, Low-Memory Computer Vision",
        "email": "k.kalyani@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Kishan Kumar",
        "interests": "Quantitative finance, Stochastic Process , Markov chain",
        "email": "Kishank0006@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Lammibert Sumer",
        "interests": "Quantum AI, Quantum-inspired Algorithms, Nature Inspired Algorithms",
        "email": "s.lammibert@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Navya Sonal Agarwal",
        "interests": "Computer Vision",
        "email": "a.navya@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    },
    {
        "batch": "Jul 2025",
        "name": "Timothy Alex John",
        "interests": "Music Information Retrieval, Computer Vision, Recommendation Systems, Algorithms",
        "email": "j.timothy@iitg.ac.in",
        "phone": "",
        "github": "",
        "linkedin": ""
    }
]

class Command(BaseCommand):
    help = 'Populate PhD Student records'

    def handle(self, *args, **kwargs):
        created_count = 0
        for entry in PHD_STUDENTS:
            obj, created = PhDStudent.objects.get_or_create(
                name=entry['name'],
                batch=entry['batch'],
                defaults={
                    'interests': entry.get('interests', ''),
                    'email':     entry.get('email', ''),
                    'phone':     entry.get('phone', ''),
                    'github':    entry.get('github', ''),
                    'linkedin':  entry.get('linkedin', ''),
                },
            )
            if created:
                created_count += 1
                self.stdout.write(f"  ✓ Created: {obj}")
            else:
                self.stdout.write(f"  — Already exists: {obj}")

        self.stdout.write(self.style.SUCCESS(f"\nDone. {created_count} new record(s) inserted."))