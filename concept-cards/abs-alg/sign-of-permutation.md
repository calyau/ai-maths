---
concept: Sign of a Permutation
slug: sign-of-permutation
category: group-theory
subcategory: permutations
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Quotient Groups and Homomorphisms"
chapter_number: 3
pdf_page: 73
section: "3.5 Transpositions and the Alternating Group"
extraction_confidence: high
aliases:
  - "parity"
  - "$\\epsilon(\\sigma)$"
  - "even permutation"
  - "odd permutation"
prerequisites:
  - symmetric-group
  - transposition
extends: []
related:
  - alternating-group
  - homomorphism
contrasts_with: []
answers_questions:
  - "What is the sign of a permutation?"
  - "How do you determine if a permutation is even or odd?"
---

# Quick Definition
The sign $\epsilon(\sigma) \in \{\pm 1\}$ of a permutation $\sigma$ is $+1$ if $\sigma$ is a product of an even number of transpositions and $-1$ if odd. The map $\epsilon: S_n \to \{\pm 1\}$ is a surjective homomorphism.

# Core Definition
For $\sigma \in S_n$, let $\Delta = \prod_{i<j}(x_i - x_j)$. Then $\sigma(\Delta) = \pm\Delta$. The *sign* of $\sigma$ is $\epsilon(\sigma) = +1$ if $\sigma(\Delta) = \Delta$ and $-1$ if $\sigma(\Delta) = -\Delta$. A permutation is *even* if $\epsilon(\sigma) = 1$ and *odd* if $\epsilon(\sigma) = -1$. The map $\epsilon: S_n \to \{\pm 1\}$ is a homomorphism (Proposition 23). All transpositions are odd (Proposition 24). A permutation is odd iff its cycle decomposition has an odd number of even-length cycles (Proposition 25) (Dummit & Foote, pp. 108-112).

# Prerequisites
- **Symmetric group**, **Transposition**

# Key Properties
1. $\epsilon$ is a surjective homomorphism
2. $\epsilon((ij)) = -1$ for all transpositions
3. An m-cycle is odd iff m is even
4. $\sigma$ is odd iff it has an odd number of even-length cycles
5. $\ker\epsilon = A_n$ (the alternating group)
6. (even)(even) = (odd)(odd) = even; (even)(odd) = odd

# Context & Application
The sign homomorphism defines the alternating group $A_n = \ker\epsilon$ and establishes that $S_n/A_n \cong \mathbb{Z}_2$. It is used in the definition of determinants and in Galois theory.

# Examples
**Example 1** (p. 110): $(1\ 2\ 3\ 4)$ has sign $-1$ (a 4-cycle is odd since 4 is even).
**Example 2** (p. 112): $(1\ 2\ 3)(4\ 5)$ has one even-length cycle, so it is odd.

# Relationships
## Builds Upon
- **symmetric-group**, **transposition**

## Enables
- **alternating-group** — $A_n = \ker\epsilon$

## Related
- **homomorphism** — $\epsilon$ is a homomorphism

# Source Reference
Chapter 3, Section 3.5, pages 108-112, Propositions 23-25.

# Verification Notes
- Definition source: direct from source pp. 108-109
- Confidence rationale: explicitly defined with propositions
- Uncertainties: none
- Cross-reference status: verified
