# customer bot
# routes queries from JSON

import json
from Agents.faq_agent import FAQAgent
from Agents.order_status_agent import OrderStatusAgent
from Router.llm_router import LLMRouter
from llm_wrappers import gpt_llm, claude_llm, gemini_llm


# select LLM for testing
llm_func = gpt_llm
# llm_func = gemini_llm
# llm_func = claude_llm


# load test queries from JSON
with open("test_queries.json", "r") as f:
    test_queries = json.load(f)  


def main():
    # create agent instances
    faq_agent = FAQAgent()
    order_agent = OrderStatusAgent()

    # initialize router with chosen LLM and agents
    router = LLMRouter(llm_func, faq_agent, order_agent)

    print(f"Testing LLM router with {llm_func.__name__}\n")

    # route each test query and display results
    for item in test_queries:
        query_text = item["query"]
        expected_intent = item["expected"]

        try:
            response = router.route(query_text)

            print(f"Query: {query_text}")
            print(f"Response: {response}")
            print(f"Expected intent: {expected_intent}\n")

        except RuntimeError as e:
            print(f"Error for query '{query_text}': {e}")
            print("Check your API key or LLM configuration.\n")


if __name__ == "__main__":
    main()
    