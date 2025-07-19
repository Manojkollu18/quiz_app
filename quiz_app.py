import json
import random

# Load questions from JSON file
def load_questions(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")
    return []

# Run the quiz
def run_quiz(questions):
    score = 0
    random.shuffle(questions)  # Randomize question order

    for idx, q in enumerate(questions, start=1):
        print(f"\nQ{idx}: {q['question']}")
        options = q['options']
        random.shuffle(options)  # Randomize option order

        for i, option in enumerate(options, start=1):
            print(f"  {i}. {option}")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if options[choice - 1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except (ValueError, IndexError):
            print(f"⚠️ Invalid input! Correct answer: {q['answer']}")

    return score, len(questions)

# Main function
def main():
    print("🎯 Welcome to the Quiz App!")
    questions = load_questions("questions.json")
    score, total = run_quiz(questions)

    print("\n🔚 Quiz Completed!")
    print(f"🎉 Your Score: {score}/{total} ({(score/total)*100:.2f}%)")

if __name__ == "__main__":
    main()
