import random
from response import responses
import re
from calculation import Calculation

bot_template = "Bot: {0}"

def respond(message):
   if message in responses:
      bot_message = random.choice(responses[message])
   else:
      bot_message = random.choice(responses["default"])
   return bot_message

def related(x_text):
    
    if "name" in x_text:
      y_text = "what's your name?"

    elif any(substring in x_text for substring in ["hi", "hey", "hello", "what's up"]):
        y_text = "greetings"

    elif "robot" in x_text:
      y_text = "are you a robot?"

    elif "how are" in x_text:
      y_text = "how are you?"

    elif any(substring in x_text for substring in ["calculate", "calculation", "calculations"]):
        y_text = "calculate"

    elif "add" in x_text:
        numbers = tuple(int(s) for s in re.findall(r'\d+', x_text))
        def add(numbers):
            return sum(numbers)
        calculate = Calculation(numbers)
        calculate.add(numbers)

        y_text = "addition"

    elif any(substring in x_text for substring in ["sub", "diff", "difference"]):
        numbers = tuple(int(s) for s in re.findall(r'\d+', x_text))
        calculate_diff = Calculation(numbers)
        calculate_diff.sub()

        y_text = "subtraction"

    elif any(substring in x_text for substring in ["mul", "multiply", "difference"]):
        numbers = tuple(int(s) for s in re.findall(r'\d+', x_text))
        calculate_product = Calculation(numbers)
        calculate_product.mul()

        y_text = "multiplication"

    else:
      y_text = ""
    return y_text

def send_message(message):
   response = respond(message)
   print(bot_template.format(response))


        