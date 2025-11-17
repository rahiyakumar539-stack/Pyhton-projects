import random
import time

print("🎯 Welcome to the Guess the Number Game!")
print("You vs Computer 🤖")
print("Both will try to guess the secret number between 1 to 100.")
print("Whoever finds it first wins!\n")

secret_number = random.randint(1, 100)
attempts = 7

low = 1
high = 100

# Start timer
start_time = time.time()

while attempts > 0:
    
    # -------- USER GUESS --------
    guess = int(input("👉 Your guess: "))

    if guess < 1 or guess > 100:
        print("❌ Invalid! Enter number between 1–100.\n")
        continue

    if guess == secret_number:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        print("🎉 YOU WIN! You guessed it correctly before the computer!")
        print(f"⏳ You took {total_time} seconds to guess!")
        break
    elif guess < secret_number:
        print("📉 Your guess is too low.")
        low = guess + 1
    else:
        print("📈 Your guess is too high.")
        high = guess - 1


    # -------- COMPUTER GUESS (SMART AI) --------
    computer_guess = (low + high) // 2
    print(f"🤖 Computer guesses: {computer_guess}")

    if computer_guess == secret_number:
        print("🤖🏆 COMPUTER WINS! It guessed the number before you!")
        break
    elif computer_guess < secret_number:
        print("🤖 Computer guessed too low.")
        low = computer_guess + 1
    else:
        print("🤖 Computer guessed too high.")
        high = computer_guess - 1


    attempts -= 1
    print(f"🔥 Attempts left: {attempts}\n")


# -------- GAME OVER --------
if attempts == 0:
    print(f"😢 Game Over! Nobody guessed the number. It was {secret_number}.")
