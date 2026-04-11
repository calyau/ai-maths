---
concept: Morphism (Category Theory)
slug: morphism-category
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 911
section: "1. Categories and Functors"
extraction_confidence: high
aliases:
  - "arrow"
  - "endomorphism"
  - "isomorphism (in a category)"
prerequisites:
  - category
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a morphism in a category?"
---

# Quick Definition
A morphism f: A → B in a category is an element of Hom(A,B). Morphisms compose associatively and have identity morphisms. An isomorphism has a two-sided inverse.

# Core Definition
A **morphism** from A to B is an element of Hom_C(A,B), denoted f: A → B. A is the domain and B the codomain. An **endomorphism** is a morphism from A to A. A morphism f: A → B is an **isomorphism** if there exists g: B → A with gf = 1_A and fg = 1_B (p. 912). Morphisms are also called arrows.

# Prerequisites
- **category** — Morphisms exist within categories

# Source Reference
Appendix II, Section 1, Definition, page 912.

# Verification Notes
- Confidence: HIGH — explicit definition
