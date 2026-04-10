---
concept: "Wagner's Theorem"
slug: wagners-theorem
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - planar-graph
  - graph-minor
  - complete-graph
  - complete-bipartite-graph
extends: []
related:
  - kuratowskis-theorem
contrasts_with: []
answers_questions:
  - "What is Wagner's theorem?"
---

# Quick Definition

Wagner's theorem (1937) states that a graph is planar iff it contains neither $K_5$ nor $K_{3,3}$ as a minor.

# Core Definition

"**Theorem 18.** A graph is planar iff it contains neither $K_5$ nor $K_{3,3}$ as a minor" (Bollobás, p. 33). This is equivalent to Kuratowski's theorem.

# Prerequisites

- **Planar graph** — The property being characterized
- **Graph minor** — The theorem uses the minor relation
- **Complete graph** — $K_5$ is a forbidden minor
- **Complete bipartite graph** — $K_{3,3}$ is a forbidden minor

# Key Properties

1. Equivalent to Kuratowski's theorem (Theorem 17)
2. $G \supset TH$ implies $G \succ H$
3. If $H$ has max degree $\le 3$, $G \supset TH \iff G \succ H$; so $G \supset TK_{3,3} \iff G \succ K_{3,3}$
4. If $G \succ K_5$ then $G \supset TK_5$ or $G \supset TK_{3,3}$

# Construction / Recognition

Same practical effect as Kuratowski's theorem: test for $K_5$ and $K_{3,3}$ minors.

# Context & Application

Wagner's formulation inspired the Robertson-Seymour graph minor theorem, one of the deepest results in graph theory, proving that every minor-closed property has finitely many forbidden minors.

# Examples

**Example** (p. 33): The equivalence with Kuratowski's theorem follows from the relationships between subdivisions and minors for small-degree graphs.

# Relationships

## Builds Upon
- **Planar graph**, **Graph minor**, **Complete graph**, **Complete bipartite graph**

## Enables
- Graph minor theory (Robertson-Seymour)

## Related
- **Kuratowski's theorem** — Equivalent formulation using subdivisions

# Common Errors

- **Error**: Thinking Wagner's theorem and Kuratowski's theorem give different information
  **Correction**: They are logically equivalent; they differ only in formulation

# Common Confusions

- **Confusion**: Thinking "minor" and "subdivision" always coincide
  **Clarification**: They coincide for graphs of max degree $\le 3$, but differ in general

# Source Reference

Chapter I: Fundamentals, Section I.4, Theorem 18, page 33.

# Verification Notes

- Definition source: Direct theorem statement from p. 33
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
