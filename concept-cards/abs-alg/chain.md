---
concept: Chain
slug: chain
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
  - "tower"
  - "totally ordered subset"
prerequisites:
  - partial-order
extends: []
related:
  - zorns-lemma
contrasts_with: []
answers_questions:
  - "What is a chain in a partially ordered set?"
---

# Quick Definition
A chain in a partially ordered set is a subset in which every pair of elements is comparable. Also called a tower or totally ordered subset.

# Core Definition
A subset B of a partially ordered set A is called a **chain** if for all x,y ∈ B, either x ≤ y or y ≤ x (Definition, p. 908). Also called a tower, totally ordered, linearly ordered, or simply ordered subset.

# Prerequisites
- **partial-order** — Chains live in posets

# Key Properties
1. Every subset of a chain is a chain
2. Chains are the key hypothesis in Zorn's Lemma

# Source Reference
Appendix I, Section 2, Definition, page 908.

# Verification Notes
- Confidence: HIGH — standard definition
