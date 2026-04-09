---
concept: Genus Reduction Lemma
slug: genus-reduction-lemma
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
  - "Lemma B.4"
prerequisites:
  - surgery
  - separating-circle
  - euler-genus
extends: []
related:
  - genus-additivity-lemma
contrasts_with: []
answers_questions:
  - "How does cutting along a non-separating circle affect the Euler genus?"
---

# Quick Definition
Cutting a surface S along a non-separating circle C and capping reduces the Euler genus: by 1 if C is one-sided, by 2 if C is two-sided.

# Core Definition
**Lemma B.4**: Let C be a non-separating circle in S, and S' the result of cutting and capping. (i) If C is one-sided, epsilon(S') = epsilon(S) - 1. (ii) If C is two-sided, epsilon(S') = epsilon(S) - 2 (Diestel, p. 365).

# Prerequisites
- **Surgery**, **Separating circle**, **Euler genus**

# Key Properties
1. One-sided non-separating: epsilon decreases by 1
2. Two-sided non-separating: epsilon decreases by 2
3. Provides the induction step for surface arguments

# Relationships
## Enables
- Induction on Euler genus

## Related
- **Genus additivity** (Lemma B.5) -- For separating circles

# Source Reference
Appendix B, Lemma B.4, page 365.

# Verification Notes
- Lemma from p. 365
- Confidence: HIGH
