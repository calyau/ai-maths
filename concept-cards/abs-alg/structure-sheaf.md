---
concept: Structure Sheaf
slug: structure-sheaf
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
aliases:
  - "sheaf of regular functions"
  - "O_X"
prerequisites:
  - prime-spectrum
  - localization
extends: []
related:
  - stalk
  - ringed-space
contrasts_with: []
answers_questions:
  - "What is the structure sheaf on Spec R?"
---

# Quick Definition
The structure sheaf O on Spec R assigns to each open set U the ring of "regular functions" on U — elements that locally look like fractions r/d. The stalk at P is the local ring R_P.

# Core Definition
The **structure sheaf** O on X = Spec R assigns to each basic open set D(f) = {P | f ∉ P} the localization R_f, and to more general open sets U the ring of sections O(U) = {s: U → ∐R_P | s is locally a fraction}. The stalk O_P at P ∈ Spec R is the local ring R_P. The pair (Spec R, O) is called an **affine scheme** (p. 741-742).

# Prerequisites
- **prime-spectrum** — The underlying topological space
- **localization** — Stalks and sections involve localization

# Key Properties
1. The stalk at P is the local ring R_P
2. On basic open sets D(f), the ring of sections is R_f
3. Global sections O(Spec R) = R
4. (Spec R, O) is a locally ringed space

# Relationships
## Builds Upon
- **prime-spectrum** — The topological space
- **localization** — Provides the local rings

# Source Reference
Chapter 15, Section 15.5, pages 741-742.

# Verification Notes
- Confidence: MEDIUM — discussed briefly, not as detailed as earlier sections
