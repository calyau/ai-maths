---
# === CORE IDENTIFICATION ===
concept: Parity-Check Matrix for Cyclic Codes
slug: parity-check-matrix-cyclic

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
  - cyclic-code
  - minimal-generator-polynomial
extends: []
related:
  - bch-code
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the parity-check matrix of a cyclic code determined?"
---

# Quick Definition

For a cyclic code $C = \langle g(t) \rangle$ with $x^n - 1 = g(x)h(x)$, the parity-check matrix $H$ is constructed from the coefficients of $h(x)$ and satisfies $HG = 0$ where $G$ is the generator matrix.

# Core Definition

Let $C = \langle g(t) \rangle$ be a cyclic code in $R_n$ and suppose $x^n - 1 = g(x)h(x)$ where $h(x) = h_0 + h_1x + \cdots + h_kx^k$. The parity-check matrix for $C$ is the $(n-k) \times n$ matrix

$$H = \begin{pmatrix} 0 & \cdots & 0 & h_k & \cdots & h_0 \\ 0 & \cdots & h_k & \cdots & h_0 & 0 \\ & & \cdots & & & \\ h_k & \cdots & h_0 & 0 & \cdots & 0 \end{pmatrix}$$

(Judson, Proposition 22.18, p. 299). Furthermore, $HG = 0$.

# Prerequisites

- **Cyclic code** — The code whose parity-check matrix is constructed
- **Minimal generator polynomial** — Determines the generator matrix

# Key Properties

1. $H$ has dimensions $(n-k) \times n$
2. $HG = 0$ where $G$ is the generator matrix
3. A word $w$ is a codeword if and only if $Hw^T = 0$
4. The polynomial $h(x)$ is called the check polynomial

# Examples

**Example 1** (p. 299): For the $(7,4)$-code with $x^7 - 1 = (1+x+x^3)(1+x+x^2+x^4)$, the parity-check matrix is the $3 \times 7$ matrix constructed from $h(x) = 1+x+x^2+x^4$.

# Relationships

## Builds Upon
- **Cyclic code** — The code structure
- **Minimal generator polynomial** — The complementary polynomial gives $H$

## Related
- **BCH code** — Uses a specialized parity-check matrix

# Source Reference

Chapter 22: Finite Fields, Section 22.2, page 299. Proposition 22.18.

# Verification Notes

- Definition source: Direct from Proposition 22.18, p. 299
- Confidence: HIGH — explicit proposition
- Cross-reference status: Verified
- Uncertainties: None
