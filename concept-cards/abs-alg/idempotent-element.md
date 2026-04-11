---
concept: Idempotent Element
slug: idempotent-element
category: ring-theory
subcategory: ring-elements
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 269
section: "7.6 The Chinese Remainder Theorem"
extraction_confidence: high
aliases: []
prerequisites:
  - ring-with-identity
extends: []
related:
  - boolean-ring
  - direct-product-of-rings
contrasts_with:
  - nilpotent-element
answers_questions:
  - "What is an idempotent element?"
---

# Quick Definition
An element $e \in R$ is idempotent if $e^2 = e$.

# Core Definition
An element $e \in R$ is called an *idempotent* if $e^2 = e$. If e is a central idempotent ($er = re$ for all r), then $R \cong Re \times R(1-e)$ (Exercise 1, Dummit & Foote, p. 269).

# Prerequisites
- **Ring with identity** — Nontrivial idempotents require the ring to have structure

# Key Properties
1. 0 and 1 are always idempotent (trivial idempotents)
2. If e is a central idempotent, $R \cong Re \times R(1-e)$ (Exercise 1)
3. In a Boolean ring, every element is idempotent
4. Nontrivial idempotents exist in $R_1 \times R_2$: e.g., $(1, 0)$

# Examples
**Example**: In $\mathbb{Z}/6\mathbb{Z}$, $\bar{3}$ and $\bar{4}$ are idempotents since $3^2 = 9 \equiv 3$ and $4^2 = 16 \equiv 4$.

# Relationships

## Related
- **boolean-ring** — Every element is idempotent
- **direct-product-of-rings** — Nontrivial idempotents decompose rings

## Contrasts With
- **nilpotent-element** — Nilpotent: $x^n = 0$; idempotent: $x^2 = x$

# Source Reference
Chapter 7, Section 7.6, Exercise 1, page 269.

# Verification Notes
- Definition: From Exercise 1, p. 269
- Confidence: HIGH — standard definition
