---
# === CORE IDENTIFICATION ===
concept: Error Polynomial
slug: error-polynomial

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
section: "22.5 Additional Exercises"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bch-code
  - polynomial-code
extends: []
related:
  - syndrome
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an error polynomial in coding theory?"
---

# Quick Definition

In the context of BCH codes, the error polynomial $e(t) = t^{a_1} + t^{a_2} + \cdots + t^{a_k}$ represents the positions where bit errors occurred during transmission. The received word is $w(t) = c(t) + e(t)$.

# Core Definition

If a code polynomial $c(t)$ is transmitted and $w(t)$ is received, and errors have occurred in bits $a_1, \ldots, a_k$, then $w(t) = c(t) + e(t)$ where $e(t) = t^{a_1} + t^{a_2} + \cdots + t^{a_k}$ is the **error polynomial** (Judson, p. 305).

The **syndrome** of $w(t)$ is $s_1, \ldots, s_{2r}$ where $s_i = w(\omega^i)$ and $\omega$ is a primitive $n$th root of unity.

# Prerequisites

- **BCH code** — Error polynomials are used in BCH error correction
- **Polynomial code** — Codewords are polynomials

# Key Properties

1. $w(t)$ is a codeword if and only if all syndrome values are zero
2. $s_i = e(\omega^i)$ since $c(\omega^i) = 0$ for codewords
3. The error-locator polynomial $(x + \omega^{a_1})(x + \omega^{a_2}) \cdots (x + \omega^{a_k})$ finds error positions

# Context & Application

Error polynomials and syndromes are the basis of BCH decoding algorithms. The decoder computes the syndrome from the received word and uses it to identify error positions.

# Examples

**Example 1** (p. 305): For a (15,7)-BCH code, if errors occur at positions $a_1$ and $a_2$, the error-locator polynomial is $s(x) = (x + \omega^{a_1})(x + \omega^{a_2})$.

# Relationships

## Builds Upon
- **BCH code** — Error correction context
- **Polynomial code** — Errors are represented as polynomials

## Related
- **Syndrome** — Computed from the error polynomial

# Source Reference

Chapter 22: Finite Fields, Section 22.5, page 305.

# Verification Notes

- Definition source: From Exercise section, p. 305
- Confidence: MEDIUM — defined in exercises/additional material
- Cross-reference status: Verified
- Uncertainties: None
