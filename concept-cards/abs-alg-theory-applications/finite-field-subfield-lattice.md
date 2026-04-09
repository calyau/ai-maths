---
# === CORE IDENTIFICATION ===
concept: Finite Field Subfield Lattice
slug: finite-field-subfield-lattice

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
section: "22.1 Structure of a Finite Field"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-field
  - degree-of-field-extension
extends: []
related:
  - tower-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the possible subfields of a finite field?"
  - "How is the subfield structure of a finite field determined?"
---

# Quick Definition

Every subfield of $GF(p^n)$ has order $p^m$ where $m$ divides $n$. Conversely, for each divisor $m$ of $n$, there is a unique subfield of $GF(p^n)$ isomorphic to $GF(p^m)$.

# Core Definition

**Theorem 22.7.** Every subfield of the Galois field $GF(p^n)$ has $p^m$ elements, where $m$ divides $n$. Conversely, if $m \mid n$ for $m > 0$, then there exists a unique subfield of $GF(p^n)$ isomorphic to $GF(p^m)$ (Judson, p. 294).

# Prerequisites

- **Finite field** — The theorem concerns subfields of finite fields
- **Degree of field extension** — The tower law provides the divisibility constraint

# Key Properties

1. The subfield lattice of $GF(p^n)$ is isomorphic to the divisor lattice of $n$
2. $GF(p^m)$ is a subfield of $GF(p^n)$ if and only if $m \mid n$
3. The proof uses $p^m - 1 \mid p^n - 1$ when $m \mid n$

# Examples

**Example 1** (p. 294): The lattice of subfields of $GF(p^{24})$ includes $GF(p), GF(p^2), GF(p^3), GF(p^4), GF(p^6), GF(p^8), GF(p^{12}), GF(p^{24})$, corresponding to the divisors of 24.

# Relationships

## Builds Upon
- **Finite field** — Concerns subfields of finite fields
- **Degree of field extension** — Uses the tower law

## Related
- **Tower theorem** — The divisibility comes from $[GF(p^n):GF(p)] = [GF(p^n):GF(p^m)][GF(p^m):GF(p)]$

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 294. Theorem 22.7.

# Verification Notes

- Definition source: Direct from Theorem 22.7, p. 294
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
