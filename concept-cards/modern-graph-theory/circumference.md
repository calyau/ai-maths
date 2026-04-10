---
concept: Circumference
slug: circumference
category: extremal-graph-theory
subcategory: cycle-parameters
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.1 Paths and Cycles"
extraction_confidence: high
aliases:
  - "maximum cycle length"
prerequisites: []
extends: []
related:
  - girth
  - hamilton-cycle
contrasts_with:
  - girth
answers_questions:
  - "What is the circumference of a graph?"
---

# Quick Definition
The circumference of a graph is the length of a longest cycle.

# Core Definition
The circumference is the maximal length of a cycle in $G$ (Bollobás, p. 112). If $G$ is Hamiltonian, its circumference is $n = |G|$.

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. If $G$ is Hamiltonian, circumference $= n$
2. Every non-Hamiltonian connected graph contains a path at least as long as its circumference
3. Theorem 2 gives lower bounds on circumference from degree conditions

# Construction / Recognition
1. Find a longest cycle in $G$
2. Its length is the circumference

# Context & Application
Circumference bounds are central to the study of Hamilton cycles and long paths/cycles in graphs with degree conditions.

# Examples
**Example** (p. 114): If $d(x) + d(y) \ge k$ for nonadjacent $x, y$ in a connected graph of order $n \ge 3$ with $k < n$, then the circumference is at least $(k+2)/2$.

# Relationships
## Related
- **hamilton-cycle** — A Hamilton cycle gives circumference $= n$
- **girth** — The minimum cycle length

## Contrasts With
- **girth** — Shortest vs. longest cycle

# Source Reference
Chapter IV, Section IV.1, page 112.

# Verification Notes
- Definition source: Direct from p. 112
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
