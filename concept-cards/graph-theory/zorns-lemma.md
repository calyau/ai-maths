---
concept: "Zorn's Lemma"
slug: zorns-lemma

category: set-theory-foundations
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Sets"
chapter_number: null
pdf_page: 367
section: null

extraction_confidence: high

aliases: []

prerequisites:
  - partially-ordered-set
  - chain
extends: []
related:
  - axiom-of-choice
  - well-ordering-theorem
contrasts_with: []

answers_questions:
  - "What is Zorn's lemma?"
  - "When can we guarantee a maximal element?"
---

# Quick Definition
Zorn's Lemma states that if every chain in a partially ordered set X has an upper bound in X, then X contains at least one maximal element. It is equivalent to the axiom of choice.

# Core Definition
Zorn's Lemma: Let (X, <=) be a partially ordered set such that every chain in X has an upper bound in X. Then X contains at least one maximal element (Diestel, p. 360).

Note that in applications, the relation <= need not correspond to an intuitive notion of 'smaller than'. Applied to sets or graphs, it can stand for the superset relation just as much as for the subset relation.

# Prerequisites
- **Partially ordered set** — Zorn's lemma applies to posets
- **Chain** — the hypothesis concerns chains

# Key Properties
1. Equivalent to the axiom of choice
2. Equivalent to the well-ordering theorem
3. The upper bound condition is the key hypothesis
4. In applications, the ordering can be subset or superset

# Context & Application
Zorn's lemma is used throughout mathematics to prove existence of maximal objects. In graph theory, it is used to construct maximal trees, matchings, and other structures in infinite graphs.

# Relationships
## Builds Upon
- **partially-ordered-set**, **chain**

## Related
- **axiom-of-choice** — equivalent
- **well-ordering-theorem** — equivalent

# Source Reference
Appendix A: Infinite Sets, page 360 (pdf p. 370).

# Verification Notes
- Direct from p. 360
- Confidence: HIGH
