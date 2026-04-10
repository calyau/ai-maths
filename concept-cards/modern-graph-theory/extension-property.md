---
# === CORE IDENTIFICATION ===
concept: Extension Property
slug: extension-property

# === CLASSIFICATION ===
category: random-graphs
subcategory: asymptotic-properties
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 234
section: "VII.2 Simple Properties of Almost All Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - extension axiom

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
  - almost-every-graph
extends: []
related:
  - first-order-properties-random-graphs
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What structural property do almost all graphs with fixed edge probability share?"
---

# Quick Definition

For fixed $p \in (0,1)$ and fixed $h \le k$, almost every $G_{n,p}$ has the property that for every sequence of $k$ vertices, there exists a vertex adjacent to the first $h$ and non-adjacent to the remaining $k - h$.

# Core Definition

**Theorem 5** (Bollobás, p. 235): Let $1 \le h \le k$ be fixed natural numbers and $0 < p < 1$ fixed. Then in $\mathcal{G}(n, p)$, a.e. graph $G_p$ is such that for every sequence of $k$ vertices $x_1, \ldots, x_k$ there exists a vertex $x$ with $xx_i \in E(G_p)$ if $1 \le i \le h$ and $xx_i \notin E(G_p)$ if $h < i \le k$.

# Prerequisites

- **G(n,p) model** -- The probability space
- **Almost every graph** -- The asymptotic framework

# Key Properties

1. Holds for fixed $p \in (0,1)$, not for $p = p(n) \to 0$
2. The probability that the property fails tends to 0 exponentially: $\varepsilon \le n^k(1-p^hq^{k-h})^{n-k} \to 0$
3. Implies Gaifman's result: every first-order sentence is either true for a.e. graph or false for a.e. graph

# Construction / Recognition

Not applicable -- this is an asymptotic property.

# Context & Application

This property is key because it implies that for fixed $p$, every first-order sentence about graphs has a 0-1 law: it is either true for almost every graph or false for almost every graph. Consequences include: a.e. graph has minimum degree at least $k$ (for any fixed $k$), a.e. graph has diameter 2, and any subgraph pattern extends to any larger pattern.

# Examples

**Example 1** (p. 236): For fixed $k$, a.e. $G_{n,p}$ has minimum degree at least $k$.

**Example 2** (p. 236): Almost every $G_{n,p}$ has diameter 2.

**Example 3** (p. 236): If $F \subset H$ and $F_0 \cong F$ is a subgraph of $G_{n,p}$, then a.e. graph has an $H_0 \cong H$ with $F_0 \subset H_0 \subset G_{n,p}$.

# Relationships

## Builds Upon
- **G(n,p) model** -- Fixed $p$ is essential
- **Almost every graph** -- Framework for the statement

## Enables
- **First-order properties of random graphs** -- 0-1 law follows

## Related
- **First-order properties of random graphs** -- Gaifman's theorem

## Contrasts With
- None

# Common Errors

- **Error**: Applying the extension property when $p$ depends on $n$
  **Correction**: The property requires fixed $p$; for $p \to 0$ or $p \to 1$, the extension property may fail

# Common Confusions

- **Confusion**: Thinking the extension property gives information about large-scale structure
  **Clarification**: As Bollobás notes, many interesting statements (chromatic number, connectivity) are not first-order sentences, so the extension property does not directly apply

# Source Reference

Chapter VII: Random Graphs, Section VII.2, Theorem 5, pages 234--236.

# Verification Notes

- Definition source: Direct from Theorem 5, p. 235
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
