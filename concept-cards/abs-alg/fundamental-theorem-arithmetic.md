---
concept: Fundamental Theorem of Arithmetic
slug: fundamental-theorem-arithmetic
category: ring-theory
subcategory: factorization
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 289
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases:
  - "unique prime factorization in Z"
prerequisites:
  - unique-factorization-domain
extends: []
related:
  - euclidean-domain
  - principal-ideal-domain
contrasts_with: []
answers_questions:
  - "Why do integers have unique prime factorizations?"
---

# Quick Definition
Every integer greater than 1 can be written as a product of prime numbers, and this factorization is unique up to the order of factors. This is Corollary 15 of the theorem that every PID is a UFD.

# Core Definition
(Corollary 15) The integers $\mathbb{Z}$ are a Unique Factorization Domain. This follows from the chain: $\mathbb{Z}$ is a Euclidean Domain, hence a PID (Proposition 1), hence a UFD (Theorem 14) (Dummit & Foote, p. 289).

# Prerequisites
- **Unique factorization domain** — $\mathbb{Z}$ is a UFD

# Key Properties
1. Every positive integer $n > 1$ has a unique factorization $n = p_1^{a_1} \cdots p_k^{a_k}$
2. Uniqueness is up to order of factors
3. Follows from: Euclidean Algorithm $\Rightarrow$ PID $\Rightarrow$ UFD

# Source Reference
Chapter 8, Section 8.3, Corollary 15, page 289.

# Verification Notes
- Definition: Direct from Corollary 15, p. 289
- Confidence: HIGH — explicit corollary
