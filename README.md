# ReAct Code-Fixing Agent with Gemini

A Gemini-powered ReAct code-fixing agent built from scratch.
The agent explores Python projects, identifies bugs, modifies
source files, and executes tests using controlled tools.

## Features

- Gemini API integration and function calling
- ReAct-based agent execution loop
- Controlled file exploration and modification
- Automated pytest execution
- Tool argument validation
- Workspace path security
- Structured Working Memory
- Token usage tracking
- Context compaction
- Session persistence

## Architecture

The agent follows a ReAct workflow:

1. Receive a debugging task.
2. Inspect project files using tools.
3. Identify potential issues.
4. Modify source code.
5. Execute tests.
6. Evaluate results and continue if necessary.

Working Memory retains structured information about the
project, inspected files, modifications, and test status.

Context compaction preserves the original task and relevant
recent interactions while reducing conversation history.

## Experiments

Three configurations were evaluated on the same Python
debugging task.

| Configuration | Total Tokens | Tests Passed |
|---|---:|---:|
| Baseline | 20,448 | 5/5 |
| Working Memory | 19,096 | 5/5 |
| Working Memory + Compaction | 18,670 | 5/5 |

The memory-enabled configuration with compaction performed
six context compactions.

These results represent a small sanity experiment, not a
statistically controlled benchmark.

## Repository Structure

- `notebooks/`: Complete implementation notebook
- `sample_project/`: Multi-file Python project used for testing
- `results/`: Experimental comparison

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Gemini API key as an environment variable:

```python
import os
os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY"
```

In Google Colab, you can instead configure the key through
Colab Secrets.

## Model

The implementation uses Gemini through an OpenAI-compatible
API interface.

## Limitations

- Tested on a small Python debugging project.
- Token estimates used for context management are heuristic.
- Agent behavior and token usage may vary across runs.
- This is a prototype, not a production sandbox.

## License

MIT
