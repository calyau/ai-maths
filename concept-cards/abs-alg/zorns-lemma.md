---
concept: "Zorn's Lemma"
slug: zorns-lemma
category: foundations
subcategory: set-theory
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
  - "Zorn lemma"
prerequisites:
  - partial-order
  - chain
extends: []
related:
  - axiom-of-choice
  - well-ordering
  - maximal-element
contrasts_with: []
answers_questions:
  - "What is Zorn's Lemma?"
---

# Quick Definition
If A is a nonempty partially ordered set in which every chain has an upper bound, then A has a maximal element.

# Core Definition
**Zorn's Lemma**: If A is a nonempty partially ordered set in which every chain has an upper bound then A has a maximal element (p. 908). This is equivalent to the Axiom of Choice and the Well Ordering Principle (Theorem 2). It is independent of the Zermelo-Fraenkel axioms.

# Prerequisites
- **partial-order** — A is a partially ordered set
- **chain** — Every chain must have an upper bound

# Key Properties
1. Equivalent to Axiom of Choice and Well Ordering Principle
2. Independent of ZF set theory
3. Used to prove: every vector space has a basis, every proper ideal is contained in a maximal ideal, existence of algebraic closures

# Context & Application
Zorn's Lemma serves as a form of "infinite induction." In algebra it is used to prove the existence of maximal ideals, algebraic closures, bases for vector spaces, and other objects that are maximal with respect to certain properties (p. 907-908).

# Relationships
## Enables
- **maximal-element** — Zorn's Lemma guarantees existence of maximal elements

## Related
- **axiom-of-choice** — Equivalent (Theorem 2)
- **well-ordering** — Equivalent (Theorem 2)

# Source Reference
Appendix I, Section 2, Zorn's Lemma and Theorem 2, pages 908-909.

# Verification Notes
- Confidence: HIGH — explicitly stated with equivalences to AC and WOP
