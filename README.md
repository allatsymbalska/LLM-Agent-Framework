# LLM Agent Framework

A Python framework that routes customer queries to the correct agent using a Large Language Model.

**Agents:**
- FAQ Agent – answers general store questions.  
- Order Status Agent – checks order status.


## Setup & Run Instructions

1. **Clone the repository:**

```bash
git clone <https://github.com/allatsymbalska/LLM-Agent-Framework.git >
cd LLM-Agent-Router 
```

2. **Create a virtual environment**

```bash
# Mac / Linux
python3 -m venv .venv

# Windows (PowerShell)
python -m venv .venv

```

3. **Activate the virtual environment**
   
```bash
# Mac / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Command Prompt)
.venv\Scripts\activate.bat
```

4. **Install dependencies**
```
pip install -r requirements.txt
```

5. **Set environment variables**

```
# Mac / Linux
export OPENAI_API_KEY="your_openai_key"
export GOOGLE_API_KEY="your_google_key"
export ANTHROPIC_API_KEY="your_anthropic_key"

# Windows (PowerShell)
setx OPENAI_API_KEY "your_openai_key"
setx GOOGLE_API_KEY "your_google_key"
setx ANTHROPIC_API_KEY "your_anthropic_key"

```

6. **Run the main program**
```
python main.py
```

## Evaluation

The system was evaluated using 7 test customer queries with predefined expected intents.

**Metrics**

- Accuracy: correctly routed queries / total queries

- Average Time: average response time per query in seconds

| Model  | Correct | Total | Accuracy | Avg Time (s) |
| ------ | ------- | ----- | -------- | ------------ |
| GPT    | 7       | 7     | 100.0%   | 1.027        |
| Gemini | 7       | 7     | 100.0%   | 0.674        |
| Claude | 5       | 7     | 71.4%    | 1.243        |


## Conclusion

**Best performing model: Gemini**

- High routing accuracy: 100%
- Fastest average response time: 0.674 seconds
  
Reasoning:
- Gemini demonstrates perfect intent routing while providing the fastest response time, making it ideal for real-time customer query handling.
- GPT also achieves perfect accuracy but is slightly slower.
- Claude shows lower accuracy and slower performance, making it less suitable for this use case.
