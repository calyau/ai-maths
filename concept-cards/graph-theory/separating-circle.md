---
concept: Separating and Non-Separating Circles
slug: separating-circle
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "non-separating circle"
  - "separating circle on a surface"
prerequisites:
  - surface
  - orientable-surface
extends: []
related:
  - surgery
  - euler-genus
contrasts_with: []
answers_questions:
  - "What is a separating circle on a surface?"
  - "What is a non-separating circle?"
---

# Quick Definition
A circle C on a surface S is separating if S \ C has two components, and non-separating if S \ C remains connected. Every surface other than the sphere has a non-separating circle.

# Core Definition
"If S \ C has two components, we call C a separating circle in S; if it has only one, then C is non-separating" (Diestel, p. 362). One-sided circles are always non-separating; two-sided circles can be either.

# Prerequisites
- **Surface** and **Orientable surface** (for one-sided/two-sided distinction)

# Key Properties
1. One-sided circles are always non-separating
2. Two-sided circles can be separating or non-separating
3. Every surface except S^2 has a non-separating circle (Lemma B.1)
4. Cutting along a non-separating circle reduces Euler genus (Lemma B.4)
5. Cutting along a separating circle decomposes genus additively (Lemma B.5)

# Context & Application
Non-separating circles are the key tool for induction on surfaces. By cutting along such a circle and capping holes, one obtains a surface of smaller Euler genus, enabling inductive proofs. Lemma B.1 guarantees that this process can always be started (unless the surface is already a sphere).

# Relationships
## Enables
- **Surgery** -- Cutting along circles reduces surface complexity
- Induction on Euler genus

## Related
- **Euler genus** -- Reduced by cutting

# Source Reference
Appendix B, page 362. Lemmas B.1, B.4, B.5.

# Verification Notes
- Definitions from p. 362
- Confidence: HIGH -- explicit definitions with supporting lemmas
