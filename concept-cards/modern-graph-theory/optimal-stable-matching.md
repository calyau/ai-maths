---
concept: Optimal Stable Matching
slug: optimal-stable-matching
category: matchings
subcategory: stable-matchings
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "V₁-optimal stable matching"
  - "boy-optimal matching"
  - "Theorem 20"
prerequisites:
  - stable-matching
  - gale-shapley-algorithm
  - stable-matching-equal-cardinality
extends:
  - stable-matching-existence
related:
  - pessimal-stable-matching
  - college-admissions-problem
contrasts_with:
  - pessimal-stable-matching
answers_questions:
  - "Is there a best stable matching for one side?"
---

# Quick Definition
The $V_1$-optimal stable matching gives every boy his best possible partner across all stable matchings. It is produced by the Gale-Shapley algorithm and is simultaneously $V_2$-pessimal.

# Core Definition
**Theorem 20**: For every assignment of preferences in an $n \times n$ complete bipartite graph, there is a $V_1$-optimal stable matching. A stable matching $M$ is $V_1$-optimal if for every stable matching $M'$ and every $a \in V_1$, if $aB \in M'$ then $aA \in M$ with $a$ preferring $A$ to $B$ (or $A = B$). The Gale-Shapley algorithm produces this matching: no girl in a boy's "possible set" $S(a)$ ever refuses him (Bollobás, pp. 98-99).

# Prerequisites
- **Stable matching** — The objects being optimized over
- **Gale-Shapley algorithm** — Produces the optimal matching
- **Equal cardinality of stable matchings** — All match same vertices

# Key Properties
1. Unique if it exists (and it always exists)
2. Produced by the Gale-Shapley algorithm with boys proposing
3. Every boy marries his favourite "possible" girl
4. The $V_1$-optimal matching is precisely the $V_2$-pessimal matching (Corollary 19)
5. Swapping proposers gives the $V_2$-optimal ($V_1$-pessimal) matching

# Construction / Recognition
1. Run the Gale-Shapley algorithm with $V_1$ proposing
2. The result is the $V_1$-optimal stable matching

# Context & Application
The optimality result shows that the proposing side in the Gale-Shapley algorithm gets the best possible outcome, while the receiving side gets the worst. This has practical implications for mechanism design.

# Examples
**Example** (p. 98): In the proof, if boy $a$ is refused by a possible girl $A$ during the algorithm, it would be because $A$ prefers suitor $b$ to $a$. But $b$ hasn't been refused by any possible girl yet, so $b$ prefers $A$ to all his possible girls — contradicting the stability of any matching where $a$ marries $A$.

# Relationships
## Builds Upon
- **gale-shapley-algorithm** — Produces the optimal matching

## Contrasts With
- **pessimal-stable-matching** — The same matching viewed from the other side

## Related
- **college-admissions-problem** — Application of optimal matching

# Source Reference
Chapter III, Section III.5, pages 98-99. Theorem 20.

# Verification Notes
- Definition source: Direct from pp. 98-99
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
