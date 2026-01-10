# College Helpdesk Rule-Based Chatbot
# AI Internship - Week 1
# Created by: Your Name

import re
import random

# Patterns to identify user intent
intent_patterns = {
    "greeting": r"\b(hi|hello|hey)\b",
    "admission": r"\b(admission|apply|enroll)\b",
    "exam": r"\b(exam|internal|semester|test)\b",
    "attendance": r"\b(attendance|present|percentage)\b",
    "placement": r"\b(placement|company|job)\b",
    "internship": r"\b(internship|training|industrial)\b",
    "library": r"\b(library|books|issue)\b",
    "hostel": r"\b(hostel|mess|room)\b",
    "fees": r"\b(fees|payment|tuition)\b",
    "help": r"\b(help|options|support)\b",
    "exit": r"\b(bye|exit|quit)\b"
}

# Responses for each intent
intent_responses = {
    "greeting": [
        "Hello! Welcome to the College Helpdesk.",
        "Hi! How can I assist you today?"
    ],
    "admission": [
        "Admissions are done through the college admission portal.",
        "You can apply for admission by filling the online application form."
    ],
    "exam": [
        "Exam schedules are released on the college website.",
        "Internal and semester exam details are shared by the department."
    ],
    "attendance": [
        "Minimum attendance required is usually 75 percent.",
        "Attendance rules are strictly followed by the college."
    ],
    "placement": [
        "The placement cell conducts training and recruitment drives.",
        "Placement information is shared via official notices."
    ],
    "internship": [
        "Internships are encouraged during semester breaks.",
        "Students can apply for internships through faculty guidance."
    ],
    "library": [
        "The library is open on all working days.",
        "Students can issue books using their library ID."
    ],
    "hostel": [
        "Hostel facilities are available for both boys and girls.",
        "Hostel rules are provided during admission."
    ],
    "fees": [
        "Fees can be paid online or at the accounts office.",
        "Fee structure details are available on the college website."
    ],
    "help": [
        "You can ask about admission, exams, attendance, placements, internships, library, hostel, and fees.",
        "Supported topics include exams, fees, placement, internship and more."
    ],
    "fallback": [
        "Sorry, I can help only with college-related queries.",
        "I am a rule-based chatbot and can answer limited college questions."
    ],
    "exit": [
        "Thank you for contacting the College Helpdesk. Goodbye!",
        "Bye! Wish you success in your academic journey."
    ]
}


def identify_intent(user_text):
    user_text = user_text.lower()

    for intent, pattern in intent_patterns.items():
        if re.search(pattern, user_text):
            return intent

    return "fallback"


def generate_reply(intent):
    return random.choice(intent_responses[intent])


def run_chatbot():
    print("🎓 College Helpdesk Chatbot")
    print("Type 'help' to see available topics or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        intent = identify_intent(user_input)
        reply = generate_reply(intent)

        print("Bot:", reply)

        if intent == "exit":
            break


run_chatbot()
