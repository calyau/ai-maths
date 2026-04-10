---
concept: Odd Component
slug: odd-component
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.4 Tutte's 1-Factor Theorem"
extraction_confidence: high
aliases:
  - "q(H)"
  - "odd component count"
prerequisites:
  - graph-connectivity
extends: []
related:
  - tuttes-1-factor-theorem
contrasts_with: []
answers_questions:
  - "What role do odd components play in Tutte's theorem?"
---

# Quick Definition
An odd component of a graph $H$ is a connected component with an odd number of vertices. The number of odd components is denoted $q(H)$.

# Core Definition
A component $C$ of a graph $H$ is an odd component if $|C|$ is odd. The function $q(H)$ denotes the number of odd components of $H$, i.e., the number of components of odd order (Bollobás, p. 90).

# Prerequisites
- **Graph connectivity** — Components are maximal connected subgraphs

# Key Properties
1. $q(H)$ counts components with odd vertex count
2. If $G$ has a 1-factor, then $q(G-S) \le |S|$ for every $S \subset V(G)$
3. $q(G) \equiv |G| \pmod{2}$ (the number of odd components has the same parity as the order)

# Construction / Recognition
1. Find all connected components of $H$
2. Count those with odd order

# Context & Application
Odd components are the key obstruction to 1-factors. If removing a set $S$ creates more odd components than $|S|$, no 1-factor exists.

# Examples
**Example** (p. 90, Fig. III.6): $|S| = 4$ and $G - S$ has 2 odd components, satisfying $q(G-S) \le |S|$.

# Relationships
## Builds Upon
- **graph-connectivity** — Components of graphs

## Enables
- **tuttes-1-factor-theorem** — Uses $q(G-S)$

# Source Reference
Chapter III, Section III.4, page 90.

# Verification Notes
- Definition source: Direct from p. 90
- Confidence rationale: Explicitly defined with notation
- Uncertainties: None
- Cross-reference status: Verified
