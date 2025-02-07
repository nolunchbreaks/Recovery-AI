# chat_with_models.py
from decision_engine import DecisionEngine
from emotional_analysis import EmotionalStateAnalyzer

def chat():
    decision_engine = DecisionEngine()
    emotional_analyzer = EmotionalStateAnalyzer()

    print("Start chatting with the AI. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        emotional_state = emotional_analyzer.assess_emotional_state(user_input, [])
        decision = decision_engine.evaluate_context(user_input, [])

        print(f"Emotion: {emotional_state}")
        print(f"Response: {decision['generated_response']}")

if __name__ == "__main__":
    chat()
