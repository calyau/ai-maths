---
concept: Maximal Element
slug: maximal-element
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
aliases: []
prerequisites:
  - partial-order
extends: []
related:
  - zorns-lemma
contrasts_with: []
answers_questions:
  - "What is a maximal element in a partially ordered set?"
---

# Quick Definition
A maximal element m of a partially ordered set A is an element such that m ≤ x implies m = x. A maximal element need not be a maximum (greatest) element.

# Core Definition
A **maximal element** of A is an element m ∈ A such that if m ≤ x for any x ∈ A, then m = x (Definition, p. 908). Note: m is maximal does NOT mean x ≤ m for all x — that would be a maximum element.

# Prerequisites
- **partial-order** — Defined in partially ordered sets

# Key Properties
1. A maximal element is NOT necessarily a maximum
2. There may be multiple maximal elements
3. Zorn's Lemma guarantees existence under chain conditions

# Source Reference
Appendix I, Section 2, Definition, page 908.

# Verification Notes
- Confidence: HIGH — explicit definition with distinction from maximum
