# This program uses pyinputplus, random, and time to create a short quiz
# based on the multiplication table, numbers 1-12. 
import pyinputplus as pyip
import random, time

# Sets the number of questions in the quiz
questions = 10

# stores correct answers
correctAnswers = 0

# main loop to execute the program
for questionNumber in range(questions):
  num1 = random.randint(0, 12)
  num2 = random.randint(0, 12)

  prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

  try:
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
    blockRegexes=[('.*', 'Incorrect!')],
    timeout=8, limit=3) # Timeout in number of seconds, limit in number of tries
  except pyip.TimeoutException:
    print('Out of time!')
  except pyip.RetryLimitException:
    print('Out of tries!')
  else:
    print('Correct!')
    correctAnswers += 1
  time.sleep(1) # Gives users 1 second to see answer before next question
print('Score: %s / %s' % (correctAnswers, questions))