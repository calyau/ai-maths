---
concept: "Menger's Theorem (Second Proof)"
slug: mengers-theorem-second-proof
category: connectivity
subcategory: proof-techniques
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "second proof of vertex form"
prerequisites:
  - mengers-theorem
extends: []
related:
  - max-flow-min-cut-theorem
contrasts_with: []
answers_questions:
  - "How is Menger's theorem proved without flows?"
---

# Quick Definition
The second proof of Menger's vertex form proceeds by contradiction on a minimal counterexample, analyzing the structure of separating sets to derive contradictions about common neighbours of $s$ and $t$.

# Core Definition
The second proof uses induction on the minimum separator size $k$. For a minimal counterexample $G$ (minimum $k$, then minimum edges), the proof shows that for any $k$-separator $W$, either $s$ or $t$ is adjacent to all vertices of $W$. Analysis of a shortest $s$-$t$ path and modified separators leads to a contradiction: $s$ and $t$ must have a common neighbour, but no such vertex can be adjacent to both (Bollobás, pp. 83-84).

# Prerequisites
- **Menger's theorem** — The theorem being reproved

# Key Properties
1. Independent of max-flow min-cut (proves from first principles)
2. Uses minimality: smallest $k$ with counterexample, then fewest edges
3. Key technique: collapsing components to single vertices ($G_s$ construction)
4. Shows separating sets have strong structural constraints

# Context & Application
"Since... the max-flow min-cut theorem can also be deduced from Menger's theorem, we shall give another proof of the vertex form from first principles" (p. 83).

# Examples
**Example** (pp. 83-84): Take shortest $s$-$t$ path $sx_1x_2\cdots x_\ell t$ with $\ell \ge 2$. Removing edge $x_1x_2$ gives separator $W_0$ of size $k-1$. Then $W_1 = \{x_1\} \cup W_0$ and $W_2 = \{x_2\} \cup W_0$ are both $k$-separators, forcing $s$ and $t$ to have common neighbours in $W_0$.

# Relationships
## Builds Upon
- **mengers-theorem** — Alternative proof

# Source Reference
Chapter III, Section III.2, pages 83-84.

# Verification Notes
- Definition source: Synthesized from proof
- Confidence rationale: Complete proof given
- Uncertainties: None
- Cross-reference status: Verified
