---
# === CORE IDENTIFICATION ===
concept: Cycle Index
slug: cycle-index

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: permutation-groups
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 287
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - cycle sum
  - cycle polynomial

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-orbit
extends: []
related:
  - polya-enumeration-theorem
  - cauchy-frobenius-lemma
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the cycle index of a permutation group?"
  - "What must I know before understanding Pólya's enumeration theorem?"
---

# Quick Definition

The cycle sum of a permutation group $\Gamma$ acting on $D$ is $\widetilde{Z}(\Gamma; a_1, \ldots, a_d) = \sum_{\alpha \in \Gamma} \prod_{k=1}^d a_k^{j_k(\alpha)}$, where $j_k(\alpha)$ counts $k$-cycles in $\alpha$. The cycle index is $Z = \widetilde{Z}/|\Gamma|$.

# Core Definition

Each $\alpha \in \Gamma$ decomposes into disjoint cycles; $j_k(\alpha)$ counts cycles of length $k$, with $\sum k \cdot j_k(\alpha) = d = |D|$. The cycle sum is $\widetilde{Z}(\Gamma; a_1, \ldots, a_d) = \sum_{\alpha \in \Gamma} \prod_{k=1}^d a_k^{j_k(\alpha)}$. The customary cycle index is $Z = \widetilde{Z}/|\Gamma|$. Bollobas uses the cycle sum to allow arbitrary commutative rings (where dividing by $|\Gamma|$ may not be possible) (p. 287).

# Prerequisites

- **Group orbit** -- The setting for the permutation group

# Key Properties

1. Encodes the complete cycle structure of $\Gamma$
2. Substituting $a_k = s_k$ (figure sums) gives $|\Gamma|S$ by Polya's theorem
3. $\widetilde{Z}(\Gamma; 1, 1, \ldots, 1) = |\Gamma|$ (each term contributes 1)
4. Depends on the action of $\Gamma$ on $D$, not just the abstract group

# Construction / Recognition

## To Compute the Cycle Sum
1. For each $\alpha \in \Gamma$, decompose into disjoint cycles (including fixed points as 1-cycles)
2. Record $j_k(\alpha)$ for each cycle length $k$
3. Form the monomial $\prod_k a_k^{j_k(\alpha)}$
4. Sum over all $\alpha \in \Gamma$

# Context & Application

The cycle index is the key algebraic input to Polya's theorem. Computing it requires understanding the cycle structure of the symmetry group, which is the main computational challenge in applications.

# Examples

**Example 1** (p. 289): $C_5$ acting on $\{1,2,3,4,5\}$: $\widetilde{Z} = a_1^5 + 4a_5$.

**Example 2** (p. 290): Rotation group of the octahedron: $\widetilde{Z} = a_1^6 + 6a_1^2a_4 + 3a_1^2a_2^2 + 6a_2^3 + 8a_3^2$.

# Relationships

## Builds Upon
- **Group orbit** -- Context

## Enables
- **Polya's enumeration theorem** -- Central input

## Related
- **Cauchy-Frobenius lemma** -- $\widetilde{Z}(\Gamma; 1, 0, \ldots) = \sum |F(\alpha)|$ recovers the orbit-counting formula

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting fixed points as 1-cycles
  **Correction**: Every element of $D$ must appear in exactly one cycle; fixed points are 1-cycles

# Common Confusions

- **Confusion**: Thinking the cycle index depends only on the abstract group
  **Clarification**: It depends on how $\Gamma$ acts on $D$; the same group acting on different sets has different cycle indices

# Source Reference

Chapter VIII, Section VIII.4, page 287.

# Verification Notes

- Definition source: Direct from p. 287
- Confidence rationale: Explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
