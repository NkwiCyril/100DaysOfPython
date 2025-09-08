print("Welcome to Python Quiz Game")

questions_answers = [
    {
        "question": "What does CPU stand for?",
        "answer": "Central Processing Unit"
    },
    {
        "question": "What does GPU stand for?",
        "answer": "Graphics Processing Unit"
    },
    {
        "question": "What does RAM stand for?",
        "answer": "Random Access Memory"
    },
    {
        "question": "What does HTTP stand for?",
        "answer": "HyperText Transfer Protocol"
    },
    {
        "question": "What does HTML stand for?",
        "answer": "HyperText Markup Language"
    },
    {
        "question": "What does IP stand for in networking?",
        "answer": "Internet Protocol"
    },
    {
        "question": "What does DNS stand for?",
        "answer": "Domain Name System"
    },
    {
        "question": "What does SQL stand for?",
        "answer": "Structured Query Language"
    },
    {
        "question": "What does API stand for?",
        "answer": "Application Programming Interface"
    },
    {
        "question": "What does OS stand for?",
        "answer": "Operating System"
    }
]

points = 0
num_questions_answered = 0
missed_questions = []

for question_answer in questions_answers:

    answer = input(question_answer["question"] + " \n")

    if answer.lower() == question_answer["answer"].lower():
        points += 1
        print("Correct! You get a point!\n")
    else:
        print("Incorrect!\n")
        missed_questions.append({
            "question": question_answer["question"],
            "correct_answer": question_answer["answer"],
            "your_answer": answer
        })

    num_questions_answered += 1

print(f"Number of questions answered: {num_questions_answered}")
print(f"Total points: {points}/{num_questions_answered}")

if missed_questions:
    print("\nYou missed the following questions:")
    for idx, item in enumerate(missed_questions, start=1):
        print(f"{idx}. {item['question']}")
        print(f"   Correct answer: {item['correct_answer']}")
        print(f"   Your answer:    {item['your_answer']}\n")
