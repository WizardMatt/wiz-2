questions = {
    "What is the capital of France?": "a",
    "Which language is used in web development? (a) Python (b) JavaScript (c) C++": "b",
    "How many legs does a spider have? (a) 6 (b) 8 (c) 10": "b"
}

score = 0

for question, answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer (a/b/c): ").lower()
    if user_answer == answer:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")

print(f"\nFinal Score: {score}/{len(questions)}")
