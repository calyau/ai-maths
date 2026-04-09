---
# === CORE IDENTIFICATION ===
concept: BCH Code
slug: bch-code

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
aliases:
  - "Bose-Chaudhuri-Hocquenghem code"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cyclic-code
  - finite-field
  - minimal-polynomial
extends:
  - cyclic-code
related:
  - polynomial-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a BCH code?"
  - "How are BCH codes constructed?"
---

# Quick Definition

A BCH code is a cyclic code whose generator polynomial is chosen to have consecutive powers of a primitive root of unity as roots, guaranteeing a minimum distance of at least $d$. BCH codes have efficient error-correction algorithms.

# Core Definition

Let $d = 2r + 1$ for some $r \geq 0$. Suppose that $\omega$ is a primitive $n$th root of unity over $\mathbb{Z}_2$, and let $m_i(x)$ be the minimal polynomial over $\mathbb{Z}_2$ of $\omega^i$. If

$$g(x) = \text{lcm}[m_1(x), m_2(x), \ldots, m_{2r}(x)],$$

then the cyclic code $\langle g(t) \rangle$ in $R_n$ is called the **BCH code** of length $n$ and distance $d$ (Judson, p. 301).

By Theorem 22.21, the minimum distance of $C$ is at least $d$.

# Prerequisites

- **Cyclic code** — BCH codes are cyclic codes
- **Finite field** — Uses roots of unity in finite field extensions
- **Minimal polynomial** — The generator is built from minimal polynomials

# Key Properties

1. The minimum distance is at least $d$ (Theorem 22.21)
2. BCH codes have efficient error correction algorithms
3. A code polynomial $f(t)$ is in $C$ if and only if $f(\omega^i) = 0$ for $1 \leq i < d$ (Theorem 22.22)
4. European and transatlantic communication systems use BCH codes

# Construction / Recognition

## To Construct:
1. Find a primitive $n$th root of unity $\omega$ over $\mathbb{Z}_2$
2. Compute minimal polynomials $m_1(x), \ldots, m_{2r}(x)$ of $\omega, \omega^2, \ldots, \omega^{2r}$
3. Set $g(x) = \text{lcm}[m_1(x), \ldots, m_{2r}(x)]$
4. The BCH code is $C = \langle g(t) \rangle$ in $R_n$

# Context & Application

BCH codes are among the most important practical error-correcting codes. They were discovered independently by Hocquenghem (1959) and Bose and Ray-Chaudhuri (1960). A practical example: a (255, 231)-BCH code is used in communication systems with a failure rate of 1 in 16 million.

# Examples

**Example 1** (p. 302): For $n = 15$ and $\omega$ a root of $1 + x + x^4$, the BCH code with $g(x) = m_1(x)m_2(x) = 1 + x^4 + x^6 + x^7 + x^8$ gives a $(15,7)$-code with minimum distance at least 5.

# Relationships

## Builds Upon
- **Cyclic code** — BCH codes are cyclic
- **Finite field** — Construction uses $GF(2^n)$

## Related
- **Polynomial code** — BCH codes are polynomial codes with special generators

# Source Reference

Chapter 22: Finite Fields, Section 22.2, pages 301–303. See Theorems 22.21, 22.22, Example 22.23.

# Verification Notes

- Definition source: Direct from p. 301
- Confidence: HIGH — explicit definition and construction
- Cross-reference status: Verified
- Uncertainties: None
