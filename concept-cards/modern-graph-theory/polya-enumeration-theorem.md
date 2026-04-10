---
# === CORE IDENTIFICATION ===
concept: "Pólya's Enumeration Theorem"
slug: polya-enumeration-theorem

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: orbit-counting
tier: advanced

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
  - Polya counting theorem
  - Polya-Redfield theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cauchy-frobenius-lemma
  - cycle-index
  - group-orbit
extends:
  - cauchy-frobenius-lemma
related:
  - pattern-enumeration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Pólya's enumeration theorem?"
  - "How do I count graphs up to isomorphism?"
---

# Quick Definition

Polya's theorem computes the weighted count of orbits (patterns) under a group action: $|\Gamma|S = \widetilde{Z}(\Gamma; s_1, s_2, \ldots, s_d)$, where $S$ is the pattern sum, $\widetilde{Z}$ is the cycle sum, and $s_k$ are figure sums.

# Core Definition

**Theorem 23** (Bollobas, p. 288): Let $\Gamma$ act on domain $D$ ($|D| = d$), $R$ be a range, $w: R \to A$ a weight function into a commutative ring, $s_k = \sum_{r \in R} w(r)^k$ the $k$th figure sum, and $S = \sum_i w(O_i)$ the pattern sum over $\Gamma^*$-orbits. Then $|\Gamma|S = \widetilde{Z}(\Gamma; s_1, s_2, \ldots, s_d)$ where $\widetilde{Z}(\Gamma; a_1, \ldots, a_d) = \sum_{\alpha \in \Gamma} \prod_{k=1}^d a_k^{j_k(\alpha)}$ is the cycle sum and $j_k(\alpha)$ counts $k$-cycles in $\alpha$.

# Prerequisites

- **Cauchy-Frobenius lemma** -- The unweighted version
- **Cycle index** -- The polynomial encoding cycle structure
- **Group orbit** -- The objects being counted

# Key Properties

1. Reduces counting patterns to knowing the cycle structure of $\Gamma$
2. Works for arbitrary commutative ring weights (integers, rationals, polynomials, complex numbers)
3. Choosing $A = \mathbb{Z}$ and $w \equiv 1$ gives the number of orbits (Burnside's lemma)
4. Choosing $A = \mathbb{Z}[x_r : r \in R]$ and $w(r) = x_r$ gives complete information

# Construction / Recognition

## To Apply Polya's Theorem
1. Identify the domain $D$, range $R$, and group $\Gamma$ acting on $D$
2. Compute the cycle sum $\widetilde{Z}(\Gamma; a_1, \ldots, a_d)$
3. Choose weights $w: R \to A$ and compute figure sums $s_k$
4. Substitute $a_k = s_k$ in the cycle sum
5. Divide by $|\Gamma|$ to get the pattern sum $S$

# Context & Application

Polya's theorem (1937) is the fundamental tool for counting equivalence classes of combinatorial objects under symmetry. It applies to counting graphs up to isomorphism, colorings of polyhedra, chemical isomers, and necklace problems.

# Examples

**Example 1** (p. 289): Bracelets of 5 beads with 3 colors, cyclic symmetry: $\Gamma = C_5$, $\widetilde{Z} = a_1^5 + 4a_5$, giving 51 distinct bracelets.

**Example 2** (p. 289): Coloring faces of a cube with 3 colors: $|\Gamma| = 24$, giving 57 distinct colorings.

**Example 3** (p. 290): Balls in octahedron vertices: 3 red, 2 blue, 1 yellow gives 3 distinct arrangements.

# Relationships

## Builds Upon
- **Cauchy-Frobenius lemma** -- Unweighted special case
- **Cycle index** -- Central algebraic tool
- **Group orbit** -- Objects being counted

## Enables
- Counting graphs up to isomorphism
- Counting colorings under symmetry

## Related
- **Pattern enumeration** -- The general framework

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting to divide by $|\Gamma|$ when working over the rationals
  **Correction**: The theorem states $|\Gamma|S = \widetilde{Z}(\ldots)$; one must divide to get $S$

# Common Confusions

- **Confusion**: Thinking Polya's theorem only counts total patterns
  **Clarification**: With polynomial weights, it gives a generating function that encodes counts by type (e.g., by color distribution)

# Source Reference

Chapter VIII, Section VIII.4, Theorem 23, pages 287--290.

# Verification Notes

- Definition source: Direct from Theorem 23, p. 288
- Confidence rationale: Explicit theorem with proof and examples
- Uncertainties: None
- Cross-reference status: Verified
