"""Haggling prompts and strategies for negotiation scenarios"""

HAGGLING_STRATEGIES = {
    "car_negotiation": {
        "scenario": "buying a used car",
        "initial_price": 15000,
        "seller_limits": {
            "min_price": 12000,
            "max_price": 18000
        },
        "opening_lines": [
            "I've seen similar models listed for less online",
            "What's your best price if I can pay cash today?",
            "There's some wear on the interior, can you come down?"
        ],
        "negotiation_tactics": [
            "Point out maintenance costs",
            "Reference market prices",
            "Highlight visible defects",
            "Offer cash as incentive"
        ]
    },
    
    "real_estate": {
        "scenario": "buying a house",
        "initial_price": 500000,
        "seller_limits": {
            "min_price": 450000,
            "max_price": 550000
        },
        "opening_lines": [
            "The market analysis shows similar homes at lower prices",
            "What repairs are needed based on the inspection?",
            "Can you include closing costs in the negotiation?"
        ],
        "negotiation_tactics": [
            "Reference inspection report",
            "Cite comparable sales",
            "Discuss market conditions",
            "Negotiate closing costs"
        ]
    },
    
    "salary_negotiation": {
        "scenario": "negotiating salary for a job offer",
        "initial_price": 80000,
        "seller_limits": {
            "min_price": 75000,
            "max_price": 95000
        },
        "opening_lines": [
            "Based on my experience and market rates, I was expecting more",
            "Can we discuss the total compensation package?",
            "What flexibility do you have on the salary offer?"
        ],
        "negotiation_tactics": [
            "Highlight relevant experience",
            "Reference industry standards",
            "Discuss additional benefits",
            "Show market data for your role"
        ]
    }
}

def get_scenario(scenario_name: str) -> dict:
    """Get haggling scenario by name"""
    return HAGGLING_STRATEGIES.get(scenario_name)

def get_all_scenarios() -> list:
    """Get all available scenarios"""
    return list(HAGGLING_STRATEGIES.keys())