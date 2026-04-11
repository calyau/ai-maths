---
concept: Second Isomorphism Theorem for Rings
slug: second-isomorphism-theorem-rings
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
aliases: []
prerequisites:
  - subring
  - ideal
  - quotient-ring
extends: []
related:
  - first-isomorphism-theorem-rings
  - third-isomorphism-theorem-rings
  - lattice-isomorphism-theorem-rings
contrasts_with: []
answers_questions:
  - "What is the Second Isomorphism Theorem for Rings?"
---

# Quick Definition
If A is a subring and B is an ideal of R, then $A + B$ is a subring, $A \cap B$ is an ideal of A, and $(A + B)/B \cong A/(A \cap B)$.

# Core Definition
(Theorem 8(1)) Let A be a subring and B an ideal of R. Then $A + B$ is a subring of R, $A \cap B$ is an ideal of A, and $(A + B)/B \cong A/(A \cap B)$ (Dummit & Foote, p. 248).

# Prerequisites
- **Subring** — A is a subring
- **Ideal** — B is an ideal
- **Quotient ring** — The theorem involves quotient rings

# Key Properties
1. $A + B$ is automatically a subring (not just a subset)
2. The isomorphism follows from the group-theoretic version plus checking multiplicativity

# Source Reference
Chapter 7, Section 7.3, Theorem 8(1), page 248.

# Verification Notes
- Definition: Direct from Theorem 8(1), p. 248
- Confidence: HIGH — explicit theorem
