---
concept: Existence of Non-Separating Circles
slug: non-separating-circle-existence
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
  - "Lemma B.1"
prerequisites:
  - surface
  - separating-circle
  - classification-of-surfaces
extends: []
related:
  - surgery
  - euler-genus
contrasts_with: []
answers_questions:
  - "Does every non-sphere surface contain a non-separating circle?"
---

# Quick Definition
Every surface other than the sphere contains a non-separating circle (Lemma B.1). This is the key fact enabling induction on surface complexity.

# Core Definition
**Lemma B.1**: "Every surface other than the sphere contains a non-separating circle" (Diestel, p. 362).

# Prerequisites
- **Surface**, **Separating circle**, **Classification of surfaces**

# Key Properties
1. Direct corollary of the classification theorem
2. Handles produce two-sided non-separating circles (the middle circle of the cylinder)
3. Crosscaps produce one-sided circles
4. Enables surgery: cut along the circle, cap, get a simpler surface

# Context & Application
This lemma is the induction engine for proofs about surfaces. Since every non-sphere surface has a non-separating circle, we can always perform surgery to reduce Euler genus, providing the inductive step.

# Relationships
## Enables
- **Surgery** -- Provides a circle to cut along
- Induction on Euler genus

# Source Reference
Appendix B, Lemma B.1, page 362.

# Verification Notes
- Lemma stated on p. 362
- Confidence: HIGH
