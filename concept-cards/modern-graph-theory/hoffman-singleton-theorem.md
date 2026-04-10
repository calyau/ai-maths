---
# === CORE IDENTIFICATION ===
concept: Hoffman-Singleton Theorem
slug: hoffman-singleton-theorem

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: existence-results
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 282
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Moore graph theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strongly-regular-graph
  - rationality-condition
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "For which degrees do Moore graphs of diameter 2 exist?"
---

# Quick Definition

A $k$-regular graph of order $k^2 + 1$ and diameter 2 exists only for $k = 2, 3, 7$, or possibly 57. For $k = 2$ it is the pentagon, for $k = 3$ the Petersen graph, and for $k = 7$ the Hoffman-Singleton graph.

# Core Definition

**Theorem 19** (Hoffman-Singleton, 1960; Bollobas, p. 282): If there is a $k$-regular graph $G$ of order $n = k^2 + 1$ and diameter 2, then $k = 2, 3, 7$ or 57. The proof uses the rationality condition for strongly regular graphs with parameters $(k, 0, 1)$: either $k = 2$ or $4k - 3$ is a perfect square $s^2$, and then $s | 15$, giving $s \in \{1, 3, 5, 15\}$, hence $k \in \{1, 3, 7, 57\}$.

# Prerequisites

- **Strongly regular graph** -- Moore graphs of diameter 2 are strongly regular with $(k, 0, 1)$
- **Rationality condition** -- The tool that restricts $k$

# Key Properties

1. $k = 2$: pentagon (unique)
2. $k = 3$: Petersen graph (unique)
3. $k = 7$: Hoffman-Singleton graph (unique)
4. $k = 57$: existence unknown (order 3250, a major open problem)
5. The proof is entirely algebraic, using the rationality condition

# Construction / Recognition

## Proof Outline
1. A $k$-regular graph of diameter 2 and order $k^2 + 1$ is strongly regular with parameters $(k, 0, 1)$
2. The rationality condition requires $4k - 3$ to be a perfect square $s^2$ (unless $k = 2$)
3. The multiplicity formula forces $s | 15$
4. So $s \in \{1, 3, 5, 15\}$, giving $k \in \{1, 3, 7, 57\}$

# Context & Application

The Hoffman-Singleton theorem is a celebrated result showing the power of algebraic methods in graph theory. The existence or nonexistence of a Moore graph of degree 57 remains one of the most famous open problems in algebraic graph theory.

# Examples

**Example** (p. 283): For $k = 2$, 3, and 7, the graphs are unique. The $k = 57$ case would have 3250 vertices.

# Relationships

## Builds Upon
- **Strongly regular graph** -- The algebraic framework
- **Rationality condition** -- The key constraint

## Enables
- Research on the $k = 57$ case

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Stating that Moore graphs of degree 57 do not exist
  **Correction**: The existence of a Moore graph of degree 57 is an open problem

# Common Confusions

- **Confusion**: Thinking the theorem applies to all Moore graphs
  **Clarification**: This is specifically for Moore graphs of diameter 2 (girth 5); other diameters have separate (and less complete) results

# Source Reference

Chapter VIII, Section VIII.3, Theorem 19, pages 282--283.

# Verification Notes

- Definition source: Direct from Theorem 19, p. 282
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
