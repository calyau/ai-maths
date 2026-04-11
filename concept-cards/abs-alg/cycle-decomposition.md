---
concept: Cycle Decomposition
slug: cycle-decomposition
category: group-theory
subcategory: permutations
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Groups"
chapter_number: 1
pdf_page: 26
section: "1.3 Symmetric Groups"
extraction_confidence: high
aliases:
  - "cycle notation"
  - "disjoint cycle decomposition"
prerequisites:
  - symmetric-group
extends: []
related:
  - transposition
  - alternating-group
contrasts_with: []
answers_questions:
  - "What is the cycle decomposition of a permutation?"
  - "How do you compute the order of a permutation from its cycle decomposition?"
---

# Quick Definition
Every permutation in $S_n$ can be written uniquely (up to order of cycles and cyclic rotation within cycles) as a product of disjoint cycles. The order of the permutation is the l.c.m. of the cycle lengths.

# Core Definition
A *cycle* $(a_1\ a_2\ \ldots\ a_m)$ is the permutation sending $a_i \to a_{i+1}$ for $1 \leq i \leq m-1$ and $a_m \to a_1$. A cycle of length m is an *m-cycle*. Two cycles are *disjoint* if they share no elements. Every $\sigma \in S_n$ has a unique *cycle decomposition* as a product of disjoint cycles (up to rearranging cycles and cyclically permuting elements within each cycle). By convention, 1-cycles are omitted (Dummit & Foote, pp. 30-33).

# Prerequisites
- **Symmetric group** — cycle decomposition applies to elements of $S_n$

# Key Properties
1. Disjoint cycles commute
2. Cycle decomposition is essentially unique
3. The order of $\sigma$ equals the l.c.m. of its cycle lengths
4. The inverse of $(a_1\ a_2\ \ldots\ a_m)$ is $(a_m\ a_{m-1}\ \ldots\ a_1)$
5. An m-cycle can be written as $m-1$ transpositions: $(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2)$

# Construction / Recognition
## To Construct/Create:
1. Start with 1; follow the permutation until returning to 1 to get the first cycle
2. Pick the smallest unused element; repeat until all elements appear
3. Remove 1-cycles

# Context & Application
Cycle decomposition is the standard notation for permutations and makes computation of products, inverses, and orders straightforward.

# Examples
**Example 1** (p. 32): $\sigma \in S_{13}$ with $\sigma(1) = 12$, etc. has decomposition $(1\ 12\ 8\ 10\ 4)(2\ 13)(5\ 11\ 7)(6\ 9)$.
**Example 2** (p. 34): Order of $(1\ 12\ 8\ 10\ 4)(2\ 13)(5\ 11\ 7)(6\ 9)$ is $\text{lcm}(5,2,3,2) = 30$.

# Relationships
## Builds Upon
- **symmetric-group**

## Enables
- **transposition** — cycles decompose into transpositions
- **alternating-group** — parity is determined from cycle decomposition

# Common Errors
- **Error**: Computing products left-to-right instead of right-to-left. **Correction**: In $\sigma \tau$, apply $\tau$ first, then $\sigma$ to the result.

# Common Confusions
- **Confusion**: Thinking the cycle decomposition depends on the starting element. **Clarification**: $(1\ 2\ 3) = (2\ 3\ 1) = (3\ 1\ 2)$; by convention, start with the smallest element.

# Source Reference
Chapter 1: Introduction to Groups, Section 1.3, pages 30-36.

# Verification Notes
- Definition source: direct from source pp. 30-33
- Confidence rationale: algorithm and examples given explicitly
- Uncertainties: none
- Cross-reference status: verified
