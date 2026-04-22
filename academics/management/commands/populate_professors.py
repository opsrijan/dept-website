from django.core.management.base import BaseCommand
from academics.models import Professor


PROFESSORS = [
    {
        "name": "Rhythm Grover",
        "designation": "Assistant Professor",
        "research_interests": "Efficient Algorithms for parameter estimation of signal processing models, Statistical properties of classical parameter estimation methods, Robust methods of parameter estimation in presence of outliers in the data",
        "degree": "PhD, IIT Kanpur, India",
        "email": "rhythmgrover@iitg.ac.in",
        "phone": "+91-361-258-3503"
    },
    {
        "name": "Shruti Shantiling Phutke",
        "designation": "Assistant Professor",
        "research_interests": "Artificial Intelligence, Machine Learning, Deep Learning, and Computer Vision for Healthcare, Agriculture, and Real-World Visual Applications, including Medical Image Analysis, EEG Signal Processing, Image and Video Inpainting, and Underwater and Aerial Image Enhancement",
        "degree": "PhD, IIT Ropar, India",
        "email": "ssphutke@iitg.ac.in",
        "phone": "+91-361-258-xxxx"
    },
    {
        "name": "Teena Sharma",
        "designation": "Assistant Professor",
        "research_interests": "Artificial Intelligence, Machine Learning, and Deep Learning Algorithms for Image Enhancement, Object Recognition, and Biomedical Data Inequality",
        "degree": "PhD, IIT Kanpur, India",
        "email": "teena@iitg.ac.in",
        "phone": "+91-361-258-3506"
    },
    {
        "name": "Amulya Kumar Mahto",
        "designation": "Assistant Professor",
        "research_interests": "Statistical Modelling, Accelerated Life Testing, Competing Risks, Multicomponent Stress-Strength Reliability, Statistical Optimization, Classical and Bayesian Estimation",
        "degree": "PhD, IIT Patna, India",
        "email": "akmahto@iitg.ac.in",
        "phone": "+91-361-258-3509"
    },
    {
        "name": "Arghyadip Roy",
        "designation": "Assistant Professor",
        "research_interests": "Optimization and Control of Stochastic Systems, Reinforcement Learning, Markov Decision Process, Multi-armed Bandit, Stochastic Approximation, Resource Allocation in Communication Networks, Application of Reinforcement learning in Wireless Communication",
        "degree": "PhD, IIT Bombay, India",
        "email": "arghyadip@iitg.ac.in",
        "phone": "+91-361-258-3505"
    },
    {
        "name": "Ayon Borthakur",
        "designation": "Assistant Professor",
        "research_interests": "Embedded AI systems, Deep learning, Neuromorphic computing, Computational neuroscience",
        "degree": "PhD, Cornell University, US",
        "email": "ayon.borthakur@iitg.ac.in",
        "phone": "+91-361-258-3511"
    },
    {
        "name": "Chiranjib Sur",
        "designation": "Assistant Professor",
        "research_interests": "Deep Learning, NLP/NLU, Recommendation Systems for Multimedia, Image/Video Captioning, Story Telling, Questioning Answering, Translation, Visual Questioning Answering, Statistical Learning, Image to Image Transformation, Segmentation and Organ detection, Object Detection, Scene Understanding, Multi-Frame Prediction, Scalable Big Data Technologies",
        "degree": "PhD, University of Florida, US",
        "email": "chiranjib@iitg.ac.in",
        "phone": "+91-361-258-3508"
    },
    {
        "name": "Debanga Raj Neog",
        "designation": "Assistant Professor",
        "research_interests": "Machine learning and Deep Learning (Object tracking and localization, stereo reconstruction), Image Processing (Semantic segmentation, biomedical image processing), Computer Vision (Eye tracking, face tracking), Computer Graphics and AR/VR (Facial animation, anatomical augmented reality), Computational Imaging (High dynamic range imaging)",
        "degree": "PhD, Univ. British Columbia Vancouver, Canada",
        "email": "dneog@iitg.ac.in",
        "phone": "+91-361-258-3504"
    },
    {
        "name": "Dipankar Mondal",
        "designation": "Assistant Professor",
        "research_interests": "Financial Risk Modelling, Sustainable Finance, Portfolio Optimization, Derivative Pricing",
        "degree": "PhD, IIT Guwahati, India",
        "email": "mdipankar@iitg.ac.in",
        "phone": "+91-361-258-3513"
    },
    {
        "name": "Neeraj Kumar Sharma",
        "designation": "Assistant Professor",
        "research_interests": "Signal Processing (Speech, Audio, EEG); Time–Frequency and AM–FM Modeling; Multimodal Representation Learning and AI; Neuro-AI; Human and Machine Intelligence",
        "degree": "PhD, IISc Bangalore, India",
        "email": "neerajs@iitg.ac.in",
        "phone": "+91-361-258-3507"
    },
    {
        "name": "Prashant W. Patil",
        "designation": "Assistant Professor",
        "research_interests": "Computer Vision, Deep Learning, Multimodal Deepfake Detection, Image/Video Super-resolution, Multi-weather Image/Video Restoration, Video Object Tracking/Recognition, Video Object Segmentation",
        "degree": "PhD, IIT Ropar, India",
        "email": "pwpatil@iitg.ac.in",
        "phone": "+91-361-258-3510"
    }
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