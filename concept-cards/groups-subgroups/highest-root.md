---
concept: Highest Root
slug: highest-root
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 298
section: "Bases"
extraction_confidence: high
aliases:
  - "α̃"
prerequisites:
  - base-of-root-system
  - positive-root
extends: []
related:
  - simple-root
contrasts_with: []
answers_questions:
  - "What is the highest root?"
---

# Quick Definition

The highest root α̃ of an indecomposable root system (relative to a base S) is the unique positive root ∑ n_α α such that n_α ≥ m_α for every other positive root ∑ m_α α.

# Core Definition

Let S be a base for an indecomposable root system R. There exists a unique root α̃ = ∑_{α∈S} n_α α such that, for any other root ∑ m_α α, we have n_α ≥ m_α for all α. This is the **highest root** for the base S (Milne, Proposition 1.12, p. 299).

# Prerequisites

- **Base of root system** — The highest root depends on the choice of base
- **Positive root** — The highest root is the "largest" positive root

# Key Properties

1. The highest root is uniquely determined by the base
2. It exists only for indecomposable root systems
3. Simple roots α with n_α = 1 in α̃ are called special

# Examples

**Example 1** (p. 299): For A_n with base {α₁, ..., αₙ}, the highest root is α̃ = α₁ + ... + αₙ = e₁ − e_{n+1}.

# Source Reference

Chapter III, Section 1e, Proposition 1.12, page 299.

# Verification Notes

- Definition source: Direct from Proposition 1.12
- Confidence: HIGH
- Uncertainties: None
