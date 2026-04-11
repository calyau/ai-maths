---
concept: Insolvability of the Quintic
slug: insolvability-of-quintic
category: galois-theory
subcategory: solvability
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 635
section: "14.7 Solvable and Radical Extensions"
extraction_confidence: high
aliases:
  - "Abel-Ruffini theorem"
  - "insolvability of the general quintic"
prerequisites:
  - solvable-extension
  - solvable-group
  - galois-group
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Why can't the general quintic be solved by radicals?"
---

# Quick Definition
The general polynomial of degree $\geq 5$ cannot be solved by radicals because $S_n$ is not a solvable group for $n \geq 5$. Specific quintics like $x^5 - 6x + 3$ over $\mathbb{Q}$ have Galois group $S_5$, hence are not solvable by radicals.

# Core Definition
(Corollary, p. 635) For $n \geq 5$, $S_n$ is not a solvable group (since $A_n$ is simple and non-abelian for $n \geq 5$). Since the Galois group of the general polynomial of degree n over $F(x_1, \ldots, x_n)$ is $S_n$, it follows that the general polynomial of degree $\geq 5$ is not solvable by radicals. Specific examples: $x^5 - 6x + 3$ has Galois group $S_5$ over $\mathbb{Q}$ (Dummit & Foote, pp. 635-637).

# Prerequisites
- **solvable-extension** — Solvability by radicals requires solvable Galois group
- **solvable-group** — $S_n$ is not solvable for $n \geq 5$
- **galois-group** — Must compute the Galois group

# Key Properties
1. $A_n$ is simple for $n \geq 5$, so $S_n$ is not solvable
2. The general polynomial of degree n has Galois group $S_n$
3. There exist specific quintics over $\mathbb{Q}$ with Galois group $S_5$
4. Some specific quintics DO have solvable Galois groups (e.g., $x^5 - 2$)

# Context & Application
This is one of the most celebrated results in mathematics, proved independently by Abel and Galois. It resolved a centuries-old question about solving polynomial equations by formulas involving radicals.

# Relationships
## Builds Upon
- **solvable-extension**, **solvable-group**, **galois-group**

# Source Reference
Chapter 14, Section 14.7, pp. 635-637.

# Verification Notes
- Confidence: HIGH — classic result with explicit examples
