---
concept: Well Ordering
slug: well-ordering
category: foundations
subcategory: order-theory
tier: foundational
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix I: Cartesian Products and Zorn's Lemma"
chapter_number: null
pdf_page: 908
section: "2. Partially Ordered Sets and Zorn's Lemma"
extraction_confidence: high
aliases:
  - "well ordering principle"
prerequisites:
  - total-order
extends:
  - total-order
related:
  - zorns-lemma
  - axiom-of-choice
contrasts_with: []
answers_questions:
  - "What is a well ordering?"
---

# Quick Definition
A well ordering on a set A is a total ordering such that every nonempty subset has a minimum element. The Well Ordering Principle states every set has a well ordering.

# Core Definition
A **well ordering** on A is a total ordering such that every nonempty subset of A has a minimum element (Definition, p. 908). The **Well Ordering Principle** states that every nonempty set has a well ordering. This is equivalent to the Axiom of Choice and Zorn's Lemma (Theorem 2).

# Prerequisites
- **total-order** — A well ordering is a total ordering with additional property

# Examples
**Example**: Z^+ with ≤ is well ordered. R with ≤ is not (e.g., R^+ has no minimum).

# Relationships
## Related
- **zorns-lemma** — Equivalent (Theorem 2)
- **axiom-of-choice** — Equivalent (Theorem 2)

# Source Reference
Appendix I, Section 2, Definition and Theorem 2, page 908.

# Verification Notes
- Confidence: HIGH — explicit definition and equivalence theorem
