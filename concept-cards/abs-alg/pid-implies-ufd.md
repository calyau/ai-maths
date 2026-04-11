---
concept: PID Implies UFD
slug: pid-implies-ufd
category: ring-theory
subcategory: structure-theorems
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 286
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases: []
prerequisites:
  - principal-ideal-domain
  - unique-factorization-domain
  - ascending-chain-condition
extends: []
related:
  - domain-hierarchy
contrasts_with: []
answers_questions:
  - "Why is every PID a UFD?"
---

# Quick Definition
Every Principal Ideal Domain is a Unique Factorization Domain. The proof uses two key ingredients: (1) the ascending chain condition ensures factorization into irreducibles terminates, and (2) irreducible = prime in a PID ensures uniqueness.

# Core Definition
(Theorem 14) Every Principal Ideal Domain is a Unique Factorization Domain. Existence of factorizations follows from the ACC on ideals (ascending chains in a PID stabilize). Uniqueness follows from the fact that irreducibles are prime in a PID (Proposition 11) (Dummit & Foote, pp. 286-288).

# Prerequisites
- **Principal ideal domain** — The hypothesis
- **Unique factorization domain** — The conclusion
- **Ascending chain condition** — Key tool for existence

# Key Properties
1. ACC ensures the factorization process terminates
2. Irreducible = prime ensures uniqueness (via induction)
3. The proof also establishes Corollary 15 (Fundamental Theorem of Arithmetic)

# Source Reference
Chapter 8, Section 8.3, Theorem 14, pages 286-288.

# Verification Notes
- Definition: Direct from Theorem 14, pp. 286-288
- Confidence: HIGH — fundamental theorem with complete proof
