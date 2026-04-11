---
concept: "Hilbert's Nullstellensatz"
slug: hilberts-nullstellensatz
category: algebraic-geometry
subcategory: fundamental-theorems
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 698
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "Nullstellensatz"
  - "Zeros Theorem"
  - "Hilbert Nullstellensatz"
prerequisites:
  - radical-of-ideal
  - affine-algebraic-set
  - algebraically-closed-field
extends: []
related:
  - noether-normalization-lemma
  - prime-spectrum
contrasts_with: []
answers_questions:
  - "What is Hilbert's Nullstellensatz?"
  - "What is the relationship between radical ideals and algebraic sets?"
---

# Quick Definition
Over an algebraically closed field k, I(Z(I)) = rad I for every ideal I. This establishes a bijective correspondence between affine algebraic sets and radical ideals.

# Core Definition
**Hilbert's Nullstellensatz** (Theorem 32, p. 730): Let k be an algebraically closed field. Then I(Z(I)) = rad I for every ideal I of k[x_1,...,x_n]. The maps Z and I define inverse bijections between {affine algebraic sets} and {radical ideals}. The **Weak Form** (Theorem 31, p. 729): maximal ideals in k[x_1,...,x_n] are exactly the ideals (x_1-a_1,...,x_n-a_n), and every proper ideal has a common zero.

# Prerequisites
- **radical-of-ideal** — The statement involves radicals
- **affine-algebraic-set** — One side of the correspondence
- **algebraically-closed-field** — Required for the theorem to hold

# Key Properties
1. Over algebraically closed k: I(Z(I)) = rad I
2. Z and I give inverse bijections: algebraic sets ↔ radical ideals
3. Points of A^n ↔ maximal ideals of k[x_1,...,x_n] (Weak Form)
4. Subvarieties ↔ prime ideals; algebraic sets ↔ radical ideals
5. Every proper ideal in k[x_1,...,x_n] has a common zero (over algebraically closed k)
6. Variant (Corollary 33): works over any field k using zeros in the algebraic closure

# Context & Application
The Nullstellensatz is the fundamental bridge between algebra and geometry. It provides a complete dictionary: algebraic sets ↔ radical ideals, varieties ↔ prime ideals, points ↔ maximal ideals, morphisms ↔ k-algebra homomorphisms. This dictionary is summarized in the table on p. 732.

# Examples
**Example** (p. 698): Over R (not algebraically closed), (x^2+1) is a maximal ideal in R[x] that defines no point of A^1 — illustrating why algebraic closure is needed.

# Relationships
## Builds Upon
- **radical-of-ideal** — rad I is the algebraic characterization
- **noether-normalization-lemma** — Used in the proof via the Weak Form

## Enables
- **prime-spectrum** — Generalizes the point-maximal ideal correspondence

# Source Reference
Chapter 15, Sections 15.2-15.3, Theorems 31-32, pages 698-730.

# Verification Notes
- Confidence: HIGH — major named theorem with complete proof
