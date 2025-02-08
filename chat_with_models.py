# chat_with_models.py
from emotional_analysis import EmotionalStateAnalyzer
from response_generator import ResponseGenerator

def chat():
    emotional_analyzer = EmotionalStateAnalyzer()
    responder = ResponseGenerator()

    print("Start chatting with the AI. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # FIX: Use predict() instead of assess_emotional_state()
        emotional_state = emotional_analyzer.predict(user_input)  
        print(f"Emotion: {emotional_state}")

        response = responder.generate_response(emotional_state, user_input)
        print(f"Response: {response}")

if __name__ == "__main__":
    chat()
