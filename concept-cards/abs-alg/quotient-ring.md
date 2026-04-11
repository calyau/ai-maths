---
concept: Quotient Ring
slug: quotient-ring
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 243
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "factor ring"
  - "residue class ring"
prerequisites:
  - ring
  - ideal
extends: []
related:
  - ring-homomorphism
  - first-isomorphism-theorem-rings
  - prime-ideal
  - maximal-ideal
contrasts_with:
  - quotient-group
answers_questions:
  - "What is a quotient ring?"
  - "When can we form a quotient ring?"
---

# Quick Definition
The quotient ring $R/I$ is the set of cosets $r + I$ of an ideal I in R, with addition $(r+I) + (s+I) = (r+s)+I$ and multiplication $(r+I)(s+I) = rs+I$.

# Core Definition
When I is an ideal of R, the ring $R/I$ with operations $(r+I) + (s+I) = (r+s) + I$ and $(r+I) \times (s+I) = (rs) + I$ is called the *quotient ring* of R by I (Dummit & Foote, pp. 244-245, Proposition 6).

# Prerequisites
- **Ring** — The ambient ring
- **Ideal** — Only ideals (not arbitrary subrings) give well-defined quotient rings

# Key Properties
1. $R/I$ is a ring iff I is an ideal (Proposition 6, p. 245)
2. The natural projection $R \to R/I$ is a surjective ring homomorphism with kernel I (Theorem 7(2), p. 246)
3. $R/M$ is a field iff M is a maximal ideal (Proposition 12, p. 256)
4. $R/P$ is an integral domain iff P is a prime ideal (Proposition 13, p. 257)

# Construction / Recognition
## To Construct:
1. Start with a ring R and an ideal I
2. Form cosets $r + I$
3. Define addition and multiplication of cosets as above

# Context & Application
Quotient rings are one of the fundamental constructions in ring theory, analogous to quotient groups. They are used to construct new rings, including fields (via maximal ideals) and integral domains (via prime ideals).

# Examples
**Example 1** (p. 245): $\mathbb{Z}/n\mathbb{Z}$ is the quotient of $\mathbb{Z}$ by the ideal $n\mathbb{Z}$.

**Example 2** (p. 246): $\mathbb{Z}[x]/(x)$ is isomorphic to $\mathbb{Z}$.

**Example 3** (p. 246): The quotient $\mathbb{Z}[x]/(x^2 + x + 1)$ over $\mathbb{F}_2$ gives a field with 4 elements.

# Relationships

## Related
- **ring-homomorphism** — Every quotient ring arises from a surjective homomorphism
- **first-isomorphism-theorem-rings** — $R/\ker\varphi \cong \varphi(R)$
- **prime-ideal** — $R/P$ is an integral domain
- **maximal-ideal** — $R/M$ is a field

## Contrasts With
- **quotient-group** — Analogous construction for groups; uses normal subgroups

# Common Errors
- **Error**: Trying to form $R/S$ where S is a subring but not an ideal
  **Correction**: Multiplication of cosets is well-defined only when S is an ideal

# Common Confusions
- **Confusion**: Thinking $R/I$ can have zero divisors only if R does
  **Clarification**: $\mathbb{Z}[x]/(x^2)$ has zero divisors ($\bar{x}^2 = 0$) even though $\mathbb{Z}[x]$ is an integral domain (p. 246)

# Source Reference
Chapter 7, Section 7.3, Proposition 6 and Definition, pages 244-245.

# Verification Notes
- Definition: Direct from pp. 244-245
- Confidence: HIGH — explicit construction with proofs
