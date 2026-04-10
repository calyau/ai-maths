---
concept: Possible Partner in Stable Matching
slug: possible-girl
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
  - "possible girl"
  - "S(a)"
prerequisites:
  - stable-matching
extends: []
related:
  - optimal-stable-matching
  - gale-shapley-algorithm
contrasts_with: []
answers_questions:
  - "What is a possible partner in stable matching theory?"
---

# Quick Definition
$S(a)$ is the set of girls that boy $a$ could marry in some stable matching — the set of "possible" girls for $a$.

# Core Definition
Denote by $S(a)$ the set of girls a boy $a$ could marry in some stable matching: this is the set of possible girls for $a$. In the Gale-Shapley algorithm, no girl in $S(a)$ ever refuses $a$, so every boy marries his favourite possible girl (Bollobás, p. 98).

# Prerequisites
- **Stable matching** — Possible partners across all stable matchings

# Key Properties
1. $|S(a)| \ge 1$ for every matched boy (by Theorem 18)
2. In the $V_1$-optimal matching, $a$ marries his top choice in $S(a)$
3. No possible girl refuses $a$ during the Gale-Shapley algorithm

# Context & Application
The concept of possible partners is key to proving optimality of the Gale-Shapley algorithm.

# Examples
**Example** (p. 98): If boy $a$ is refused by possible girl $A$ during the algorithm, another suitor $b$ must prefer $A$ to all his possible girls, contradicting the existence of a stable matching where $a$ marries $A$ and $b$ marries someone else.

# Relationships
## Enables
- **optimal-stable-matching** — Every boy gets his best possible partner

# Source Reference
Chapter III, Section III.5, page 98.

# Verification Notes
- Definition source: Direct from p. 98
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
