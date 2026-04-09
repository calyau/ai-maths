---
# === CORE IDENTIFICATION ===
concept: Cyclicity of Finite Field Multiplicative Group
slug: cyclicity-of-finite-field-multiplicative-group

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
  - cyclic-group
extends: []
related:
  - frobenius-automorphism
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of the non-zero elements of a finite field?"
  - "Why is the multiplicative group of a finite field cyclic?"
---

# Quick Definition

The multiplicative group of nonzero elements of any finite field is cyclic. More generally, every finite subgroup of the multiplicative group of any field is cyclic.

# Core Definition

**Theorem 22.10.** If $G$ is a finite subgroup of $F^*$, the multiplicative group of nonzero elements of a field $F$, then $G$ is cyclic (Judson, p. 295).

**Corollary 22.11.** The multiplicative group of all nonzero elements of a finite field is cyclic (p. 295).

# Prerequisites

- **Finite field** — The theorem concerns finite fields
- **Cyclic group** — The multiplicative group has this structure

# Key Properties

1. $GF(p^n)^*$ is cyclic of order $p^n - 1$
2. A generator of this cyclic group is called a primitive element
3. Every finite extension of a finite field is simple (Corollary 22.12), because the generator of $E^*$ generates $E$ over $F$
4. The proof uses the Fundamental Theorem of Finite Abelian Groups

# Examples

**Example 1** (p. 295): The multiplicative group of $GF(2^4)$ is isomorphic to $\mathbb{Z}_{15}$ with generator $\alpha$ where $1 + \alpha + \alpha^4 = 0$.

# Relationships

## Builds Upon
- **Finite field** — The result concerns finite fields
- **Cyclic group** — The multiplicative group is cyclic

## Enables
- **Frobenius automorphism** — Uses the cyclic structure

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 295. See Theorem 22.10, Corollaries 22.11, 22.12.

# Verification Notes

- Definition source: Direct from Theorem 22.10 and Corollary 22.11
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
