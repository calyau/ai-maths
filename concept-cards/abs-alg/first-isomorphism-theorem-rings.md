---
concept: First Isomorphism Theorem for Rings
slug: first-isomorphism-theorem-rings
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 245
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - ring-homomorphism
  - ideal
  - quotient-ring
extends: []
related:
  - second-isomorphism-theorem-rings
  - third-isomorphism-theorem-rings
  - lattice-isomorphism-theorem-rings
contrasts_with: []
answers_questions:
  - "What is the First Isomorphism Theorem for Rings?"
---

# Quick Definition
If $\varphi: R \to S$ is a ring homomorphism, then $\ker\varphi$ is an ideal of R, $\varphi(R)$ is a subring of S, and $R/\ker\varphi \cong \varphi(R)$.

# Core Definition
(Theorem 7(1)) If $\varphi: R \to S$ is a homomorphism of rings, then $\ker\varphi$ is an ideal of R, the image of $\varphi$ is a subring of S, and $R/\ker\varphi$ is isomorphic as a ring to $\varphi(R)$. Furthermore, every ideal is the kernel of a ring homomorphism (namely the natural projection $R \to R/I$) (Dummit & Foote, pp. 245-246).

# Prerequisites
- **Ring homomorphism** — The theorem applies to ring homomorphisms
- **Ideal** — The kernel is an ideal
- **Quotient ring** — The quotient by the kernel is the source of the isomorphism

# Key Properties
1. Establishes bijection between ideals and kernels of homomorphisms
2. The natural projection $R \to R/I$ defined by $r \mapsto r + I$ is a surjective ring homomorphism with kernel I

# Construction / Recognition
## To Apply:
1. Identify the ring homomorphism $\varphi: R \to S$
2. Compute $\ker\varphi$
3. Conclude $R/\ker\varphi \cong \varphi(R)$

# Context & Application
This is the fundamental tool for understanding quotient rings. It is the ring-theoretic analogue of the First Isomorphism Theorem for groups.

# Examples
**Example 1** (p. 246): The evaluation homomorphism $\mathbb{Z}[x] \to \mathbb{Z}$ mapping $p(x) \mapsto p(0)$ has kernel $(x)$, giving $\mathbb{Z}[x]/(x) \cong \mathbb{Z}$.

**Example 2** (p. 247): The reduction map $\mathbb{Z}[x] \to \mathbb{Z}/2\mathbb{Z}$ via $p(x) \mapsto p(0) \bmod 2$ has kernel = polynomials with even constant term.

# Relationships

## Related
- **second-isomorphism-theorem-rings** — $(A+B)/B \cong A/(A \cap B)$
- **third-isomorphism-theorem-rings** — $(R/I)/(J/I) \cong R/J$
- **lattice-isomorphism-theorem-rings** — Bijection between subrings of $R/I$ and subrings of R containing I

# Common Errors
- **Error**: Forgetting to verify the map is a ring homomorphism (not just a group homomorphism)
  **Correction**: Must check both additive and multiplicative preservation

# Common Confusions
- **Confusion**: Thinking the isomorphism theorem only works for surjective maps
  **Clarification**: The isomorphism is with the *image* $\varphi(R)$, not necessarily all of S

# Source Reference
Chapter 7, Section 7.3, Theorem 7, pages 245-246.

# Verification Notes
- Definition: Direct from Theorem 7, pp. 245-246
- Confidence: HIGH — fundamental theorem with explicit proof
