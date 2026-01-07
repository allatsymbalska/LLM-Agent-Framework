class FAQAgent:
   
    def __init__(self, faq_data: dict | None = None):

         # mock faq database
        self.faq_data = faq_data or {
            "hours": "We are open from 9am to 8pm Mon-Fri, from 10am to 18pm on Saturday.",
            "return": "You can return items within 30 days of purchase.",
            "shipping": "Shipping takes 3–5 business days."
        }

    # handle user query and return FAQ answer
    def handle(self, query: str) -> str:
        
        # normalize query for keyword matching
        query = query.lower().strip()  

        # check if any keyword matches the query
        for key, answer in self.faq_data.items():
            if key in query:
                return answer

        # response if no keywords match
        return "I can help with store hours, returns, or shipping."
