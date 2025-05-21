# This quiz game has users add 4 numbers together and tells them if they are correct or not.
import pyinputplus as pyip
import random, time

# Number of questions to be asked.
questions = 5

# Stores answers that are correct, starts at 0.
correct_answers = 0

# Main loop that sets up the game and accepts user input.
for question_number in range(questions):
  num_1 = random.randint(0, 20)
  num_2 = random.randint(0, 20)
  num_3 = random.randint(0, 20)
  num_4 = random.randint(0, 20)

  prompt = "question # %s: %s + %s + %s + %s = " % (question_number, num_1, num_2, num_3, num_4)

  try:
    pyip.inputStr(prompt, allowRegexes=["^%s$" % (num_1 + num_2 + num_3 + num_4)],
                  blockRegexes=[(".*", "Incorrect!")], timeout=12, limit=3)
  except pyip.TimeoutException:
    print('Out of time!')
  except pyip.RetryLimitException:
    print('Out of tries!')
  else:
    print('Correct!')
    correct_answers += 1
  time.sleep(1) # Gives users 1 second to see answer before next question
print('Score: %s / %s' % (correct_answers, questions))