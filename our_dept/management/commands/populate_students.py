from django.core.management.base import BaseCommand
from our_dept.models import Student

STUDENTS = [
    {
        "name": "Chekuri Muni Siva Keerthan",
        "roll_number": "220150001",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Dhruv Khichi",
        "roll_number": "220150002",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Goli Poojitha",
        "roll_number": "220150003",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Himanshu Singhal",
        "roll_number": "220150004",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Karan Kumawat",
        "roll_number": "220150005",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Karnati Ravi Teja",
        "roll_number": "220150006",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Madamanchi Chandana",
        "roll_number": "220150007",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mohit Yadav",
        "roll_number": "220150008",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mulla Meharaj",
        "roll_number": "220150009",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Patel Heet Niraj",
        "roll_number": "220150010",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Prakhar Punj",
        "roll_number": "220150011",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Prince Tholia",
        "roll_number": "220150012",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Priyansh Awasthi",
        "roll_number": "220150013",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Raparla Sushmitha",
        "roll_number": "220150014",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Raunit Patel",
        "roll_number": "220150015",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rishita Agarwal",
        "roll_number": "220150016",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sahil Kumar",
        "roll_number": "220150017",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sahil Raj",
        "roll_number": "220150018",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Saptarshi Mukherjee",
        "roll_number": "220150019",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shinde Onkar Harishchandra",
        "roll_number": "220150021",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shivansh Pal",
        "roll_number": "220150022",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sirigudi Midhush",
        "roll_number": "220150024",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Takkellapati Nagendra",
        "roll_number": "220150025",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ujwal Fandulal Kirsan",
        "roll_number": "220150026",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vanama Pranav",
        "roll_number": "220150027",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Varakala Rajasree",
        "roll_number": "220150028",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vishal",
        "roll_number": "220150029",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Uoga Venkata Sai Charan Boddapati",
        "roll_number": "220150030",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Soumya Savarn",
        "roll_number": "220150031",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Arushi Kumar",
        "roll_number": "220150032",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mayukh Maithy",
        "roll_number": "220150033",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ishan Chandra Gupta",
        "roll_number": "220150034",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rishab Sonthalia",
        "roll_number": "220150035",
        "batch": "2022-2026",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    }, 
    {
        "name": "Aditya Sunil Lambat",
        "roll_number": "230150002",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aryan Sandeep Gupta",
        "roll_number": "230150003",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Asif Nazeer Hossain",
        "roll_number": "230150004",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Bandi Kesava Sai Kalyan Ram",
        "roll_number": "230150005",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Bhavika Pandya",
        "roll_number": "230150006",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Billa Cherish",
        "roll_number": "230150007",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Daivik Gupta",
        "roll_number": "230150008",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Dogga Yaswanth",
        "roll_number": "230150009",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ghantenavaru Om",
        "roll_number": "230150010",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Golla Jeswanth Kumar",
        "roll_number": "230150011",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Harshit",
        "roll_number": "230150012",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kasukurthi Sujeeth",
        "roll_number": "230150013",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kudurupaka Ashmita",
        "roll_number": "230150014",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Madam Abhiram",
        "roll_number": "230150015",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mogali Pranav Kumar Reddy",
        "roll_number": "230150016",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mood Prashanth Naik",
        "roll_number": "230150017",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mrigank Pendyala",
        "roll_number": "230150018",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pallempati Sharvani",
        "roll_number": "230150019",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rajarshi Malakar",
        "roll_number": "230150020",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Samvid Pundir",
        "roll_number": "230150021",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sandhya S",
        "roll_number": "230150022",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sanka Hema Naga Sri Varshith",
        "roll_number": "230150023",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shourya Goyal",
        "roll_number": "230150024",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Srijan Kumar",
        "roll_number": "230150025",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sure Naga Sai Balaji",
        "roll_number": "230150026",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Tejas Gajanan Deshmukh",
        "roll_number": "230150027",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vaishnavi Agarwal",
        "roll_number": "230150028",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vibha Gupta",
        "roll_number": "230150029",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Yuvraj Nim",
        "roll_number": "230150030",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Lakshmi C",
        "roll_number": "230150031",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Yash Sarveish Kharangate",
        "roll_number": "230150032",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Avneesh Kumar",
        "roll_number": "230150033",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Anant Sharma",
        "roll_number": "230150034",
        "batch": "2023-2027",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Garg",
        "roll_number": "240150001",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ankit Raj",
        "roll_number": "240150002",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Anuj Kumar",
        "roll_number": "240150003",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Arghya Ojha",
        "roll_number": "240150004",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Arnav Sinha",
        "roll_number": "240150005",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Badri Bishal Das",
        "roll_number": "240150006",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Banoth Sree Ram Nayak",
        "roll_number": "240150007",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Banothu Neeharika",
        "roll_number": "240150008",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Bodakuntla Nishanth",
        "roll_number": "240150009",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Chinthalapalli Bhaskarreddy",
        "roll_number": "240150010",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Huzefa S Bhagat",
        "roll_number": "240150012",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Jaypal Malviya",
        "roll_number": "240150013",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kanhav Purohit",
        "roll_number": "240150014",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kolli Shyamm Kisshore",
        "roll_number": "240150015",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kumar Utkarsh",
        "roll_number": "240150016",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Menni Charan Sree Teja",
        "roll_number": "240150018",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Mohammad Shafqat Jabbar",
        "roll_number": "240150019",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nansy Veronika Mallepogu",
        "roll_number": "240150020",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nayakwadi Saharshini",
        "roll_number": "240150021",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nilay Mittal",
        "roll_number": "240150022",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Palli Ritvik",
        "roll_number": "240150023",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ponaganti Sai Deva Charan",
        "roll_number": "240150024",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pratyaksha Jha",
        "roll_number": "240150025",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pushpendra Singh",
        "roll_number": "240150026",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rachit Gupta",
        "roll_number": "240150027",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rathod Ravikiran",
        "roll_number": "240150029",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ravula Deepansh Reddy",
        "roll_number": "240150030",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ritwik Viswanathan",
        "roll_number": "240150031",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Rup Narayan Jha",
        "roll_number": "240150032",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sheth Freya Amitbhai",
        "roll_number": "240150033",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Somita Agarwal",
        "roll_number": "240150035",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sunkari Sharanya",
        "roll_number": "240150036",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Tanish Anand",
        "roll_number": "240150037",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Tumu Sai Seshi Kiran",
        "roll_number": "240150038",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Yendluri Yasaswi",
        "roll_number": "240150040",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sujal Patnaik",
        "roll_number": "240150041",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sudipto Ghosh",
        "roll_number": "240150042",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Maimoona Saifee",
        "roll_number": "240150043",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Deshmane Lalit Santosh",
        "roll_number": "240150044",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pratham Saluja",
        "roll_number": "240150045",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kushagra Singhal",
        "roll_number": "240150046",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Paul",
        "roll_number": "240150047",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sahil Shamrao Rathod",
        "roll_number": "240150048",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Debarghya Das",
        "roll_number": "240150049",
        "batch": "2024-2028",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Raj",
        "roll_number": "250150001",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Rajesh Borkar",
        "roll_number": "250150002",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Aditya Rana",
        "roll_number": "250150003",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Anant Gupta",
        "roll_number": "250150004",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Anjali Pogulwad",
        "roll_number": "250150005",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Arya Bhagchand Khapekar",
        "roll_number": "250150006",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Avani Moon",
        "roll_number": "250150007",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ayush Rahul Bholane",
        "roll_number": "250150008",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Bagadi Bhargav",
        "roll_number": "250150009",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Bhukya Charandeep",
        "roll_number": "250150010",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Chhavi Mittal",
        "roll_number": "250150011",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Daksh Bhutani",
        "roll_number": "250150012",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Deepak Dhakad",
        "roll_number": "250150013",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Golamaru Gowtham Sai Reddy",
        "roll_number": "250150014",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Hadekar Ankit Kishor",
        "roll_number": "250150015",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Harsh Verma",
        "roll_number": "250150016",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Jatin Mehra",
        "roll_number": "250150017",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kshetrimayum Naresh Singh",
        "roll_number": "250150018",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Kushagra Jayprakash Sinha",
        "roll_number": "250150019",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Loukya Nuthalapati",
        "roll_number": "250150020",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Madhav Shahi",
        "roll_number": "250150021",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Madireddy Ashok Reddy",
        "roll_number": "250150022",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Maloth Anji",
        "roll_number": "250150023",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Moirangthem Arlex Singh",
        "roll_number": "250150024",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nistha Gautam",
        "roll_number": "250150025",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Nitin Mali",
        "roll_number": "250150026",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Polina Swathi",
        "roll_number": "250150027",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Prachi Goel",
        "roll_number": "250150028",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Prajapati Maitra Jitendrakumar",
        "roll_number": "250150029",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Prakash Kumar",
        "roll_number": "250150030",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pranjal Sharma",
        "roll_number": "250150031",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Praveen Kumar",
        "roll_number": "250150032",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Pulicheru Sahasravarun Tej",
        "roll_number": "250150033",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ruttala Vamsi Krishna",
        "roll_number": "250150034",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Ryan Rajesh",
        "roll_number": "250150035",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sayan Patra",
        "roll_number": "250150036",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Shreyas Samantray",
        "roll_number": "250150037",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Siddhant Patil",
        "roll_number": "250150038",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Siddharth Kochhar",
        "roll_number": "250150039",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Singh Ayushkumar Jairam",
        "roll_number": "250150040",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Sukanya Kumari",
        "roll_number": "250150041",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Swarit Subham",
        "roll_number": "250150042",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Tank Raj Nalinkumar",
        "roll_number": "250150043",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Tankasala Madhughnesh",
        "roll_number": "250150044",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vaidik Maheshwari",
        "roll_number": "250150045",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vamika Jakkula",
        "roll_number": "250150046",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vanama Abhinav",
        "roll_number": "250150047",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Vedant Nitin Kalbende",
        "roll_number": "250150048",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Waghela Yuvraj Pinakin",
        "roll_number": "250150049",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    },
    {
        "name": "Yash Choudhary",
        "roll_number": "250150050",
        "batch": "2025-2029",
        "email": "",
        "phone": "",
        "github": "",
        "linkedin": "",
        "company": "",
        "role": ""
    }
]


from django.core.management.base import BaseCommand
from our_dept.models import Student

class Command(BaseCommand):
    help = 'Populate Student records (sync mode)'

    def handle(self, *args, **kwargs):
        created_count = 0
        updated_count = 0

        # Track roll numbers from script
        incoming_rolls = set()

        for entry in STUDENTS:
            roll = entry.get('roll_number')
            if not roll:
                self.stdout.write(self.style.WARNING(f"Skipping entry without roll_number: {entry}"))
                continue

            incoming_rolls.add(roll)

            obj, created = Student.objects.update_or_create(
                roll_number=roll,
                defaults={
                    'name': entry.get('name', ''),
                    'batch': entry.get('batch'),
                    'email': entry.get('email', ''),
                    'phone': entry.get('phone', ''),
                    'linkedin_url': entry.get('linkedin_url', ''),
                    'github': entry.get('github', ''),
                    'current_role': entry.get('current_role', ''),
                    'company': entry.get('company', ''),
                },
            )

            if created:
                created_count += 1
                self.stdout.write(f"✓ Created: {obj}")
            else:
                updated_count += 1
                self.stdout.write(f"↻ Updated: {obj}")

        # 🔥 DELETE old records not present anymore
        deleted_count, _ = Student.objects.exclude(
            roll_number__in=incoming_rolls
        ).delete()

        # Summary
        self.stdout.write(self.style.SUCCESS(
            f"\nDone. Created: {created_count}, Updated: {updated_count}, Deleted: {deleted_count}"
        ))