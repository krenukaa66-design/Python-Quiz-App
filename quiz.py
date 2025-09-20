import random

# Questions directly inside the code (no file needed)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "C++", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    }
]

def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    print("\n📘 Welcome to the Quiz App!\n")

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"   {i}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if q["options"][answer - 1].lower() == q["answer"].lower():
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}\n")
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.\n")

    print(f"🎯 Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz(questions)
