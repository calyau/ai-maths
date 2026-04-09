---
# === CORE IDENTIFICATION ===
concept: UFD Polynomial Ring Theorem
slug: ufd-polynomial-ring

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 247
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unique-factorization-domain
  - polynomial-ring
  - gausss-lemma-ufd
extends: []
related:
  - domain-hierarchy
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a polynomial ring a UFD?"
  - "Is Z[x] a UFD?"
---

# Quick Definition

If $D$ is a UFD, then $D[x]$ is also a UFD. By induction, $D[x_1, \ldots, x_n]$ is a UFD. This is how we know $\mathbb{Z}[x]$ is a UFD.

# Core Definition

"If $D$ is a UFD, then $D[x]$ is a UFD" (Judson, Theorem 18.29, p. 247). The proof uses Gauss's Lemma (primitive polynomial version) and the fact that $F[x]$ is a UFD (where $F$ is the field of fractions of $D$).

# Prerequisites

- **UFD** — The base ring must be a UFD
- **Polynomial ring** — The result concerns $D[x]$
- **Gauss's Lemma (UFD)** — Key tool in the proof

# Key Properties

1. $D$ UFD $\Rightarrow$ $D[x]$ UFD
2. By induction: $D$ UFD $\Rightarrow$ $D[x_1, \ldots, x_n]$ UFD (Corollary 18.32)
3. $\mathbb{Z}[x]$ is a UFD (Corollary 18.31)
4. $F[x]$ is a UFD for any field $F$ (Corollary 18.30)

# Construction / Recognition

## To Apply:
1. Verify $D$ is a UFD
2. Conclude $D[x]$ is a UFD

# Context & Application

This theorem extends unique factorization from a domain to its polynomial ring. It is essential for algebraic geometry (polynomial rings are UFDs) and number theory.

# Examples

**Example 1** (p. 248): $\mathbb{Z}[x]$ is a UFD since $\mathbb{Z}$ is a UFD.

**Example 2**: $\mathbb{Q}[x,y]$ is a UFD since $\mathbb{Q}$ is a UFD (field), $\mathbb{Q}[x]$ is a UFD, then $\mathbb{Q}[x][y] = \mathbb{Q}[x,y]$ is a UFD.

# Relationships

## Builds Upon
- **UFD** — The base ring property
- **Gauss's Lemma (UFD)** — Product of primitives is primitive

## Enables
- **$\mathbb{Z}[x]$ is a UFD** — Key application

# Common Errors

- **Error**: Assuming $D[x]$ is a PID when $D$ is a UFD
  **Correction**: $\mathbb{Z}[x]$ is a UFD but not a PID

# Common Confusions

- **Confusion**: Thinking that "UFD" and "PID" are preserved the same way by polynomial extension
  **Clarification**: UFD is preserved ($D$ UFD $\Rightarrow$ $D[x]$ UFD), but PID is not ($\mathbb{Z}$ is PID but $\mathbb{Z}[x]$ is not)

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Theorem 18.29 and Corollaries 18.30-18.32, pages 247-248.

# Verification Notes

- Definition source: Direct from Theorem 18.29
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
