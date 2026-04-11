---
concept: Group Ring
slug: group-ring
category: representation-theory
subcategory: ring-structures
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Representation Theory and Character Theory"
chapter_number: 18
pdf_page: 840
section: "18.1 Linear Actions and Modules over Group Rings"
extraction_confidence: high
aliases:
  - "FG"
  - "group algebra"
prerequisites:
  - group
  - ring
  - vector-space
extends: []
related:
  - representation
  - fg-module
contrasts_with: []
answers_questions:
  - "What is the group ring FG?"
---

# Quick Definition
The group ring FG is the set of all formal sums Σα_g g (α_g ∈ F, g ∈ G) with componentwise addition and multiplication extending the group and field operations. FG is an F-algebra of dimension |G|.

# Core Definition
The **group ring** of G over F is the set of formal sums Σ_{g∈G} α_g g with α_g ∈ F, with componentwise addition and multiplication (αg)(βh) = (αβ)(gh) extended by distributivity (Definition, p. 840). FG is a vector space over F with G as a basis, so dim_F FG = |G|. FG is commutative iff G is abelian.

# Prerequisites
- **group** — G provides the basis elements
- **ring** — FG is a ring
- **vector-space** — FG is a vector space over F

# Key Properties
1. dim_F FG = |G|
2. F is contained in the center of FG
3. FG is commutative iff G is abelian
4. FG-modules ↔ representations of G
5. For cyclic G = ⟨g⟩ of order n: FG ≅ F[x]/(x^n - 1)

# Examples
**Example** (p. 842): For G = S_3 and F = Q, a typical element is 5(12) - 7(123) ∈ QS_3.

# Relationships
## Enables
- **representation** — Representations = FG-modules
- **fg-module** — Study of FG-module structure

# Source Reference
Chapter 18, Section 18.1, Definition and Examples, pages 840-843.

# Verification Notes
- Confidence: HIGH — explicit definition with worked examples
