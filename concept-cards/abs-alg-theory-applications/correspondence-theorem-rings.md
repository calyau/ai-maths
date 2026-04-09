---
# === CORE IDENTIFICATION ===
concept: Correspondence Theorem for Rings
slug: correspondence-theorem-rings

# === CLASSIFICATION ===
category: ring-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Rings"
chapter_number: 16
pdf_page: 212
section: "16.3 Ring Homomorphisms and Ideals"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Fourth Isomorphism Theorem for rings"
  - "lattice isomorphism theorem for rings"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - ideal
  - factor-ring
extends: []
related:
  - first-isomorphism-theorem-rings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Correspondence Theorem for rings?"
  - "How do ideals of a quotient ring relate to ideals of the original ring?"
---

# Quick Definition

There is a one-to-one correspondence between subrings of $R$ containing ideal $I$ and subrings of $R/I$, given by $S \mapsto S/I$. Under this correspondence, ideals correspond to ideals.

# Core Definition

"Let $I$ be an ideal of a ring $R$. Then $S \mapsto S/I$ is a one-to-one correspondence between the set of subrings $S$ containing $I$ and the set of subrings of $R/I$. Furthermore, the ideals of $R$ containing $I$ correspond to ideals of $R/I$" (Judson, Theorem 16.34, p. 212).

# Prerequisites

- **Ideal** — The theorem concerns ideals
- **Factor ring** — The theorem involves $R/I$

# Key Properties

1. Subrings of $R$ containing $I$ correspond bijectively to subrings of $R/I$
2. Ideals of $R$ containing $I$ correspond bijectively to ideals of $R/I$
3. The correspondence preserves inclusion

# Construction / Recognition

## To Apply:
1. Form the quotient $R/I$
2. Ideals of $R/I$ are exactly the images $J/I$ where $J$ is an ideal of $R$ containing $I$

# Context & Application

This theorem is essential for understanding the ideal structure of quotient rings. It explains how maximal and prime ideals "pass through" to quotient rings.

# Examples

**Example 1**: The ideals of $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}_6$ correspond to ideals of $\mathbb{Z}$ containing $6\mathbb{Z}$: namely $\mathbb{Z}$, $2\mathbb{Z}$, $3\mathbb{Z}$, and $6\mathbb{Z}$.

# Relationships

## Related
- **First Isomorphism Theorem for rings** — Complementary structural result

# Common Errors

- **Error**: Looking for ideals of $R/I$ that don't come from ideals of $R$
  **Correction**: Every ideal of $R/I$ is of the form $J/I$ for some ideal $J \supset I$ of $R$

# Common Confusions

- **Confusion**: Thinking all subrings of $R$ (not just those containing $I$) correspond to subrings of $R/I$
  **Clarification**: Only subrings containing $I$ participate in the correspondence

# Source Reference

Chapter 16: Rings, Section 16.3, Theorem 16.34, page 212.

# Verification Notes

- Definition source: Direct from Theorem 16.34
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
