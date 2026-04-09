---
# === CORE IDENTIFICATION ===
concept: Multiplicity of a Root
slug: multiplicity-of-root

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "order of a root"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial
  - splitting-field
extends: []
related:
  - separable-polynomial
  - simple-root
contrasts_with:
  - simple-root

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the multiplicity of a root of a polynomial?"
---

# Quick Definition

The multiplicity of a root $\alpha_i$ of a polynomial $f(x)$ is the exponent $n_i$ in the factorization $f(x) = \prod (x - \alpha_i)^{n_i}$ over the splitting field.

# Core Definition

Let $E$ be the splitting field of a polynomial $f(x) \in F[x]$. If $f(x)$ factors over $E$ as

$$f(x) = (x - \alpha_1)^{n_1}(x - \alpha_2)^{n_2} \cdots (x - \alpha_r)^{n_r},$$

the **multiplicity** of a root $\alpha_i$ of $f(x)$ is $n_i$. A root with multiplicity 1 is called a **simple root** (Judson, p. 310).

# Prerequisites

- **Polynomial** — Multiplicity is a property of roots of polynomials
- **Splitting field** — Multiplicity is determined in the splitting field

# Key Properties

1. A polynomial of degree $n$ has at most $n$ roots counted with multiplicity
2. A polynomial is separable if and only if all roots have multiplicity 1
3. $f(x)$ has a repeated root if and only if $\gcd(f(x), f'(x)) \neq 1$

# Examples

**Example 1**: $(x-1)^3(x+2)^2$ has root 1 with multiplicity 3 and root $-2$ with multiplicity 2.

**Example 2**: $x^2 - 2 = (x - \sqrt{2})(x + \sqrt{2})$ has two simple roots.

# Relationships

## Related
- **Separable polynomial** — A polynomial with all simple roots

## Contrasts With
- **Simple root** — A root of multiplicity 1

# Source Reference

Chapter 23: Galois Theory, Section 23.1, page 310.

# Verification Notes

- Definition source: Direct from p. 310
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
