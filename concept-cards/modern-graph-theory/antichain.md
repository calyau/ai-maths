---
concept: Antichain
slug: antichain
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
aliases: []
prerequisites:
  - partial-order
extends: []
related:
  - chain
  - dilworths-theorem
contrasts_with:
  - chain
answers_questions:
  - "What is an antichain in a partially ordered set?"
---

# Quick Definition
An antichain in a partially ordered set is a subset where no two elements are comparable ($x < y$ implies $\{x,y\} \not\subset A$).

# Core Definition
A set $A \subset P$ is an antichain if $x < y$ implies that $\{x, y\} \not\subset A$ (Bollobás, p. 89).

# Prerequisites
- **Partial order** — Antichains are defined within posets

# Key Properties
1. No element in the antichain is above or below another
2. Maximum antichain size determines minimum chain decomposition (Dilworth)

# Context & Application
The maximum antichain size is the key invariant in Dilworth's theorem.

# Examples
**Example** (p. 89, Fig. III.5): A maximal antichain is highlighted in the Hasse diagram.

# Relationships
## Builds Upon
- **partial-order** — Antichains exist in posets

## Contrasts With
- **chain** — Totally ordered vs. totally incomparable

# Source Reference
Chapter III, Section III.3, page 89.

# Verification Notes
- Definition source: Direct from p. 89
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
