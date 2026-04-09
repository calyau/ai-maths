---
concept: Surgery on Surfaces
slug: surgery
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
  - "cutting and capping"
  - "surface surgery"
prerequisites:
  - surface
  - separating-circle
  - euler-genus
extends: []
related:
  - classification-of-surfaces
contrasts_with: []
answers_questions:
  - "How is surgery used to simplify surfaces?"
  - "What happens when you cut a surface along a circle?"
---

# Quick Definition
Surgery on a surface involves cutting along a non-separating circle and capping the resulting holes with discs to produce a surface of smaller Euler genus. This enables induction on surface complexity.

# Core Definition
"To cut S along C, we form a new space S' from S by replacing every point x in C with two points x', x'' and defining the topology on the modified set" appropriately. "We turn S' into a surface by capping its holes: for each boundary circle we take a disc and identify its boundary circle with the hole" (Diestel, pp. 364-365).

# Prerequisites
- **Surface**, **Separating circle**, **Euler genus**

# Key Properties
1. Cutting along a non-separating one-sided circle: epsilon decreases by 1 (Lemma B.4(i))
2. Cutting along a non-separating two-sided circle: epsilon decreases by 2 (Lemma B.4(ii))
3. Cutting along a separating circle: epsilon(S) = epsilon(S') + epsilon(S'') (Lemma B.5)
4. If the separating circle does not bound a disc, both pieces have smaller genus

# Context & Application
Surgery is the main technique for induction on surfaces. Since every non-sphere surface has a non-separating circle (Lemma B.1), we can always reduce to simpler surfaces. This is used extensively in the proof of the graph minor theorem and the generalized Kuratowski theorem (Chapter 12.5).

# Relationships
## Builds Upon
- **Separating circle**, **Euler genus**

## Enables
- Induction proofs on surface complexity
- **Graph minor theorem** (Chapter 12)

# Source Reference
Appendix B, pages 364-367. Lemmas B.4, B.5, B.6.

# Verification Notes
- Definitions adapted from pp. 364-365
- Confidence: HIGH -- detailed description with supporting lemmas
