---
concept: Principal Series
slug: principal-series
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
aliases: []
prerequisites:
  - normal-series
  - simple-group
extends:
  - normal-series
related:
  - composition-series
contrasts_with:
  - composition-series
answers_questions:
  - "What is a principal series?"
---

# Quick Definition

A principal series of $G$ is a normal series where each factor group $H_{i+1}/H_i$ is simple. It differs from a composition series in that each $H_i$ must be normal in $G$ (not just in $H_{i+1}$).

# Core Definition

"A normal series $\{H_i\}$ of $G$ is a **principal series** if all the factor groups are simple" (Judson, p. 176).

# Prerequisites

- **Normal series** — Each $H_i$ is normal in $G$
- **Simple group** — Factor groups are simple

# Key Properties

1. Each $H_i \trianglelefteq G$ (stronger than composition series)
2. Each factor $H_{i+1}/H_i$ is simple
3. For abelian groups, composition series and principal series coincide

# Examples

**Example 1** (p. 176): Since $\mathbb{Z}_{60}$ is abelian, its composition series is automatically a principal series.

# Relationships

## Builds Upon
- **Normal series** — Adds simplicity of factors

## Contrasts With
- **Composition series** — In a composition series, $H_i$ need only be normal in $H_{i+1}$

# Source Reference

Chapter 13: The Structure of Groups, Section 13.2, p. 176.

# Verification Notes

- Definition source: Direct from p. 176
- Confidence: HIGH
