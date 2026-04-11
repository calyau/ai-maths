---
concept: Lattice Isomorphism Theorem for Rings
slug: lattice-isomorphism-theorem-rings
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 247
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "Fourth Isomorphism Theorem for Rings"
  - "Correspondence Theorem for Rings"
prerequisites:
  - ideal
  - quotient-ring
extends: []
related:
  - first-isomorphism-theorem-rings
  - maximal-ideal
  - prime-ideal
contrasts_with: []
answers_questions:
  - "What is the Lattice Isomorphism Theorem for Rings?"
  - "How are ideals of R/I related to ideals of R?"
---

# Quick Definition
The correspondence $A \leftrightarrow A/I$ is an inclusion-preserving bijection between subrings of R containing I and subrings of $R/I$. A is an ideal of R iff $A/I$ is an ideal of $R/I$.

# Core Definition
(Theorem 8(3)) Let I be an ideal of R. The correspondence $A \leftrightarrow A/I$ is an inclusion-preserving bijection between the set of subrings A of R that contain I and the set of subrings of $R/I$. Furthermore, A (containing I) is an ideal of R if and only if $A/I$ is an ideal of $R/I$ (Dummit & Foote, p. 248).

# Prerequisites
- **Ideal** — I is an ideal of R
- **Quotient ring** — The theorem involves $R/I$

# Key Properties
1. Subrings of $R/I$ correspond to subrings of R containing I
2. Ideals of $R/I$ correspond to ideals of R containing I
3. Preserves inclusion ordering
4. Used crucially in proofs involving maximal and prime ideals

# Examples
**Example** (p. 248): For $R = \mathbb{Z}$ and $I = 12\mathbb{Z}$, the ideals of $\mathbb{Z}/12\mathbb{Z}$ are $\bar{R}, 2\mathbb{Z}/12\mathbb{Z}, 3\mathbb{Z}/12\mathbb{Z}, 4\mathbb{Z}/12\mathbb{Z}, 6\mathbb{Z}/12\mathbb{Z}, \bar{0}$.

# Relationships

## Related
- **maximal-ideal** — M is maximal iff $R/M$ has only trivial ideals (i.e., is a field)
- **prime-ideal** — P is prime iff $R/P$ is an integral domain

# Source Reference
Chapter 7, Section 7.3, Theorem 8(3), page 248.

# Verification Notes
- Definition: Direct from Theorem 8(3), p. 248
- Confidence: HIGH — explicit theorem
