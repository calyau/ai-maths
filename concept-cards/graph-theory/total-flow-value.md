---
concept: Total Flow Value
slug: total-flow-value
category: network-flows
subcategory: network-flows
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 152
section: "6.2 Flows in networks"
extraction_confidence: high
aliases:
  - "flow value"
  - "|f|"
prerequisites:
  - flow-in-network
  - cut-in-network
related:
  - max-flow-min-cut-theorem
answers_questions:
  - "How is the value of a flow defined?"
---

# Quick Definition
The total value of a flow f in a network is |f| = f(s, V), the net flow leaving the source; it equals f(S, S-bar) for every cut (S, S-bar).

# Core Definition
Let f be a flow in a network N = (G, s, t, c). The **total value** of f, denoted |f|, is defined as f(s, V). By Proposition 6.2.1, every cut (S, S-bar) in N satisfies f(S, S-bar) = f(s, V), so the total value is independent of the choice of cut. (Diestel, p. 142)

# Prerequisites
- **Flow in network** — The total value is a property of a flow
- **Cut in network** — The value equals the net flow across any cut

# Key Properties
1. |f| = f(s, V) = f(S, S-bar) for every cut (S, S-bar) (Proposition 6.2.1)
2. |f| <= c(S, S-bar) for every cut — the value is bounded by every cut's capacity
3. |f| may formally be negative (swapping s and t changes the sign)
4. For integral flows, |f| is an integer

# Context & Application
The total flow value measures the net throughput of a network from source to sink. Maximizing this value is the central optimization problem in network flow theory.

# Examples
**Example** (p. 142): The flow shown in Figure 6.2.1 has total value 3.

# Relationships
## Builds Upon
- **Flow in network** — Total value is a derived quantity

## Enables
- **Max-flow min-cut theorem** — States that the maximum |f| equals the minimum cut capacity

# Source Reference
Chapter 6: Flows, Section 6.2, page 142 (pdf page 152). See Proposition 6.2.1.

# Verification Notes
- Definition: Directly from p. 142
- Confidence: HIGH — explicitly defined and named
