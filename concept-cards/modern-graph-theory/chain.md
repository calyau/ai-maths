---
concept: Chain
slug: chain
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
  - "tower"
  - "totally ordered subset"
prerequisites:
  - partial-order
extends: []
related:
  - antichain
  - dilworths-theorem
contrasts_with:
  - antichain
answers_questions:
  - "What is a chain in a partially ordered set?"
---

# Quick Definition
A chain in a partially ordered set is a subset in which every two elements are comparable ($x \le y$ or $y < x$).

# Core Definition
A subset $C$ of a partially ordered set $P$ is a chain (or tower) if for $x, y \in C$ either $x \le y$ or $y < x$ (Bollobás, p. 89).

# Prerequisites
- **Partial order** — Chains are defined within posets

# Key Properties
1. Every two elements are comparable
2. No two elements of an antichain can be in the same chain
3. Dilworth: minimum chains to cover $P$ equals maximum antichain size

# Context & Application
Chains and antichains are dual objects in Dilworth's theorem.

# Examples
**Example** (p. 89, Fig. III.5): In the Hasse diagram, a chain is a path going consistently upward.

# Relationships
## Builds Upon
- **partial-order** — Chains exist in posets

## Contrasts With
- **antichain** — No two elements comparable

# Source Reference
Chapter III, Section III.3, page 89.

# Verification Notes
- Definition source: Direct from p. 89
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
