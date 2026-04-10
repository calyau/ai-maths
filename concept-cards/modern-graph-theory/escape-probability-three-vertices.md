---
concept: Escape Probability to One of Two Targets
slug: escape-probability-three-vertices
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 316
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "P_esc(s -> t < u)"
prerequisites:
  - escape-probability
extends:
  - escape-probability
related:
  - reciprocity-law-random-walks
contrasts_with: []
answers_questions:
  - "How do I compute hitting times for a random walk?"
---

# Quick Definition
$P_{\text{esc}}(s \to t < u)$ is the probability that starting at $s$, the walk reaches $t$ before either $s$ or $u$. Theorem 21 links this to currents: setting $s$ at potential 1, $t$ and $u$ at 0, the current leaving at $t$ is $d(s) P_{\text{esc}}(s \to t < u)$.

# Core Definition
Theorem 21 (p. 316): "Let $s$, $t$ and $u$ be distinct vertices of a graph. Set $s$ at potential 1, and $t$ and $u$ at potential 0. Then a current of size $d(s) P_{\text{esc}}(s \to t < u)$ leaves $G$ at $t$."

# Prerequisites
- **Escape probability** — Generalized to three vertices

# Key Properties
1. $d(s) P_{\text{esc}}(s \to t < u) = d(t) P_{\text{esc}}(t \to s < u)$ (Theorem 22, reciprocity)
2. Connected to electrical network with two sinks

# Relationships
## Builds Upon
- **escape-probability**

## Related
- **reciprocity-law-random-walks** — $d(s) P_{\text{esc}}(s \to t < u) = d(t) P_{\text{esc}}(t \to s < u)$

# Source Reference
Chapter IX, Section IX.3, Theorems 21-22, pages 316-317.

# Verification Notes
- Definition source: Direct from Theorems 21-22
- Confidence rationale: Explicit theorems
- Uncertainties: None
- Cross-reference status: Verified
