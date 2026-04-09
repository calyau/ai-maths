---
concept: Genus Additivity Lemma
slug: genus-additivity-lemma
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
  - "Lemma B.5"
prerequisites:
  - surgery
  - separating-circle
  - euler-genus
extends: []
related:
  - genus-reduction-lemma
contrasts_with: []
answers_questions:
  - "How does cutting along a separating circle affect the Euler genus?"
---

# Quick Definition
When cutting a surface S along a separating circle C, the Euler genus is additive: epsilon(S) = epsilon(S') + epsilon(S''). If C does not bound a disc, both pieces have smaller genus.

# Core Definition
**Lemma B.5**: If C is a separating circle in S producing surfaces S' and S'', then epsilon(S) = epsilon(S') + epsilon(S''). If C does not bound a disc, both S' and S'' have smaller Euler genus than S (Diestel, p. 365).

# Prerequisites
- **Surgery**, **Separating circle**, **Euler genus**

# Key Properties
1. Euler genus is additive under separation
2. Both pieces are strictly simpler if C does not bound a disc
3. Provides an alternative induction route via separating circles

# Relationships
## Related
- **Genus reduction lemma** (Lemma B.4) -- For non-separating circles

# Source Reference
Appendix B, Lemma B.5, page 365.

# Verification Notes
- Lemma from p. 365
- Confidence: HIGH
