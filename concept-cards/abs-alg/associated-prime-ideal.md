---
concept: Associated Prime Ideal
slug: associated-prime-ideal
category: commutative-algebra
subcategory: ideal-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 712
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "isolated prime"
  - "embedded prime"
prerequisites:
  - primary-decomposition
extends: []
related:
  - primary-ideal
contrasts_with: []
answers_questions:
  - "What are the associated primes of an ideal?"
---

# Quick Definition
The associated prime ideals of I are the radicals of the primary components in any minimal primary decomposition. Isolated primes are minimal among these; the rest are embedded.

# Core Definition
If I has a primary decomposition I = Q_1 ∩ ··· ∩ Q_m, the primes P_i = rad Q_i are the **associated prime ideals** of I (Definition, p. 713). If P_i does not contain any other P_j, it is **isolated**; otherwise it is **embedded**. The set of associated primes is uniquely determined (Theorem 21).

# Prerequisites
- **primary-decomposition** — Associated primes come from primary decomposition

# Key Properties
1. The set of associated primes is unique (Theorem 21)
2. rad I = intersection of associated (equivalently, isolated) primes (Corollary 22)
3. A prime contains I iff it contains some associated prime
4. Isolated prime components are unique; embedded ones may not be

# Source Reference
Chapter 15, Section 15.2, Definition and Corollary 22, pages 712-713.

# Verification Notes
- Confidence: HIGH — explicit definition with uniqueness theorem
