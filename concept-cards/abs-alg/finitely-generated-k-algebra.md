---
concept: Finitely Generated k-Algebra
slug: finitely-generated-k-algebra
category: commutative-algebra
subcategory: ring-structures
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 670
section: "15.1 Noetherian Rings and Affine Algebraic Sets"
extraction_confidence: high
aliases:
  - "finitely generated algebra"
prerequisites:
  - ring
  - polynomial-ring
extends: []
related:
  - noetherian-ring
  - hilbert-basis-theorem
contrasts_with: []
answers_questions:
  - "What is a finitely generated k-algebra?"
---

# Quick Definition
A k-algebra R is finitely generated if R is generated as a ring by k together with finitely many elements r_1,...,r_n. Equivalently, R is a quotient of a polynomial ring k[x_1,...,x_n].

# Core Definition
The ring R is a **finitely generated k-algebra** if R is generated as a ring by k together with some finite set r_1,...,r_n of elements of R (Definition, p. 670). Equivalently, there is a surjective k-algebra homomorphism k[x_1,...,x_n] → R (Corollary 5). Any finitely generated k-algebra is Noetherian.

# Prerequisites
- **ring** — Base structure
- **polynomial-ring** — Finitely generated k-algebras are quotients of polynomial rings

# Key Properties
1. Equivalent to being a quotient of k[x_1,...,x_n]
2. Always Noetherian (Corollary 5)
3. Distinguished from being finitely generated as a vector space (Example, p. 670)

# Relationships
## Enables
- **noetherian-ring** — Every finitely generated k-algebra is Noetherian

# Source Reference
Chapter 15, Section 15.1, Definition and Corollary 5, pages 670-671.

# Verification Notes
- Confidence: HIGH — explicit definition
