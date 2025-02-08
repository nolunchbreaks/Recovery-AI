import random

class ResponseGenerator:
    def generate_response(self, emotional_state: dict, user_input: str) -> str:
        sadness = emotional_state.get('sadness', 0)
        hope = emotional_state.get('hope', 0)
        anxiety = emotional_state.get('anxiety', 0)
        overall = emotional_state.get('overall_score', 0)

        if sadness > 0.4:
            return random.choice([
                "I'm here for you. Can you share what's making you feel this way?",
                "It's okay to feel sad sometimes. Do you want to talk about it?",
                "You're not alone in this. What’s been on your mind?"
            ])
        elif hope > 0.5:
            return random.choice([
                "I love your positivity! What’s something you're looking forward to?",
                "Hope is a powerful thing! What keeps you going?",
                "It’s great to hear that! Tell me more about what excites you."
            ])
        elif anxiety > 0.4:
            return random.choice([
                "I can sense some worry. Want to talk about what’s on your mind?",
                "Sometimes deep breaths help. Would you like some guidance on relaxation?",
                "You’re doing your best, and that’s enough. What’s causing you stress?"
            ])
        else:
            return random.choice([
                "I appreciate you sharing. How can I support you today?",
                "That’s interesting! Tell me more about it.",
                "I’m here to listen. What’s on your mind?"
            ])
