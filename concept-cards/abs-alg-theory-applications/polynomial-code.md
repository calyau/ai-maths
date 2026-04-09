---
# === CORE IDENTIFICATION ===
concept: Polynomial Code
slug: polynomial-code

# === CLASSIFICATION ===
category: field-theory
subcategory: finite-fields
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Finite Fields"
chapter_number: 22
pdf_page: 292
section: "22.2 Polynomial Codes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-field
  - polynomial
extends: []
related:
  - cyclic-code
  - bch-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a polynomial code?"
  - "How are polynomial codes constructed?"
---

# Quick Definition

A polynomial code is a linear code obtained by encoding $k$-tuples as polynomials and multiplying by a fixed generator polynomial $g(x)$ of degree $n - k$ to produce $n$-tuples.

# Core Definition

Let $g(x) \in \mathbb{Z}_2[x]$ be a nonconstant polynomial of degree $n - k$. An $(n,k)$-code $C$ is defined by encoding the $k$-tuple $(a_0, \ldots, a_{k-1})$ as the polynomial $f(x) = a_0 + a_1x + \cdots + a_{k-1}x^{k-1}$ and multiplying by $g(x)$. The codewords are all polynomials of degree less than $n$ divisible by $g(x)$. Codes obtained in this manner are called **polynomial codes** (Judson, p. 297).

# Prerequisites

- **Finite field** — Polynomial codes are built over $\mathbb{Z}_2$
- **Polynomial** — Codewords are represented as polynomials

# Key Properties

1. The encoding map $\phi: f(x) \mapsto g(x)f(x)$ is a group homomorphism (and linear transformation)
2. If $g(x)$ has no repeated roots, $\phi$ is injective
3. Binary $n$-tuples correspond to polynomials of degree $< n$ over $\mathbb{Z}_2$

# Construction / Recognition

## To Construct:
1. Choose a generator polynomial $g(x)$ of degree $n - k$
2. For each message polynomial $f(x)$ of degree $< k$, compute $g(x)f(x)$
3. The codewords are the resulting polynomials of degree $< n$

# Examples

**Example 1** (p. 297): With $g(x) = 1 + x^3$, the $(6,3)$-code encodes:
- $1 \mapsto 1 + x^3$, i.e., $(100) \mapsto (100100)$
- $x \mapsto x + x^4$, i.e., $(010) \mapsto (010010)$
- $x^2 \mapsto x^2 + x^5$, i.e., $(001) \mapsto (001001)$

# Relationships

## Enables
- **Cyclic code** — Many polynomial codes are cyclic
- **BCH code** — A sophisticated type of polynomial code

# Source Reference

Chapter 22: Finite Fields, Section 22.2, pages 297–298.

# Verification Notes

- Definition source: Direct from p. 297
- Confidence: HIGH — explicit definition with construction
- Cross-reference status: Verified
- Uncertainties: None
