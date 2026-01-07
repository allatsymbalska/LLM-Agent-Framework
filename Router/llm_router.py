class LLMRouter:
    """
    Routes user queries to the correct agent using LLM intent classification.
    """

    def __init__(self, llm_classifier, faq_agent, order_status_agent):
        self.llm_classifier = llm_classifier

        # map intents to agents
        self.agents = {
            "FAQ": faq_agent,
            "ORDER_STATUS": order_status_agent,
        }

    def route(self, query: str) -> str:
        """
        Routes a user query to the appropriate agent.

        Args:
            query (str): User input

        Returns:
            str: Response from the selected agent
        """
        if not query or not query.strip():
            return "Please enter a valid question."

        try:
            # classify intent using LLM
            intent = self.llm_classifier(query)

        except Exception as e:
            # LLM failure
            return f"Routing error: {e}"

        # route to the correct agent
        agent = self.agents.get(intent)

        if not agent:
            # should not happen if wrappers validate output
            return "Sorry, I couldn't understand your request."

        return agent.handle(query)
