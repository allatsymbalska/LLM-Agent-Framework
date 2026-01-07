# LLM Customer Query Router

A Python framework that routes customer queries to the correct agent using a Large Language Model.

**Agents:**
- FAQ Agent – answers general store questions.  
- Order Status Agent – checks order status.

---

## Setup & Run Instructions

1. **Clone the repository:**

```bash
git clone <https://github.com/allatsymbalska/LLM-Agent-Framework.git >
cd LLM-Agent-Router 

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

# Set environment variables

export OPENAI_API_KEY="your_openai_key"
export GOOGLE_API_KEY="your_google_key"
export ANTHROPIC_API_KEY="your_anthropic_key"

# Run the main program
python main.py

Evaluation
The system was evaluated using 7 test customer queries with predefined expected intents.
Metrics
Accuracy: correctly routed queries / total queries
Average Time: average response time per query in seconds

| Model  | Correct | Total | Accuracy | Avg Time (s) |
| ------ | ------- | ----- | -------- | ------------ |
| GPT    | 6       | 7     | 85.7%    | 1.220        |
| Claude | 4       | 7     | 57.1%    | 0.897        |
| Gemini | 6       | 7     | 85.7%    | 0.686        |


## Conclusion

**Best performing model: Gemini**

- High routing accuracy (**85.7%**)
- Fastest average response time (**0.686 seconds**)

**Reasoning:**  
Gemini provides reliable intent routing while outperforming other models in speed.  
Although GPT achieves similar accuracy, Gemini’s faster response time makes it more suitable for real-time customer query handling.  
Claude shows lower accuracy and is therefore less optimal for this use case.
