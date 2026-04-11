---
concept: Cayley-Hamilton Theorem
slug: cayley-hamilton-theorem
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 481
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases: []
prerequisites:
  - characteristic-polynomial
  - minimal-polynomial-linear
  - rational-canonical-form
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is the Cayley-Hamilton Theorem?"
---

# Quick Definition
The Cayley-Hamilton Theorem states that every matrix (or linear transformation) satisfies its own characteristic polynomial: $c_T(T) = 0$. Equivalently, the minimal polynomial divides the characteristic polynomial.

# Core Definition
(Corollary 15) Let T be a linear transformation of a finite dimensional vector space V over F with characteristic polynomial $c_T(x)$. Then $c_T(T) = 0$, i.e., the characteristic polynomial annihilates V as an F[x]-module. Equivalently, $m_T(x) \mid c_T(x)$. This follows from the fact that $c_T(x) = a_1(x) \cdots a_m(x)$ is the product of the invariant factors, and each $a_i(x)$ divides $a_m(x) = m_T(x)$ (Dummit & Foote, Corollary 15, p. 481).

# Prerequisites
- **characteristic-polynomial**, **minimal-polynomial-linear**, **rational-canonical-form**

# Key Properties
1. $c_T(T) = 0$ for any linear transformation T
2. The minimal polynomial divides the characteristic polynomial
3. They have the same irreducible factors (same roots in any extension field)

# Context & Application
The Cayley-Hamilton theorem is a fundamental result with applications throughout mathematics and engineering. In this text, it follows immediately from the structure theory of modules over PIDs.

# Relationships
## Builds Upon
- **characteristic-polynomial**, **rational-canonical-form**

# Source Reference
Chapter 12, Section 12.2, Corollary 15, p. 481.

# Verification Notes
- Confidence: HIGH — explicit corollary
