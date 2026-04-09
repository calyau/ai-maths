---
concept: Subnormal Series
slug: subnormal-series
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
  - "subinvariant series"
prerequisites:
  - normal-subgroup
  - factor-group
extends: []
related:
  - normal-series
  - composition-series
  - solvable-group
contrasts_with:
  - normal-series
answers_questions:
  - "What is a subnormal series?"
  - "How does a subnormal series differ from a normal series?"
---

# Quick Definition

A subnormal series of a group $G$ is a finite chain $G = H_n \supset H_{n-1} \supset \cdots \supset H_1 \supset H_0 = \{e\}$ where each $H_i$ is normal in $H_{i+1}$ (but not necessarily in $G$). The length is the number of proper inclusions.

# Core Definition

"A **subnormal series** of a group $G$ is a finite sequence of subgroups $G = H_n \supset H_{n-1} \supset \cdots \supset H_1 \supset H_0 = \{e\}$, where $H_i$ is a normal subgroup of $H_{i+1}$" (Judson, p. 175).

# Prerequisites

- **Normal subgroup** — Each $H_i \trianglelefteq H_{i+1}$
- **Factor group** — The factor groups $H_{i+1}/H_i$ describe the series

# Key Properties

1. Each $H_i$ is normal in $H_{i+1}$ (not necessarily in $G$)
2. The factor groups $H_{i+1}/H_i$ characterize the series
3. Two series are isomorphic if their factor groups can be put in one-to-one correspondence
4. A refinement of $\{H_i\}$ is a series $\{K_j\}$ with $\{H_i\} \subset \{K_j\}$

# Examples

**Example 1** (p. 176): $D_4 \supset \{(1), (12)(34), (13)(24), (14)(23)\} \supset \{(1), (12)(34)\} \supset \{(1)\}$ is a subnormal series that is NOT a normal series.

# Relationships

## Enables
- **Composition series** — A subnormal series with simple factors
- **Solvable group** — Defined via subnormal series with abelian factors

## Contrasts With
- **Normal series** — In a normal series, each $H_i$ is normal in $G$, not just in $H_{i+1}$

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 175.

# Verification Notes

- Definition source: Direct quote from p. 175
- Confidence: HIGH
