---
# === CORE IDENTIFICATION ===
concept: Degree Sequence Tree Count
slug: degree-sequence-tree-count

# === CLASSIFICATION ===
category: graph-enumeration
subcategory: tree-enumeration
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 284
section: "VIII.4 Enumeration and Pólya's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - prufer-code
  - cayley-formula-trees
extends:
  - cayley-formula-trees
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many labelled trees have a given degree sequence?"
---

# Quick Definition

The number of labelled trees of order $n$ with degree sequence $(d_1, \ldots, d_n)$ is the multinomial coefficient $\binom{n-2}{d_1-1, d_2-1, \ldots, d_n-1}$.

# Core Definition

**Corollary 21** (Bollobas, p. 284): Let $d_1 \le d_2 \le \cdots \le d_n$ be the degree sequence of a tree ($d_i \ge 1$, $\sum d_i = 2n-2$). The number of labelled trees with this degree sequence is $\binom{n-2}{d_1-1, d_2-1, \ldots, d_n-1}$. This follows from the Prufer code: vertex $i$ appears $d_i - 1$ times in the code.

# Prerequisites

- **Prufer code** -- The encoding that proves the result
- **Cayley's formula for trees** -- The total count

# Key Properties

1. A vertex of degree $d$ appears $d-1$ times in the Prufer code
2. The total $\sum(d_i - 1) = 2n - 2 - n = n - 2$ matches the code length
3. Summing over all valid degree sequences recovers $n^{n-2}$

# Construction / Recognition

Not applicable -- this is a counting formula.

# Context & Application

This refines Cayley's formula by partitioning the count according to degree sequence. It is useful in analyzing random trees and in combinatorial probability.

# Examples

**Example**: Trees on 4 vertices with degree sequence $(1, 1, 1, 3)$: $\binom{2}{0, 0, 0, 2} = 1$. With degree sequence $(1, 1, 2, 2)$: $\binom{2}{0, 0, 1, 1} = 2$. With degree sequence $(1, 2, 2, 1)$: same = 2. Total paths = 3 (labeled). Total stars = 4. Grand total = $4^2 = 16$.

# Relationships

## Builds Upon
- **Prufer code** -- The proof tool
- **Cayley's formula for trees** -- The total count

## Enables
- Random tree degree distribution analysis

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Forgetting the $d_i - 1$ shift in the multinomial
  **Correction**: The multinomial uses $d_i - 1$, not $d_i$, since each vertex appears $d_i - 1$ times in the code

# Common Confusions

- **Confusion**: Thinking this counts unlabelled trees
  **Clarification**: This counts labelled trees with a specific degree sequence

# Source Reference

Chapter VIII, Section VIII.4, Corollary 21, page 284.

# Verification Notes

- Definition source: Direct from Corollary 21
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified
