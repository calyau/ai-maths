---
concept: Solvable Extension
slug: solvable-extension
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
  - "solvability by radicals"
prerequisites:
  - galois-extension
  - galois-group
  - solvable-group
  - radical-extension
extends: []
related:
  - insolvability-of-quintic
contrasts_with: []
answers_questions:
  - "What is solvability by radicals?"
---

# Quick Definition
A polynomial $f(x) \in F[x]$ is solvable by radicals if its roots lie in a radical extension of F (obtained by successively adjoining nth roots). This holds iff the Galois group of $f(x)$ is a solvable group.

# Core Definition
A radical extension is a tower $F = F_0 \subset F_1 \subset \cdots \subset F_k$ where each $F_{i+1} = F_i(\alpha_i)$ with $\alpha_i^{n_i} \in F_i$. A polynomial is solvable by radicals if its splitting field is contained in some radical extension. The fundamental theorem: $f(x) \in F[x]$ is solvable by radicals iff the Galois group of $f(x)$ over F is a solvable group (assuming F contains appropriate roots of unity, or char F = 0) (Dummit & Foote, pp. 625-635).

# Prerequisites
- **galois-extension**, **galois-group** — The Galois group determines solvability
- **solvable-group** — The group-theoretic condition
- **radical-extension** — The field-theoretic condition

# Key Properties
1. Solvable by radicals $\iff$ Galois group is solvable (over characteristic 0)
2. Polynomials of degree $\leq 4$ always have solvable Galois groups ($S_n$ is solvable for $n \leq 4$)
3. General polynomials of degree $\geq 5$ are NOT solvable by radicals ($S_n$ is not solvable for $n \geq 5$)
4. Specific degree 5 polynomials may or may not be solvable

# Relationships
## Builds Upon
- **galois-group**, **solvable-group**, **radical-extension**

## Enables
- **insolvability-of-quintic** — The general quintic is not solvable

# Source Reference
Chapter 14, Section 14.7, pp. 625-635.

# Verification Notes
- Confidence: HIGH — central theorem with proof
