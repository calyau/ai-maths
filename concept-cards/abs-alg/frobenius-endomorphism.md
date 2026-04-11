---
concept: Frobenius Endomorphism
slug: frobenius-endomorphism
category: galois-theory
subcategory: finite-fields
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 586
section: "14.3 Finite Fields"
extraction_confidence: high
aliases:
  - "Frobenius automorphism"
  - "Frobenius map"
prerequisites:
  - finite-field-classification
extends: []
related:
  - galois-group
contrasts_with: []
answers_questions:
  - "What is the Frobenius endomorphism?"
---

# Quick Definition
The Frobenius endomorphism of a field of characteristic p is the map $\sigma_p: x \mapsto x^p$. For finite fields, it is an automorphism that generates the Galois group $\text{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) \cong \mathbb{Z}/n\mathbb{Z}$.

# Core Definition
In a field F of characteristic p, the Frobenius endomorphism $\sigma_p: F \to F$ is defined by $\sigma_p(x) = x^p$. This is a field homomorphism because $(x+y)^p = x^p + y^p$ in characteristic p. For finite fields it is an automorphism, and $\text{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) = \langle\sigma_p\rangle$ (Dummit & Foote, pp. 586-588).

# Prerequisites
- **finite-field-classification** — Frobenius generates Galois groups of finite fields

# Key Properties
1. $(x + y)^p = x^p + y^p$ in characteristic p (the "Freshman's Dream")
2. $\sigma_p$ is always injective; for finite fields it is also surjective
3. $\sigma_p^n = \text{id}$ on $\mathbb{F}_{p^n}$; $\sigma_p$ has order n
4. Fixed field of $\sigma_p^k$ is $\mathbb{F}_{p^k}$

# Relationships
## Enables
- Generates **galois-group** of finite field extensions

# Source Reference
Chapter 14, Section 14.3, pp. 586-588.

# Verification Notes
- Confidence: HIGH — explicit definition
