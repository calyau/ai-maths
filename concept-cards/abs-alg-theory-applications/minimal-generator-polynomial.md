---
# === CORE IDENTIFICATION ===
concept: Minimal Generator Polynomial
slug: minimal-generator-polynomial

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
  - "generator polynomial"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cyclic-code
  - polynomial
extends: []
related:
  - bch-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the minimal generator polynomial of a cyclic code?"
---

# Quick Definition

The minimal generator polynomial of a cyclic code $C = \langle g(t) \rangle$ in $R_n$ is the unique monic polynomial $g(x)$ of smallest degree that generates $C$. It must divide $x^n - 1$.

# Core Definition

Every ideal $C$ in $R_n = \mathbb{Z}_2[x]/\langle x^n - 1 \rangle$ is of the form $C = \langle g(t) \rangle$ for some unique monic polynomial $g(x)$ that divides $x^n - 1$. The unique monic polynomial of the smallest degree that generates $C$ is called the **minimal generator polynomial** of $C$ (Judson, p. 298).

# Prerequisites

- **Cyclic code** — The generator polynomial generates a cyclic code
- **Polynomial** — Generator polynomials are polynomials in $\mathbb{Z}_2[x]$

# Key Properties

1. $g(x)$ divides $x^n - 1$ in $\mathbb{Z}_2[x]$
2. The code $C$ has dimension $k = n - \deg g(x)$
3. The factorization $x^n - 1 = g(x)h(x)$ gives both the generator and the parity-check polynomial
4. The number of cyclic codes of length $n$ equals the number of monic divisors of $x^n - 1$

# Examples

**Example 1** (p. 298): For $x^7 - 1 = (1+x)(1+x+x^3)(1+x^2+x^3)$ in $\mathbb{Z}_2[x]$, the polynomial $g(x) = 1 + x + x^3$ generates a $(7,4)$-cyclic code.

# Relationships

## Builds Upon
- **Cyclic code** — The generator polynomial generates the code

## Related
- **BCH code** — The generator is constructed from minimal polynomials of roots of unity

# Source Reference

Chapter 22: Finite Fields, Section 22.2, page 298.

# Verification Notes

- Definition source: Direct from p. 298
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
