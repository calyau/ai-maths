---
# === CORE IDENTIFICATION ===
concept: Solvable Series
slug: solvable-series

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 89
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subnormal-series
extends:
  - subnormal-series
related:
  - solvable-group
  - derived-series
contrasts_with:
  - composition-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a solvable series?"
---

# Quick Definition

A solvable series is a subnormal series whose quotient groups are all commutative. A group is solvable if and only if it admits a solvable series.

# Core Definition

A subnormal series whose quotient groups are all commutative is called a *solvable series*.

(Milne, p. 89)

# Prerequisites

- **subnormal-series** -- a solvable series is a subnormal series with a condition on quotients

# Key Properties

1. The derived series (when it terminates at {1}) is the shortest solvable series
2. A solvable series can be refined to a composition series, whose quotients will all be cyclic of prime order
3. Any two solvable series can have different lengths, but the derived series is canonical and shortest

# Context & Application

The existence of a solvable series is the defining property of solvable groups. The derived series is the canonical choice, but other solvable series may be useful in specific contexts.

# Relationships

## Builds Upon
- **subnormal-series** -- adds the abelian quotients condition

## Enables
- **solvable-group** -- defined by having a solvable series

## Contrasts With
- **composition-series** -- has simple (not necessarily abelian) quotients

# Source Reference

Chapter 6, p. 89.

# Verification Notes

- Definition source: Direct from p. 89
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
