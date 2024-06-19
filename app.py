# chatbot.py
from flask import Flask, request, jsonify, render_template
import re
app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

def get_response(user_input):
    user_input = user_input.lower()
    
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"
    
    elif re.search(r'\bhow are you\b|\bhow\'s it going\b', user_input):
        return "I'm a bot, so I don't have feelings, but thank you for asking! How can I assist you?"
    
    elif re.search(r'\bbye\b|\bgoodbye\b|\bsee you\b', user_input):
        return "Goodbye! Have a great day!"
    
    elif re.search(r'\bweather\b', user_input):
        return "I'm not currently connected to a weather service, but it's always a good idea to check a weather app!"
    
    elif re.search(r'\btime\b', user_input):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."
    
    elif re.search(r'\bname\b', user_input):
        return "I'm Nova, your virtual assistant."
    
    elif re.search(r'\bjoke\b|\bfunny\b', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    
    elif re.search(r'\bhelp\b', user_input):
        return ("Sure! I can assist you with the following:\n"
                "1. Greet you (say hello, hi, etc.)\n"
                "2. Tell you the current time\n"
                "3. Tell a joke\n"
                "4. Provide information about myself\n"
                "5. Discuss the weather (though I can't provide live updates)\n"
                "Just type what you want to know!")
    
    else:
        return "I'm not sure how to respond to that. Can you please rephrase or type 'help' for assistance?"

if __name__ == "__main__":
    app.run(debug=True)
