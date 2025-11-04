import random
import time

quiz_question= [
    {
      "question": "Which language is used to create web pages?",
      "options":["Python", "HTML", "C++", "JAVA"],
      "answer": "HTML"  
    },
    {
      "question": "Which data structure uses FIFO (Firrst in first out}?",
      "options":["Stack", "Queue", "Tree", "Graph"],
      "answer": "Queue"  
    },
    {
        "question": "Who developed the Python programming language?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Sundar Pichai"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
     {
        "question": "What is the output of 5 + 3 * 2?",
        "options": ["16", "13", "11", "10"],
        "answer": "11"
    },
     {
        "question": "Which of the following is not a programming language?",
        "options": ["HTML", "Python", "Ruby", "C++"],
        "answer": "HTML"
    },
     {
        "question": "Which company owns the Android operating system?",
        "options": ["Apple", "Google", "Microsoft", "Samsung"],
        "answer": "Google"
    },
     {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Central Processor Utility"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
     {
        "question": "Which one is the largest social media platform?",
        "options": ["Twitter", "Instagram", "Facebook", "LinkedIn"],
        "answer": "Facebook"
    }   
]
def run_quiz():
    print(" 🎉Welcome to the Fun Quiz Game!")
    time.sleep(1)
    name=input(" 👉what's your name? ")
    print(f"\nHey {name}! 😄 Lets test your knowledge. \n")
    time.sleep(1)
    score=0
    total=len(quiz_question)
    
    random.shuffle(quiz_question)
    
    for i, q in enumerate(quiz_question, start=1):
        print(f"-----------------------------")
        print(f"🧩 Question {i} of {total}")
        print(f"{q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f" {idx}.  {option}")
        
       # "user input"
        try:
            choice = int(input(" 👉Enter your answer (1-4): "))
            selected = q["options"][choice - 1]
        except (ValueError, IndexError):
            print(" ⚠️ Invalid input! Let's move to the next one.\n")
            time.sleep(1)
            continue
        #check answes
        if selected.lower() == q["answer"].lower():
            print("✅ Correct! Nice one! 🎯\n")
            score+=1
        else:
            print(f"❌ Oops! The correct answer is: {q['answer']}\n")
            time.sleep(1)
            
        # Result summary
    print("=================================")
    print(f"🏁 Quiz finished, {name}!")
    print(f"📊 Your final score: {score}/{total}\n")
    
    #feedback message
    if score == total:
        print("🎖️ Outstanding! You nailed every question!")
    elif score >= total * 0.8:
        print("👏 Great job! You clearly know your stuff.")
    elif score >= total * 0.5:
        print("👍 Not bad! Keep practicing and you’ll get even better.")
    else:
        print("😅 Looks like you need a bit more practice. Don’t give up!")
    print("=================================")

if __name__ == "__main__":
    run_quiz()