---
concept: Forgetful Functor
slug: forgetful-functor
category: category-theory
subcategory: basic-concepts
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Appendix II: Category Theory"
chapter_number: null
pdf_page: 914
section: "1. Categories and Functors"
extraction_confidence: high
aliases: []
prerequisites:
  - functor
extends: []
related:
  - category
contrasts_with: []
answers_questions:
  - "What is a forgetful functor?"
---

# Quick Definition
The forgetful functor maps a structured category (like Grp or R-mod) to Set by "forgetting" the algebraic structure, sending each object to its underlying set and each homomorphism to the underlying function.

# Core Definition
The **forgetful functor** from Grp to Set sends each group G to the same set G, and each group homomorphism φ to the same set map φ (Example 2, p. 914). Similarly there are forgetful functors from Ab, R-mod, Top, etc. to Set. The forgetful functor is faithful but not full.

# Prerequisites
- **functor** — The forgetful functor is a specific functor

# Source Reference
Appendix II, Section 1, Example 2, page 914.

# Verification Notes
- Confidence: HIGH — standard example
