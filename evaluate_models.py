# evaluation of LLM Router

# => routing accuracy and execution time 
# using a JSON file of test queries and expected intents


import json
import time
from Agents.faq_agent import FAQAgent
from Agents.order_status_agent import OrderStatusAgent
from Router.llm_router import LLMRouter
from llm_wrappers import gpt_llm, gemini_llm, claude_llm


# load test queries from JSON
with open("test_queries.json", "r") as f:
    test_data = json.load(f)  


# initialize agents
faq_agent = FAQAgent()
order_agent = OrderStatusAgent()


# LLMs to evaluate
llms = {
    "GPT": gpt_llm,
    "Gemini": gemini_llm,
    "Claude": claude_llm
}


# evaluation loop
print("Evaluating LLM router accuracy and time per query...\n")
print(f"{'Model':10} | {'Correct':7} | {'Total':5} | {'Accuracy':8} | {'Avg Time (s)':12}")
print("-" * 60)

for llm_name, llm_func in llms.items():
    router = LLMRouter(llm_func, faq_agent, order_agent)

    correct = 0
    total = len(test_data)
    total_time = 0.0

    for item in test_data:
        query = item["query"]
        expected_intent = item["expected"]

        try:
            start_time = time.time() # start timing
            predicted_response = router.route(query)
            end_time = time.time() # end timing

            elapsed = end_time - start_time
            total_time += elapsed

            # determine predicted intent based on which agent responded
            if predicted_response in faq_agent.faq_data.values():
                predicted_intent = "FAQ"
            else:
                predicted_intent = "ORDER_STATUS"

            if predicted_intent == expected_intent:
                correct += 1

        except RuntimeError as e:
            print(f"Error for model {llm_name} on query '{query}': {e}")

    accuracy = (correct / total) * 100
    avg_time = total_time / total
    
    print(f"{llm_name:10} | {correct:7} | {total:5} | {accuracy:7.1f}% | {avg_time:12.3f}")
