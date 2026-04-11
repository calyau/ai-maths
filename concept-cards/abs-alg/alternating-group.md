---
concept: Alternating Group
slug: alternating-group
category: group-theory
subcategory: important-groups
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
  - "$A_n$"
prerequisites:
  - symmetric-group
  - transposition
  - normal-subgroup
extends:
  - symmetric-group
related:
  - simple-group
  - sign-of-permutation
contrasts_with: []
answers_questions:
  - "What is the alternating group?"
  - "What is an even permutation?"
---

# Quick Definition
The alternating group $A_n$ is the subgroup of $S_n$ consisting of all even permutations (products of an even number of transpositions). It has order $n!/2$ and is a normal subgroup of $S_n$ with $S_n/A_n \cong Z_2$.

# Core Definition
The sign homomorphism $\epsilon: S_n \to \{\pm 1\}$ maps $\sigma$ to $+1$ if $\sigma(\Delta) = \Delta$ and $-1$ if $\sigma(\Delta) = -\Delta$, where $\Delta = \prod_{i < j}(x_i - x_j)$. A permutation is *even* if $\epsilon(\sigma) = 1$ and *odd* if $\epsilon(\sigma) = -1$. The *alternating group* $A_n = \ker\epsilon$ is the set of even permutations. Since $\epsilon$ is surjective, $|A_n| = n!/2$ and $S_n/A_n \cong Z_2$ (Dummit & Foote, pp. 107-112).

# Prerequisites
- **Symmetric group** — $A_n \leq S_n$
- **Transposition** — parity is defined via transpositions
- **Normal subgroup** — $A_n \trianglelefteq S_n$

# Key Properties
1. $|A_n| = n!/2$
2. $A_n \trianglelefteq S_n$ with $S_n/A_n \cong Z_2$
3. All transpositions are odd; an m-cycle is odd iff m is even
4. $\sigma$ is odd iff its cycle decomposition has an odd number of even-length cycles
5. $A_n$ is simple for $n \geq 5$
6. $A_3 \cong Z_3$; $A_4$ has order 12 and is solvable

# Context & Application
The alternating groups form one of the 18 infinite families of finite simple groups (for $n \geq 5$). They play a crucial role in Galois theory and the unsolvability of the quintic.

# Examples
**Example 1** (p. 112): $A_3 = \langle (123) \rangle \cong Z_3$.
**Example 2** (p. 112): $A_4$ has order 12 with a normal subgroup $\{1, (12)(34), (13)(24), (14)(23)\} \cong V_4$.

# Relationships
## Builds Upon
- **symmetric-group**, **transposition**, **normal-subgroup**

## Enables
- **simple-group** — $A_n$ is simple for $n \geq 5$

## Related
- **sign-of-permutation** — $A_n = \ker\epsilon$
- **solvable-group** — $A_4$ is solvable; $A_5$ is not

# Source Reference
Chapter 3, Section 3.5, pages 107-114.

# Verification Notes
- Definition source: direct from source pp. 110-111
- Confidence rationale: explicitly defined with full development
- Uncertainties: none
- Cross-reference status: verified
