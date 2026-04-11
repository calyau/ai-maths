---
concept: Hilbert Basis Theorem
slug: hilbert-basis-theorem
category: commutative-algebra
subcategory: chain-conditions
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
  - "Hilbert's Basis Theorem"
prerequisites:
  - noetherian-ring
  - polynomial-ring
extends: []
related:
  - finitely-generated-k-algebra
  - affine-algebraic-set
contrasts_with: []
answers_questions:
  - "Why is a polynomial ring over a field Noetherian?"
  - "How are larger Noetherian rings built from existing ones?"
---

# Quick Definition
If R is a Noetherian ring, then the polynomial ring R[x] is also Noetherian. By induction, k[x_1,...,x_n] is Noetherian for any field k.

# Core Definition
**Theorem 3 (Hilbert's Basis Theorem)**: If R is a Noetherian ring then so is the polynomial ring R[x] (p. 670). As an immediate corollary (Corollary 4), k[x_1,...,x_n] with coefficients from a field k is Noetherian, and more generally any finitely generated k-algebra is Noetherian (Corollary 5).

# Prerequisites
- **noetherian-ring** — The theorem extends the Noetherian property to polynomial extensions
- **polynomial-ring** — The construction R[x] is the object of study

# Key Properties
1. If R is Noetherian, so is R[x]
2. By induction, R[x_1,...,x_n] is Noetherian for any Noetherian R
3. Any finitely generated k-algebra is Noetherian (being a quotient of k[x_1,...,x_n])
4. Analogous to the theorem that R[x] is a UFD when R is (Theorem 7, Section 9.3)

# Construction / Recognition
## To Apply:
1. Verify R is Noetherian
2. Conclude R[x] is Noetherian
3. Apply inductively for polynomial rings in multiple variables

# Context & Application
The Hilbert Basis Theorem is foundational for algebraic geometry. It ensures that every ideal in k[x_1,...,x_n] is finitely generated, so every affine algebraic set is the zero locus of finitely many polynomials. Hilbert originally proved this theorem to show that invariant rings of finite groups acting on polynomial rings are finitely generated (p. 670).

# Examples
**Example** (p. 670): The polynomial ring k[x_1,x_2,...,x_n] over a field k is Noetherian. The polynomial ring k[x_1,x_2,...] in infinitely many variables is not.

# Relationships
## Builds Upon
- **noetherian-ring** — Extends the Noetherian property to polynomial rings

## Enables
- **affine-algebraic-set** — Every algebraic set is cut out by finitely many equations
- **finitely-generated-k-algebra** — All finitely generated k-algebras are Noetherian

# Common Errors
- **Error**: Trying to apply the theorem to infinitely many variables. **Correction**: The theorem requires finitely many variables; k[x_1,x_2,...] is not Noetherian.

# Common Confusions
- **Confusion**: Thinking the theorem says ideals in R[x] are principal. **Clarification**: It only says they are finitely generated; R[x] need not be a PID even when R is a field and n > 1.

# Source Reference
Chapter 15, Section 15.1, Theorem 3 and Corollaries 4-5, pages 670-671.

# Verification Notes
- Theorem statement directly from p. 670
- Confidence: HIGH — named theorem with clear statement
