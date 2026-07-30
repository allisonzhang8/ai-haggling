import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class HagglingNegotiator:
    """AI-powered haggling negotiator using OpenAI API"""
    
    def __init__(self, model="gpt-4o-mini"):
        """Initialize the negotiator with OpenAI client"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.conversation_history = []
        self.negotiation_data = {
            "initial_price": None,
            "final_price": None,
            "rounds": 0,
            "offers": []
        }
    
    def set_scenario(self, scenario: str, initial_price: float, seller_limits: dict):
        """Set up the negotiation scenario"""
        self.scenario = scenario
        self.negotiation_data["initial_price"] = initial_price
        self.seller_limits = seller_limits
        self.conversation_history = []
        
    def get_ai_response(self, user_message: str) -> str:
        """Get AI response for haggling conversation"""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self._build_system_prompt() + self.conversation_history,
            temperature=0.7,
            max_tokens=200
        )
        
        ai_message = response.choices[0].message.content
        self.conversation_history.append({
            "role": "assistant",
            "content": ai_message
        })
        
        self.negotiation_data["rounds"] += 1
        return ai_message
    
    def _build_system_prompt(self) -> list:
        """Build system prompt for the negotiation"""
        return [{
            "role": "system",
            "content": f"""You are a reluctant seller of {self.scenario}.
    Initial asking price: ${self.negotiation_data['initial_price']:,.2f}
    Your minimum acceptable price: ${self.seller_limits['min_price']:,.2f}
    Your maximum asking price: ${self.seller_limits['max_price']:,.2f}

    The buyer is trying to negotiate a lower price. Gradually lower your price as they negotiate, but don't go below your minimum.
    Be realistic and use tactics like mentioning maintenance costs, market value, or conditions of the item.
    Keep responses brief (1-2 sentences) and focused on the negotiation.
    Always counter-offer with a lower price when the buyer makes an offer."""
        }]
    
    def get_negotiation_summary(self) -> dict:
        """Get summary of the negotiation"""
        return {
            "scenario": self.scenario,
            "initial_price": self.negotiation_data["initial_price"],
            "rounds_completed": self.negotiation_data["rounds"],
            "messages_exchanged": len(self.conversation_history),
            "conversation": self.conversation_history
        }
    