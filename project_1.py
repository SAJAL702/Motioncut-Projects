questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A.New Delhi","B.Pune","C.Hyderabad","D.Lucknow"],
        "answer": "A"
    },
    {
        "question": "Which is the largest country?",
        "options": ["A.India","B.America","c.Russia","D.England"],
        "answer": "C"
    },
    {
        "question":"What is the capital of France?",
        "options": ["A.Paris","B.London","C.Berlin","D.Madrid"],
        "answer": "A"
    },
    {
        
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
]
def main(questions):
    score = 0
    for i,question in enumerate(questions):
        print(f"Q{i + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Your answer: ").strip().upper()
        if answer == question['answer']:
            score += 1
            print("\nYour answer is correct")
        else:
            print(f"\nCorrect answer is {question['answer']}")
        print(f"\nTotal score is {score}/{len(questions)}")
main(questions)