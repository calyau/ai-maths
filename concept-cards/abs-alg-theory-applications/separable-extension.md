---
# === CORE IDENTIFICATION ===
concept: Separable Extension
slug: separable-extension

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
  - separable-polynomial
  - extension-field
extends:
  - extension-field
related:
  - normal-extension
  - galois-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a separable extension?"
  - "When is an extension automatically separable?"
---

# Quick Definition

An extension $E$ of $F$ is a separable extension if every element in $E$ is the root of a separable polynomial in $F[x]$ (i.e., a polynomial with no repeated roots in its splitting field).

# Core Definition

An extension $E$ of $F$ is a **separable extension** of $F$ if every element in $E$ is the root of a separable polynomial in $F[x]$ (Judson, p. 293).

# Prerequisites

- **Separable polynomial** — Separable extensions are defined via separable polynomials
- **Extension field** — Separable extensions are field extensions

# Key Properties

1. Every extension of a field of characteristic 0 is separable (Proposition 23.12)
2. Every extension of a finite field is separable
3. Separability + normality + finiteness = Galois extension (Theorem 23.19)
4. Every finite separable extension has a primitive element (Primitive Element Theorem, Theorem 23.13)

# Context & Application

Separability is one of the two conditions (along with normality) needed for the Fundamental Theorem of Galois Theory to apply. In practice, extensions of $\mathbb{Q}$ and finite fields are always separable, so the condition is automatic in many common settings.

# Examples

**Example 1** (p. 293): $\mathbb{Q}(\sqrt{2})$ is a separable extension of $\mathbb{Q}$. Every element $a + b\sqrt{2}$ is a root of the separable polynomial $x^2 - 2ax + (a^2 - 2b^2)$.

# Relationships

## Builds Upon
- **Separable polynomial** — Every element satisfies a separable polynomial
- **Extension field** — A type of field extension

## Enables
- **Galois theory** — The Fundamental Theorem requires separable extensions
- **Primitive Element Theorem** — Applies to finite separable extensions

## Related
- **Normal extension** — Together with separability, defines Galois extensions

# Source Reference

Chapter 22: Finite Fields, Section 22.1, page 293. Also Chapter 23, Proposition 23.12 and Theorem 23.13.

# Verification Notes

- Definition source: Direct from p. 293
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
