# quiz_app.py

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Unit"],
        "answer": "B"
    },
    {
        "question": "Which one is a Python framework?",
        "options": ["A. Django", "B. Laravel", "C. React", "D. Spring"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. define", "B. def", "C. function", "D. func"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    print("\n🎯 Welcome to the Quiz App!\n")

    for idx, q in enumerate(questions, start=1):
        print(f"Q{idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

    print("📊 Quiz Completed!")
    print(f"Your Score: {score} out of {len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("🏆 Excellent performance!")
    elif percentage >= 50:
        print("👍 Good effort!")
    else:
        print("📘 Keep practicing!")

if __name__ == "__main__":
    run_quiz()
