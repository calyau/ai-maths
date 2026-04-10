---
concept: Randomly Eulerian Graph
slug: randomly-eulerian-graph
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: medium
aliases: []
prerequisites:
  - eulerian-graph
  - euler-circuit
extends:
  - eulerian-graph
related: []
contrasts_with: []
answers_questions:
  - "What is a randomly Eulerian graph?"
---

# Quick Definition

A graph is randomly Eulerian from a vertex $x$ if any walk from $x$ that avoids repeating edges and continues until no new edges are available will necessarily traverse all edges — i.e., any greedy strategy produces an Euler circuit from $x$.

# Core Definition

"The graph of such an exhibition is said to be randomly Eulerian from the vertex corresponding to the entrance (which is also the exit)" (Bollobás, p. 28). A visitor who avoids retracing edges and continues until stuck will see all exhibits (traverse all edges). See Fig. I.17 for examples.

# Prerequisites

- **Eulerian graph** — A randomly Eulerian graph must be Eulerian
- **Euler circuit** — The greedy strategy produces an Euler circuit

# Key Properties

1. Any greedy traversal from $x$ (avoiding repeated edges) produces an Euler circuit
2. Not all Eulerian graphs are randomly Eulerian from every vertex
3. Randomly Eulerian graphs are characterized in Exercises 50-52

# Construction / Recognition

Recognition criteria are developed in the exercises (50-52). The condition is more restrictive than being Eulerian.

# Context & Application

This concept models "well-designed exhibitions" where a visitor cannot get stuck in a dead end as long as they don't retrace their steps.

# Examples

**Example** (p. 28): Fig. I.17 shows three examples: $G$ is randomly Eulerian from $x$; $H$ is randomly Eulerian from both $u$ and $v$; multigraph $M$ is randomly Eulerian from $w$.

# Relationships

## Builds Upon
- **Eulerian graph** — Must be Eulerian to be randomly Eulerian

# Common Errors

- **Error**: Assuming all Eulerian graphs are randomly Eulerian
  **Correction**: Many Eulerian graphs have vertices from which a greedy traversal can get stuck

# Common Confusions

- **Confusion**: Thinking "randomly Eulerian" means "a random walk gives an Euler circuit"
  **Clarification**: It means any non-backtracking greedy walk from the given vertex succeeds

# Source Reference

Chapter I: Fundamentals, Section I.3, page 28; Fig. I.17.

# Verification Notes

- Definition source: Descriptive from p. 28; formal characterization in exercises
- Confidence rationale: Medium — the concept is described but formal characterization is deferred to exercises
- Uncertainties: Exact characterization not given in the main text
- Cross-reference status: Verified
