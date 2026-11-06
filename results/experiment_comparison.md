# Experiment Comparison

| Configuration | Steps | Requests | Prompt Tokens | Completion Tokens | Total Tokens | Tests |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 12 | 13 | 20,039 | 409 | 20,448 | 5/5 |
| Working Memory | 11 | 12 | 18,762 | 334 | 19,096 | 5/5 |
| Working Memory + Compaction | 12 | 13 | 18,336 | 334 | 18,670 | 5/5 |

The memory-only experiment reduced total token usage by
approximately 6.6% compared with the baseline.

The memory + compaction experiment reduced total token usage
by approximately 8.7%.

The memory + compaction run reached its step limit with one
pending tool call, although the code fix was applied and all
five tests passed.

These results are from a single small sanity experiment.
