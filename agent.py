def generate_agent_reply(history):
    if len(history) < 3:
        return "Why is my account being blocked?"
    elif len(history) < 6:
        return "Can you explain the process clearly?"
    else:
        return "Okay tell me where I need to send the money."
