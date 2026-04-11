---
concept: Homology Group
slug: homology-group
category: homological-algebra
subcategory: complexes
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Homological Algebra and Group Cohomology"
chapter_number: 17
pdf_page: 776
section: "17.1 Introduction to Homological Algebra"
extraction_confidence: high
aliases:
  - "cohomology group"
  - "H^n"
prerequisites:
  - chain-complex
extends: []
related:
  - exact-sequence
contrasts_with: []
answers_questions:
  - "What is a homology/cohomology group?"
---

# Quick Definition
The n-th cohomology group of a cochain complex C is H^n(C) = ker d_{n+1}/image d_n. It measures the failure of exactness at the n-th stage.

# Core Definition
For a cochain complex C with maps d_n, the **n-th cohomology group** is H^n(C) = ker d_{n+1}/image d_n (Definition, p. 776). Elements of ker d_{n+1} are called cocycles; elements of image d_n are coboundaries. H^n = 0 iff the complex is exact at stage n.

# Prerequisites
- **chain-complex** — Cohomology is defined for complexes

# Key Properties
1. H^n = 0 iff exact at stage n
2. Homomorphisms of complexes induce maps on cohomology
3. Short exact sequence of complexes → long exact sequence in cohomology

# Relationships
## Builds Upon
- **chain-complex** — Defined as quotients in chain complexes

# Source Reference
Chapter 17, Section 17.1, Definition, page 776.

# Verification Notes
- Confidence: HIGH — standard definition
