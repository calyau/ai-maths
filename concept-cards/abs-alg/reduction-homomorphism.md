---
concept: Reduction Homomorphism
slug: reduction-homomorphism
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 249
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "reduction modulo n"
  - "mod n map"
prerequisites:
  - ring-homomorphism
  - quotient-ring
extends:
  - ring-homomorphism
related:
  - reduction-mod-p
  - chinese-remainder-theorem
contrasts_with: []
answers_questions:
  - "What is the reduction homomorphism?"
  - "How is reducing modulo n used in number theory?"
---

# Quick Definition
The reduction homomorphism is the natural projection $R \to R/I$ that maps each element to its coset. For $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, this is "reducing modulo n."

# Core Definition
The canonical projection map from a ring R to the quotient ring $R/I$, mapping $r \mapsto r + I$, is called the reduction (or natural projection) homomorphism. For $R = \mathbb{Z}$, $I = n\mathbb{Z}$: this is *reduction modulo n*. For $R = \mathbb{Z}[x]$, $I = p\mathbb{Z}[x]$: this reduces polynomial coefficients modulo p (Dummit & Foote, pp. 246, 249).

# Prerequisites
- **Ring homomorphism** — The reduction map is a ring homomorphism
- **Quotient ring** — The target is a quotient ring

# Key Properties
1. Always surjective with kernel I (Theorem 7(2), p. 246)
2. Relations in R project to relations in R/I
3. Useful for Diophantine equations: if an equation has no solution mod n, it has no integer solution
4. $\mathbb{Z}[x] \to \mathbb{Z}/p\mathbb{Z}[x]$ reducing coefficients mod p is a ring homomorphism (p. 249)

# Examples
**Example 1** (p. 249): The equation $x^2 + y^2 = 3z^2$ has no nonzero integer solutions (check mod 4).

**Example 2** (p. 249): Reducing polynomial coefficients mod p can detect irreducibility (Chapter 9).

# Relationships

## Related
- **reduction-mod-p** — Using reduction to test polynomial irreducibility
- **chinese-remainder-theorem** — Uses reduction modulo pairwise coprime ideals

# Source Reference
Chapter 7, Section 7.3, pages 246, 249.

# Verification Notes
- Definition: From pp. 246, 249
- Confidence: HIGH — explicit construction
