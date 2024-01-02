def handle_response(message) -> str:
    msg = message.lower()

    if msg == 'hello' or msg == 'hi':
        return 'Hey there'
    
    if(msg == 'thank you'):
        return 'Its my pleasure to help you.'

    if msg == 'how are you?':
        return 'I am good. How you are doing?'
    