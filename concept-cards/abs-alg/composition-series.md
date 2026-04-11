---
concept: Composition Series
slug: composition-series
category: group-theory
subcategory: structure-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.4 Composition Series and the Holder Program"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-subgroup
  - quotient-group
  - simple-group
extends: []
related:
  - jordan-holder-theorem
  - holder-program
  - solvable-group
contrasts_with: []
answers_questions:
  - "What is a composition series?"
  - "How do composition series relate to simple groups?"
---

# Quick Definition
A composition series of G is a chain $1 = N_0 \trianglelefteq N_1 \trianglelefteq \cdots \trianglelefteq N_k = G$ where each successive quotient $N_{i+1}/N_i$ is simple. The quotients are the composition factors.

# Core Definition
A sequence $1 = N_0 \leq N_1 \leq \cdots \leq N_k = G$ is a *composition series* if $N_i \trianglelefteq N_{i+1}$ and $N_{i+1}/N_i$ is a simple group for each $0 \leq i \leq k-1$. The quotients $N_{i+1}/N_i$ are the *composition factors*. Note: $N_i$ need only be normal in $N_{i+1}$, not in G. By the Jordan-Holder Theorem, the composition factors are unique up to permutation and isomorphism (Dummit & Foote, pp. 102-104).

# Prerequisites
- **Normal subgroup**, **Quotient group**, **Simple group**

# Key Properties
1. Every finite group with $|G| > 1$ has a composition series
2. The composition factors are unique up to isomorphism and reordering (Jordan-Holder)
3. Different composition series may have the same factors in different orders
4. Non-isomorphic groups may have identical lists of composition factors

# Examples
**Example 1** (p. 103): $1 \leq \langle s \rangle \leq \langle s, r^2 \rangle \leq D_8$ and $1 \leq \langle r^2 \rangle \leq \langle r \rangle \leq D_8$ are two composition series for $D_8$, both with factors $Z_2, Z_2, Z_2$.

# Relationships
## Builds Upon
- **normal-subgroup**, **quotient-group**, **simple-group**

## Enables
- **holder-program** — classify groups by their composition factors

## Related
- **jordan-holder-theorem** — uniqueness of composition factors
- **solvable-group** — all composition factors of prime order

# Source Reference
Chapter 3, Section 3.4, pages 102-106, Theorem 22 (Jordan-Holder).

# Verification Notes
- Definition source: direct from source pp. 102-103
- Confidence rationale: explicitly defined with theorem
- Uncertainties: none
- Cross-reference status: verified
