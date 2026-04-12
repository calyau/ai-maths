---
# === CORE IDENTIFICATION ===
concept: Sign Polynomial
slug: sign-polynomial

# === CLASSIFICATION ===
category: permutation-groups
subcategory: sign
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Permutations"
chapter_number: 6
pdf_page: 33
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Vandermonde-type polynomial for sign"
  - "polynomial P"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - permutation
extends: []
related:
  - sign-of-a-permutation
  - even-permutation
  - odd-permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the sign of a permutation rigorously defined?"
  - "Why is the parity of a permutation well-defined?"
---

# Quick Definition

The polynomial $P = \prod_{i < j} (x_i - x_j)$ is used to rigorously define the sign of a permutation: applying $\alpha \in S_n$ to $P$ gives either $+P$ or $-P$.

# Core Definition

Armstrong introduces the polynomial (p. 35):
$$P = P(x_1, x_2, \ldots, x_n) = \prod_{1 \le i < j \le n} (x_i - x_j).$$

For $\alpha \in S_n$, define $\alpha P$ as the product of all factors $(x_{\alpha(i)} - x_{\alpha(j)})$ where $i < j$. "The effect of $\alpha$ is to permute the terms of $P$, while at the same time changing the sign of some of them. Therefore, $\alpha P$ is either $+P$ or $-P$" (p. 35-36). This determines the sign of $\alpha$.

# Prerequisites

- **Permutation** — The polynomial is acted on by permutations

# Key Properties

1. $P$ is the product of all differences $(x_i - x_j)$ with $i < j$
2. Applying $\alpha$ permutes the factors and possibly changes signs
3. $\alpha P = \pm P$ for any $\alpha \in S_n$
4. The sign function is multiplicative: $(\alpha\beta)P = \alpha(\beta P)$
5. This construction proves the sign is well-defined independent of transposition decomposition

# Construction / Recognition

## To Compute $\alpha P$:
1. Write $P = \prod_{i<j} (x_i - x_j)$
2. Replace each $x_k$ by $x_{\alpha(k)}$
3. Each factor $(x_i - x_j)$ becomes $(x_{\alpha(i)} - x_{\alpha(j)})$
4. Rewrite each factor as $\pm(x_a - x_b)$ with $a < b$
5. The product of the signs gives $\alpha P = \pm P$

# Context & Application

The polynomial $P$ provides the rigorous foundation for defining the sign of a permutation. Without it, one would need to prove independently that the parity of the number of transpositions in any decomposition is invariant -- a fact that is not obvious. The polynomial approach makes the proof clean and algebraic.

# Examples

**Example** (p. 36): For $n = 3$ and $\alpha = (132)$:
$$P = (x_1 - x_2)(x_1 - x_3)(x_2 - x_3)$$
$$\alpha P = (x_3 - x_1)(x_3 - x_2)(x_1 - x_2)$$
$$= (-(x_1 - x_3))(-(x_2 - x_3))(x_1 - x_2) = +P.$$
So the sign of $(132)$ is $+1$.

# Relationships

## Enables
- **Sign of a permutation** — The polynomial $P$ defines the sign rigorously

## Related
- **Even permutation** — $\alpha P = +P$
- **Odd permutation** — $\alpha P = -P$

# Common Errors

- **Error**: Forgetting to account for the sign change when reordering factors.
  **Correction**: $(x_{\alpha(i)} - x_{\alpha(j)}) = -(x_{\alpha(j)} - x_{\alpha(i)})$ when $\alpha(i) > \alpha(j)$, so each such inversion contributes a factor of $-1$.

# Common Confusions

- **Confusion**: Thinking $P$ must be computed explicitly to find the sign.
  **Clarification**: In practice, one counts the number of inversions or uses cycle lengths; $P$ is the theoretical justification, not a practical computation tool.

# Source Reference

Chapter 6: Permutations, pages 35-36 (pdf pp. 35-36). Definition and worked example.

# Verification Notes

- Definition: Direct from pp. 35-36
- Example: Directly from source
- Confidence: HIGH — explicit definition with worked computation
