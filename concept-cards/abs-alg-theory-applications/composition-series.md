---
concept: Composition Series
slug: composition-series
category: group-structure
subcategory: series-of-subgroups
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Structure of Groups"
chapter_number: 13
pdf_page: 176
section: "Solvable Groups"
extraction_confidence: high
aliases:
  - "composition factors"
prerequisites:
  - subnormal-series
  - simple-group
extends:
  - subnormal-series
related:
  - jordan-holder-theorem
  - principal-series
  - solvable-group
contrasts_with:
  - principal-series
answers_questions:
  - "What is a composition series?"
  - "How do composition series relate to simple groups?"
---

# Quick Definition

A composition series of $G$ is a subnormal series $G = H_n \supset \cdots \supset H_0 = \{e\}$ where all factor groups $H_{i+1}/H_i$ are simple. The factors are called composition factors.

# Core Definition

"A subnormal series $\{H_i\}$ of a group $G$ is a **composition series** if all the factor groups are simple; that is, if none of the factor groups of the series contains a normal subgroup" (Judson, p. 176).

# Prerequisites

- **Subnormal series** — A composition series is a special subnormal series
- **Simple group** — The factor groups must be simple

# Key Properties

1. Factor groups $H_{i+1}/H_i$ are all simple
2. Composition series need not be unique (Example: $\mathbb{Z}_{60}$ has multiple)
3. Any two composition series of $G$ are isomorphic (Jordan-Holder Theorem)
4. Not every group has a composition series ($\mathbb{Z}$ does not)
5. Composition factors are the "building blocks" of the group

# Examples

**Example 1** (p. 176): $\mathbb{Z}_{60} \supset \langle 3 \rangle \supset \langle 15 \rangle \supset \langle 30 \rangle \supset \{0\}$ with factors $\mathbb{Z}_3, \mathbb{Z}_5, \mathbb{Z}_2, \mathbb{Z}_2$.

**Example 2** (p. 177): For $n \geq 5$, $S_n \supset A_n \supset \{(1)\}$ is a composition series since $S_n/A_n \cong \mathbb{Z}_2$ and $A_n$ is simple.

**Example 3** (p. 177): $\mathbb{Z}$ does NOT have a composition series because any initial factor $k\mathbb{Z}/\{0\} \cong k\mathbb{Z}$ has nontrivial normal subgroups.

# Relationships

## Builds Upon
- **Subnormal series** — Composition series is a subnormal series with simple factors
- **Simple group** — Factors must be simple

## Enables
- **Jordan-Holder theorem** — Any two composition series are isomorphic

## Related
- **Solvable group** — Has a subnormal series with abelian factors

## Contrasts With
- **Principal series** — Uses normal series (each $H_i$ normal in $G$) with simple factors

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 176-177. Examples 13.15-13.17.

# Verification Notes

- Definition source: Direct from p. 176
- Confidence: HIGH
