---
concept: Upper Triangular Matrices
slug: upper-triangular-matrix
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 239
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix-ring
  - subring
extends:
  - subring
related:
  - matrix-ring
contrasts_with: []
answers_questions:
  - "Are upper triangular matrices a subring?"
---

# Quick Definition
The set of upper triangular matrices (entries below the main diagonal are zero) forms a subring of $M_n(R)$.

# Core Definition
An *upper triangular matrix* is $(a_{ij})$ with $a_{pq} = 0$ whenever $p > q$. The sum and product of upper triangular matrices are upper triangular, so they form a subring of $M_n(R)$. A *strictly upper triangular* matrix also has zeros on the diagonal; such matrices are nilpotent: $A^n = 0$ (Exercise 8, Dummit & Foote, pp. 239, 240).

# Prerequisites
- **Matrix ring** — Upper triangular matrices live in $M_n(R)$
- **Subring** — They form a subring

# Key Properties
1. Upper triangular matrices form a subring
2. Strictly upper triangular matrices satisfy $A^n = 0$ (Exercise 8)
3. The diagonal entries of a product of upper triangular matrices are the products of the diagonal entries

# Source Reference
Chapter 7, Section 7.2, page 239.

# Verification Notes
- Definition: Direct from p. 239
- Confidence: HIGH — explicit example
