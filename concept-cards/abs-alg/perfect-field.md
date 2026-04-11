---
concept: Perfect Field
slug: perfect-field
category: field-theory
subcategory: separability
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Field Theory"
chapter_number: 13
pdf_page: 549
section: "13.5 Separable and Inseparable Extensions"
extraction_confidence: high
aliases: []
prerequisites:
  - separable-extension
extends: []
related:
  - finite-field-classification
contrasts_with: []
answers_questions:
  - "What is a perfect field?"
---

# Quick Definition
A field F is perfect if every irreducible polynomial over F is separable. All fields of characteristic 0 and all finite fields are perfect.

# Core Definition
A field F is perfect if every algebraic extension of F is separable, equivalently if every irreducible polynomial in F[x] is separable. A field of characteristic 0 is always perfect. A field of characteristic p is perfect iff $F = F^p$ (every element has a pth root in F). All finite fields are perfect (Dummit & Foote, pp. 549-550).

# Prerequisites
- **separable-extension** — Perfect fields are those where all extensions are separable

# Key Properties
1. Characteristic 0 fields are always perfect
2. Finite fields are perfect
3. A field of char p is perfect iff $F^p = F$ (Frobenius is surjective)
4. $\mathbb{F}_p(t)$ is NOT perfect: $x^p - t$ is irreducible but inseparable

# Relationships
## Builds Upon
- **separable-extension**

## Related
- **finite-field-classification** — Finite fields are perfect

# Source Reference
Chapter 13, Section 13.5, pp. 549-550.

# Verification Notes
- Confidence: HIGH — explicit definition
