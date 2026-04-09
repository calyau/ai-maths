---
concept: Galois Extension Equivalence
slug: galois-theory-equivalence
category: galois-theory
subcategory: field-automorphisms
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - normal-extension
  - separable-extension
  - splitting-field
  - fixed-field
extends: []
related:
  - galois-extension
  - fundamental-theorem-of-galois-theory
contrasts_with: []
answers_questions:
  - "What are the equivalent conditions for a Galois extension?"
---

# Quick Definition

Three equivalent conditions define a Galois extension $E/F$: (1) $E$ is finite, normal, and separable over $F$; (2) $E$ is the splitting field of a separable polynomial over $F$; (3) $F = E_G$ for some finite group $G$ of automorphisms of $E$.

# Core Definition

**Theorem 23.19.** Let $E$ be a field extension of $F$. The following are equivalent (Judson, p. 313):

1. $E$ is a finite, normal, separable extension of $F$.
2. $E$ is a splitting field over $F$ of a separable polynomial.
3. $F = E_G$ for some finite group $G$ of automorphisms of $E$.

# Prerequisites

- **Normal extension** — Condition in (1)
- **Separable extension** — Condition in (1)
- **Splitting field** — Condition in (2)
- **Fixed field** — Condition in (3)

# Key Properties

1. $(1) \Rightarrow (2)$: By the Primitive Element Theorem, $E = F(\alpha)$; take $f$ as the minimal polynomial
2. $(2) \Rightarrow (3)$: $E_{G(E/F)} = F$ by Proposition 23.17
3. $(3) \Rightarrow (1)$: Uses Artin's Lemma and the structure of the fixed field

# Context & Application

This theorem characterizes Galois extensions from three different perspectives: intrinsic properties (normal + separable), constructive (splitting field), and group-theoretic (fixed field). Having all three viewpoints is essential for applications.

# Relationships

## Builds Upon
- All four prerequisites listed above

## Enables
- **Fundamental Theorem of Galois Theory** — Applies to these extensions

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 313–314. Theorem 23.19.

# Verification Notes

- Definition source: Direct from Theorem 23.19, p. 313
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified
- Uncertainties: None
