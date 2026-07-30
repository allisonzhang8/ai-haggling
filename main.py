from src.negotiator import HagglingNegotiator
from src.prompts import get_scenario, get_all_scenarios

def main():
    """Main function to run haggling negotiation"""
    
    # Display available scenarios
    print("Available Haggling Scenarios:")
    scenarios = get_all_scenarios()
    for i, scenario in enumerate(scenarios, 1):
        print(f"{i}. {scenario}")
    
    # Choose scenario
    choice = input("\nSelect scenario (1-3): ").strip()
    scenario_map = {str(i): scenarios[i-1] for i in range(1, len(scenarios) + 1)}
    selected_scenario = scenario_map.get(choice, scenarios[0])
    
    # Get scenario details
    scenario_data = get_scenario(selected_scenario)
    
    # Initialize negotiator
    negotiator = HagglingNegotiator()
    negotiator.set_scenario(
        scenario=scenario_data["scenario"],
        initial_price=scenario_data["initial_price"],
        seller_limits=scenario_data["seller_limits"]
    )
    
    print(f"\n--- Starting Negotiation: {scenario_data['scenario'].upper()} ---")
    print(f"Initial Price: ${scenario_data['initial_price']:,.2f}\n")
    
    # Negotiation loop
    round_count = 0
    max_rounds = 5
    
    while round_count < max_rounds:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "done"]:
            break
        
        if not user_input:
            continue
        
        # Get AI response
        ai_response = negotiator.get_ai_response(user_input)
        print(f"Seller: {ai_response}\n")
        
        round_count += 1
    
    # Print summary
    summary = negotiator.get_negotiation_summary()
    print("\n--- Negotiation Summary ---")
    print(f"Scenario: {summary['scenario']}")
    print(f"Initial Price: ${summary['initial_price']:,.2f}")
    print(f"Rounds Completed: {summary['rounds_completed']}")
    print(f"Messages Exchanged: {summary['messages_exchanged']}")

if __name__ == "__main__":
    main()