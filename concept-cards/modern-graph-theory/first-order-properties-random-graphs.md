---
# === CORE IDENTIFICATION ===
concept: First-Order Properties of Random Graphs
slug: first-order-properties-random-graphs

# === CLASSIFICATION ===
category: random-graphs
subcategory: logical-properties
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 236
section: "VII.2 Simple Properties of Almost All Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - zero-one law for random graphs
  - Gaifman's theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-property
  - almost-every-graph
extends: []
related:
  - gnp-model
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does every first-order sentence about graphs have a zero-one law?"
---

# Quick Definition

For fixed $p \in (0,1)$, every first-order sentence about graphs is either true for almost every $G_{n,p}$ or false for almost every $G_{n,p}$ (Gaifman's zero-one law), as a consequence of the extension property (Theorem 5).

# Core Definition

By Gaifman's result, the extension property (Theorem 5) implies that for fixed $0 < p < 1$, every first-order sentence about graphs is either true for a.e. graph in $\mathcal{G}(n,p)$ or false for a.e. graph. This means that any property expressible in first-order logic has probability converging to 0 or 1. However, many important graph properties (chromatic number, connectivity) are not first-order expressible (Bollobas, p. 236).

# Prerequisites

- **Extension property** -- The structural property that implies the zero-one law
- **Almost every graph** -- The framework for the statement

# Key Properties

1. Applies to fixed $p \in (0,1)$, not to $p$ depending on $n$
2. Every first-order sentence has a limiting probability of 0 or 1
3. Properties like "minimum degree $\ge k$" and "diameter $= 2$" are immediate corollaries
4. Properties like "$\chi(G) \le k$" or "connected" are NOT first-order

# Construction / Recognition

Not applicable -- this is a logical/asymptotic result.

# Context & Application

The zero-one law shows that random graphs with fixed edge probability have highly predictable first-order properties. However, the most interesting graph properties (chromatic number, connectivity, Hamiltonicity) are not first-order, so the zero-one law does not apply to them.

# Examples

**Example** (p. 236): For fixed $k$ and fixed $p$: a.e. $G_{n,p}$ has minimum degree $\ge k$ (first-order). But "$\chi(G) \le n^{1/2}$" is not first-order.

# Relationships

## Builds Upon
- **Extension property** -- The structural basis
- **Almost every graph** -- Framework

## Enables
- Quick deduction of many a.e. properties

## Related
- **G(n,p) model** -- The setting

## Contrasts With
- None

# Common Errors

- **Error**: Applying the zero-one law to non-first-order properties
  **Correction**: Properties involving quantification over large sets (connectivity, Hamiltonicity, chromatic number) are typically not first-order

# Common Confusions

- **Confusion**: Thinking the zero-one law is stronger than the extension property
  **Clarification**: Bollobas notes the zero-one law is actually weaker: given any first-order sentence, Theorem 5 directly determines its truth value for a.e. graph

# Source Reference

Chapter VII, Section VII.2, page 236.

# Verification Notes

- Definition source: Synthesized from p. 236 discussion
- Confidence rationale: Clear statement referencing Gaifman
- Uncertainties: None
- Cross-reference status: Verified
