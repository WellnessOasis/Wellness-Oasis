from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import ask, append_interaction_to_chat_log

app = Flask(__name__)

app.secret_key = "019phungalala694200"
app.config['SECRET KEY'] =  '019phungalala694200'


@app.route('/chatbot', methods=['POST'])

def bot():
    incoming_msg = request.values['BODY']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)



