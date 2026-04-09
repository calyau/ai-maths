---
concept: Euler Genus Bound for Disjoint Circles
slug: euler-genus-bound-circles
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
  - "Lemma B.6"
prerequisites:
  - surgery
  - euler-genus
  - separating-circle
extends: []
related:
  - genus-reduction-lemma
  - genus-additivity-lemma
contrasts_with: []
answers_questions:
  - "How many disjoint non-trivial circles can a surface support?"
---

# Quick Definition
If S has a finite set C of disjoint circles, none bounding a disc, with a component of S \ union(C) whose closure meets every circle, then epsilon(S) >= |C|.

# Core Definition
**Lemma B.6**: Let S be a surface and C a finite set of disjoint circles in S. Assume none bounds a disc and S \ union(C) has a component D_0 whose closure meets every circle. Then epsilon(S) >= |C| (Diestel, p. 366).

# Prerequisites
- **Surgery**, **Euler genus**, **Separating circle**

# Key Properties
1. Bounds the number of disjoint non-trivial circles by the Euler genus
2. The proof partitions circles into one-sided, two-sided non-separating, and separating
3. Uses sequential surgery to reduce genus

# Context & Application
This lemma is used in the direct proof of the generalized Kuratowski theorem for arbitrary surfaces (Corollary 12.5.3 in Ch. 12).

# Relationships
## Builds Upon
- **Genus reduction lemma**, **Genus additivity lemma**

# Source Reference
Appendix B, Lemma B.6, pages 366-367.

# Verification Notes
- Full proof given pp. 366-367
- Confidence: HIGH
