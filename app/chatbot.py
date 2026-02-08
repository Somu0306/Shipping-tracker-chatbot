import string
from app.tracker import track_shipment

def chatbot_response(user_input, shipments):
    """
    Processes user input and returns chatbot response
    """

    # Lowercase input
    cleaned_input = user_input.lower()

    # Remove punctuation
    cleaned_input = cleaned_input.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = cleaned_input.split()

    for word in words:
        word = word.strip().upper()  # IMPORTANT FIX

        # Strict shipment ID pattern
        if word.startswith("SH") and word[2:].isdigit():
            return track_shipment(word, shipments)

    if "help" in cleaned_input:
        return (
            "🤖 I can help you track shipments.\n"
            "Examples:\n"
            "- track SH1001\n"
            "- where is my shipment SH1002?"
        )

    return "🔍 Please provide a valid Shipment ID (e.g., SH1001)."
