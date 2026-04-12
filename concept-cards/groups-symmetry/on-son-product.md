---
# === CORE IDENTIFICATION ===
concept: O_n as SO_n x Z_2 (Odd n)
slug: on-son-product

# === CLASSIFICATION ===
category: structure-theory
subcategory: products
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Products"
chapter_number: 10
pdf_page: 59
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "O_n decomposition for odd n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
  - special-orthogonal-group
  - internal-direct-product-criterion
  - direct-product
extends: []
related:
  - central-inversion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is O_n isomorphic to SO_n x Z_2?"
  - "How does the orthogonal group decompose?"
---

# Quick Definition

For odd $n$, $O_n \cong SO_n \times \mathbb{Z}_2$. For even $n$, this decomposition fails.

# Core Definition

Armstrong proves (Example iv, p. 61): $O_3 \cong SO_3 \times \mathbb{Z}_2$ by defining $\varphi: SO_3 \times \{I, J\} \to O_3$ via $\varphi(A, U) = AU$, where $J = -I_3$. The map preserves multiplication (because $J$ commutes with everything), is injective (by determinant argument), and is surjective (every $A \in O_3$ is either in $SO_3$ or $AJ \in SO_3$).

"The same argument shows that $O_n$ is isomorphic to $SO_n \times \mathbb{Z}_2$ when $n$ is odd. For even $n$ this result is false" (p. 62). The failure for even $n$ occurs because $\det(-I_n) = (-1)^n = +1$ when $n$ is even, so $-I_n \in SO_n$ rather than serving as a separate factor (Exercise 10.9).

# Prerequisites

- **Orthogonal group** — The group being decomposed
- **Special orthogonal group** — One factor
- **Internal direct product criterion** — Theorem 10.2 provides the framework
- **Direct product** — The structure of the result

# Key Properties

1. For odd $n$: $O_n \cong SO_n \times \mathbb{Z}_2$
2. For even $n$: $O_n \not\cong SO_n \times \mathbb{Z}_2$
3. The $\mathbb{Z}_2$ factor is $\{I_n, -I_n\}$
4. $-I_n$ commutes with every orthogonal matrix
5. For odd $n$: $\det(-I_n) = -1$, so $-I_n \notin SO_n$
6. For even $n$: $\det(-I_n) = +1$, so $-I_n \in SO_n$ and $\{I_n, -I_n\} \le SO_n$

# Construction / Recognition

## To Verify for Odd $n$:
1. $H = SO_n$, $K = \{I_n, -I_n\}$
2. $HK = O_n$: any $A \in O_n$ is either in $SO_n$ or $A(-I_n) \in SO_n$
3. $H \cap K = \{I_n\}$: $-I_n$ has det $-1$ when $n$ is odd, so $-I_n \notin SO_n$
4. $-I_n$ commutes with all matrices
5. Theorem 10.2 applies

# Context & Application

This is the motivating example for Theorem 10.2 and demonstrates the power of the internal direct product criterion. The result also explains why the full symmetry groups of 3D Platonic solids decompose as rotational group times $\mathbb{Z}_2$.

# Examples

**Example** (p. 61): $O_3 \cong SO_3 \times \mathbb{Z}_2$, with the isomorphism $\varphi(A, U) = AU$.

# Relationships

## Builds Upon
- **Internal direct product criterion** — Theorem 10.2
- **Central inversion** — $-I$ is central inversion

## Related
- **Full symmetry groups of solids** — Uses the same decomposition

# Common Errors

- **Error**: Applying the decomposition for all $n$.
  **Correction**: It fails for even $n$ because $-I_n \in SO_n$ when $n$ is even.

# Common Confusions

- **Confusion**: Thinking the failure for even $n$ means $O_n$ has no useful decomposition.
  **Clarification**: For even $n$, $O_n$ still has interesting structure, but it is not a direct product of $SO_n$ and $\mathbb{Z}_2$.

# Source Reference

Chapter 10: Products, pages 61-62 (pdf pp. 61-62). Example (iv) and subsequent remark.

# Verification Notes

- Proof: Complete for $n = 3$ on pp. 61-62
- Even $n$ failure: Stated on p. 62, Exercise 10.9
- Confidence: HIGH — detailed proof for $O_3$ case
