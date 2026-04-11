---
concept: Radical Extension
slug: radical-extension
category: galois-theory
subcategory: solvability
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 625
section: "14.7 Solvable and Radical Extensions"
extraction_confidence: high
aliases:
  - "extension by radicals"
prerequisites:
  - field-extension
extends: []
related:
  - solvable-extension
  - insolvability-of-quintic
contrasts_with: []
answers_questions:
  - "What is a radical extension?"
---

# Quick Definition
A radical extension is a tower $F = F_0 \subset F_1 \subset \cdots \subset F_k$ where each $F_{i+1} = F_i(\alpha_i)$ with $\alpha_i^{n_i} \in F_i$ for some positive integer $n_i$. A polynomial is solvable by radicals if its roots lie in some radical extension.

# Core Definition
A field extension K/F is a radical extension if there exists a tower $F = F_0 \subset F_1 \subset \cdots \subset F_k = K$ such that $F_{i+1} = F_i(\alpha_i)$ where $\alpha_i^{n_i} \in F_i$ for some $n_i \geq 1$. In other words, K is obtained by successively adjoining nth roots. A polynomial $f(x) \in F[x]$ is solvable by radicals if the splitting field of f is contained in some radical extension of F (Dummit & Foote, pp. 625-627).

# Prerequisites
- **field-extension** — Radical extensions are field extensions

# Key Properties
1. Solving by radicals means expressing roots using $+, -, \times, \div$ and nth roots
2. The quadratic formula gives radicals for degree 2
3. Cardano's formula gives radicals for degree 3
4. Ferrari's method gives radicals for degree 4
5. General degree $\geq 5$: not always solvable by radicals

# Relationships
## Builds Upon
- **field-extension**

## Enables
- **solvable-extension** — Solvability = Galois group is solvable
- **insolvability-of-quintic** — $S_5$ is not solvable

# Source Reference
Chapter 14, Section 14.7, pp. 625-627.

# Verification Notes
- Confidence: HIGH — explicit definition
