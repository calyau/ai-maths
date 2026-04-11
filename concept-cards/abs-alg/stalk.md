---
concept: Stalk
slug: stalk
category: algebraic-geometry
subcategory: scheme-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 741
section: "15.5 The Prime Spectrum of a Ring"
extraction_confidence: medium
aliases: []
prerequisites:
  - structure-sheaf
  - localization
extends: []
related:
  - local-ring
contrasts_with: []
answers_questions:
  - "What is a stalk of a sheaf?"
---

# Quick Definition
The stalk of the structure sheaf at a point P ∈ Spec R is the local ring R_P, obtained by localizing R at the prime ideal P.

# Core Definition
For the structure sheaf O on Spec R, the **stalk** at a point P is O_P = R_P, the localization of R at P. It captures the "local behavior" of functions near P. The stalk is always a local ring with maximal ideal PR_P.

# Prerequisites
- **structure-sheaf** — The stalk is a local invariant of the sheaf
- **localization** — The stalk equals R_P

# Key Properties
1. O_P = R_P is a local ring
2. An element of R is determined by its values at all stalks (if R has no nilpotents)

# Relationships
## Builds Upon
- **localization** — The stalk R_P is a localization

# Source Reference
Chapter 15, Section 15.5, page 741.

# Verification Notes
- Confidence: MEDIUM — briefly discussed
