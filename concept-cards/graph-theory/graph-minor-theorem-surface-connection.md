---
concept: Graph Minor Theorem and Surfaces
slug: graph-minor-theorem-surface-connection
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
extraction_confidence: medium
aliases:
  - "Robertson-Seymour theorem surface connection"
prerequisites:
  - surface
  - euler-genus
  - kuratowski-theorem
extends: []
related:
  - classification-of-surfaces
  - surgery
contrasts_with: []
answers_questions:
  - "How do surfaces relate to the graph minor theorem?"
---

# Quick Definition
The connection between graphs and surfaces lies at the heart of the Robertson-Seymour graph minor theorem. Euler's formula (generalized to surfaces) provides that distinct surfaces can be distinguished by the arithmetic invariant n - m + l of embedded graphs, enabling the inductive structure of the minor theorem proof.

# Core Definition
"This fundamental connection between graphs and surfaces lies at the heart of the proof of the famous Robertson-Seymour graph minor theorem; see Chapter 12.5" (Diestel, p. 91). The generalized Kuratowski theorem for arbitrary surfaces (Corollary 12.5.3) uses surface surgery (Appendix B) to characterize embeddability.

# Prerequisites
- **Surface**, **Euler genus**, **Kuratowski's theorem**

# Key Properties
1. Each surface has finitely many forbidden minors for embeddability
2. The proof of the graph minor theorem uses induction on surface complexity
3. Surgery on surfaces (Appendix B) provides the induction mechanism
4. Lemma B.6 is used directly in the proof of the generalized Kuratowski theorem

# Relationships
## Builds Upon
- **Surfaces**, **Euler genus**, **Surgery**

## Related
- **Kuratowski's theorem** -- Prototype for surface-specific forbidden minor theorems

# Source Reference
Chapter 4, page 91 (footnote). Appendix B. Chapter 12.5.

# Verification Notes
- Connection stated on p. 91 and throughout Appendix B
- Confidence: MEDIUM -- the connection is described but the actual proof is in Ch. 12
