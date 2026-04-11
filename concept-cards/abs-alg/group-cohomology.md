---
concept: Group Cohomology
slug: group-cohomology
category: homological-algebra
subcategory: group-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 793
section: "17.2 The Cohomology of Groups"
extraction_confidence: high
aliases:
  - "H^n(G,A)"
  - "cohomology of groups"
prerequisites:
  - ext-functor
  - group-ring
  - module
extends: []
related:
  - crossed-homomorphism
  - group-extension
  - factor-set
contrasts_with: []
answers_questions:
  - "What is group cohomology?"
  - "How does H^0, H^1, H^2 relate to group theory?"
---

# Quick Definition
The n-th cohomology group H^n(G,A) of a group G with coefficients in a ZG-module A is Ext^n_ZG(Z,A), computed using a projective resolution of Z over ZG.

# Core Definition
For a group G and a ZG-module A, the **n-th cohomology group** of G with coefficients in A is H^n(G,A) = Ext^n_ZG(Z,A) (p. 793). Here Z is viewed as a trivial ZG-module. H^0(G,A) = A^G = {a ∈ A | ga = a for all g ∈ G} (the fixed points). H^1(G,A) classifies crossed homomorphisms modulo principal ones. H^2(G,A) classifies group extensions of A by G.

# Prerequisites
- **ext-functor** — Group cohomology is a special case of Ext
- **group-ring** — Coefficients are ZG-modules
- **module** — A must be a ZG-module

# Key Properties
1. H^0(G,A) = A^G (fixed points under G-action)
2. H^1(G,A) = crossed homomorphisms / principal crossed homomorphisms
3. H^2(G,A) classifies group extensions of A by G
4. Long exact sequence from short exact sequences of ZG-modules
5. Computed using the bar resolution or other projective resolutions of Z

# Relationships
## Builds Upon
- **ext-functor** — H^n(G,A) = Ext^n_ZG(Z,A)

## Enables
- **crossed-homomorphism** — H^1 is defined via crossed homomorphisms
- **group-extension** — H^2 classifies extensions

# Source Reference
Chapter 17, Sections 17.2-17.4, pages 793-840.

# Verification Notes
- Confidence: HIGH — major topic with detailed development
