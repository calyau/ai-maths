---
concept: Partial Order
slug: partial-order
category: matchings
subcategory: order-theory
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "partially ordered set"
  - "poset"
prerequisites: []
extends: []
related:
  - chain
  - antichain
  - dilworths-theorem
contrasts_with: []
answers_questions:
  - "What is a partial order?"
---

# Quick Definition
A partial order on a set is a transitive and irreflexive relation. A set with a partial order is a partially ordered set (poset).

# Core Definition
A partial order $<$ on a set is a transitive and irreflexive relation defined on some ordered pairs of elements. Thus if $x < y$ and $y < z$ then $x < z$, but $x < y$ and $y < x$ cannot both hold. A set with a partial order is a partially ordered set (Bollobás, p. 89).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Transitive: $x < y, y < z \Rightarrow x < z$
2. Irreflexive: $x \not< x$
3. Antisymmetric: $x < y$ and $y < x$ cannot both hold
4. $x \le y$ means $x = y$ or $x < y$

# Context & Application
Partially ordered sets are the setting for Dilworth's theorem (Theorem 13).

# Examples
**Example** (p. 89, Fig. III.5): A partially ordered set with a maximal antichain is shown via a Hasse diagram.

# Relationships
## Enables
- **chain** — Totally ordered subsets
- **antichain** — Incomparable subsets
- **dilworths-theorem** — Chain decomposition

# Source Reference
Chapter III, Section III.3, page 89.

# Verification Notes
- Definition source: Direct from p. 89
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
