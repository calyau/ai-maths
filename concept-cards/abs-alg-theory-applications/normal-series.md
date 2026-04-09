---
concept: Normal Series
slug: normal-series
category: group-structure
subcategory: series-of-subgroups
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 175
section: "Solvable Groups"
extraction_confidence: high
aliases:
  - "invariant series"
prerequisites:
  - normal-subgroup
  - subnormal-series
extends:
  - subnormal-series
related:
  - principal-series
  - composition-series
contrasts_with:
  - subnormal-series
answers_questions:
  - "What is a normal series?"
---

# Quick Definition

A normal series of $G$ is a subnormal series $G = H_n \supset \cdots \supset H_0 = \{e\}$ where each $H_i$ is normal in $G$ (not just in $H_{i+1}$). Every normal series is a subnormal series, but not conversely.

# Core Definition

"If each subgroup $H_i$ is normal in $G$, then the series is called a **normal series**" (Judson, p. 175).

# Prerequisites

- **Normal subgroup** — Each $H_i \trianglelefteq G$
- **Subnormal series** — A normal series is a special subnormal series

# Key Properties

1. Every $H_i$ is normal in $G$ (stronger than subnormal)
2. Any series of subgroups of an abelian group is a normal series
3. Every normal series is automatically a subnormal series

# Examples

**Example 1** (p. 175): $\mathbb{Z} \supset 9\mathbb{Z} \supset 45\mathbb{Z} \supset 180\mathbb{Z} \supset \{0\}$ is a normal series since every subgroup of $\mathbb{Z}$ is normal.

# Relationships

## Builds Upon
- **Subnormal series** — A normal series has a stronger condition

## Enables
- **Principal series** — A normal series with simple factors

## Contrasts With
- **Subnormal series** — Only requires normality in the next term

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 175.

# Verification Notes

- Definition source: Direct from p. 175
- Confidence: HIGH
