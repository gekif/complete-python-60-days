import json

# Load questions from JSON file
with open('question.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0  # sum of all right answer
total = len(data)  # total of question

print("=== QUIZ DIMULAI ===\n")

for index, question in enumerate(data, start=1):
    print(f"Question {index}: {question['question']}")

    # Show the alternative answer
    for option in question['options']:
        print(option)

    # User answer input
    user_answer = input("Enter your answer (put number): ")

    # validasi input & cek jawaban
    try:
        if int(user_answer) == question['answer']:
            print("✅ Right ANSWER\n")
            score += 1
        else:
            print("❌ Wrong ANSWER\n")
    except ValueError:
        print("❌ Not a valid input (Wrong answer)\n")

# hasil akhir
print("=== RESULT ===")
print(f"Score: {score}/{total}")
print(f"Explanation: only {score} from {total} question that right chosen")
