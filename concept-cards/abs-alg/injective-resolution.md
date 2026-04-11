---
concept: Injective Resolution
slug: injective-resolution
category: homological-algebra
subcategory: resolutions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 787
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases: []
prerequisites:
  - module
  - injective-module
extends: []
related:
  - ext-functor
  - projective-resolution
contrasts_with:
  - projective-resolution
answers_questions:
  - "What is an injective resolution?"
---

# Quick Definition
An injective resolution of a module D is an exact sequence 0 → D → E^0 → E^1 → ··· where each E^i is injective. The Ext groups can also be computed from injective resolutions.

# Core Definition
An **injective resolution** of an R-module D is an exact sequence 0 → D → E^0 → E^1 → ··· where each E^i is an injective R-module (p. 787). Ext^n_R(A,D) can be computed using either a projective resolution of A or an injective resolution of D, giving the same groups (Theorem 8).

# Prerequisites
- **module** — D is an R-module
- **injective-module** — The E^i must be injective

# Key Properties
1. Every module has an injective resolution
2. Ext computed from injective resolutions agrees with Ext from projective resolutions

# Relationships
## Contrasts With
- **projective-resolution** — Dual approach

# Source Reference
Chapter 17, Section 17.1, pages 787-788.

# Verification Notes
- Confidence: HIGH — stated with comparison to projective approach
