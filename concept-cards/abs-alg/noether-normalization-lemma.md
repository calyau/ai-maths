---
concept: Noether Normalization Lemma
slug: noether-normalization-lemma
category: commutative-algebra
subcategory: fundamental-theorems
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 727
section: "15.3 Integral Extensions and Hilbert's Nullstellensatz"
extraction_confidence: high
aliases:
  - "Normalization Lemma"
  - "Noether's Normalization Lemma"
prerequisites:
  - finitely-generated-k-algebra
  - integral-extension
extends: []
related:
  - hilberts-nullstellensatz
contrasts_with: []
answers_questions:
  - "What is Noether's Normalization Lemma?"
---

# Quick Definition
Every finitely generated k-algebra A contains algebraically independent elements y_1,...,y_q such that A is integral over the polynomial subring k[y_1,...,y_q].

# Core Definition
**Theorem 30 (Noether's Normalization Lemma)**: Let k be a field and A = k[r_1,...,r_m] a finitely generated k-algebra. Then for some q, 0 ≤ q ≤ m, there are algebraically independent elements y_1,...,y_q ∈ A such that A is integral over k[y_1,...,y_q] (p. 727). This is used in the proof of the Weak Form of the Nullstellensatz.

# Prerequisites
- **finitely-generated-k-algebra** — A must be finitely generated over k
- **integral-extension** — A is integral over the polynomial subring

# Key Properties
1. Geometrically: every affine algebraic set is a finite covering of some A^q (Exercise 15)
2. The integer q equals the dimension of the variety when A = k[V] for a variety V

# Relationships
## Enables
- **hilberts-nullstellensatz** — The Normalization Lemma is a key step in the proof

# Source Reference
Chapter 15, Section 15.3, Theorem 30, pages 727-728.

# Verification Notes
- Confidence: HIGH — named theorem with complete proof
