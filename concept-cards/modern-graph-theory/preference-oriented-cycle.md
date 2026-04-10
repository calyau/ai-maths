---
concept: Preference-Oriented Cycle
slug: preference-oriented-cycle
category: matchings
subcategory: stable-matchings
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "Lemma 17"
prerequisites:
  - stable-matching
extends: []
related:
  - stable-matching-equal-cardinality
contrasts_with: []
answers_questions:
  - "What is the structure of the symmetric difference of two stable matchings?"
---

# Quick Definition
A cycle $aAbB \cdots zZ$ in a bipartite graph is preference-oriented if $A$ prefers $b$ to $a$, $b$ prefers $B$ to $A$, ..., and $Z$ prefers $a$ to $z$ — preferences alternate consistently around the cycle.

# Core Definition
A cycle is preference-oriented if it can be written as $aAbB \cdots zZ$ such that $A$ prefers $b$ to $a$, $b$ prefers $B$ to $A$, and so on cyclically. **Lemma 17**: If $M$ and $M'$ are two stable matchings, every component of $M \cup M'$ with at least three vertices is a preference-oriented cycle. In particular, if $aA, bB \in M$ and $aB \in M'$, then $a$ prefers $A$ to $B$ iff $B$ prefers $a$ to $b$ (Bollobás, p. 97).

# Prerequisites
- **Stable matching** — The symmetric difference structure

# Key Properties
1. Components of $M \cup M'$ (two stable matchings) are either single edges or preference-oriented cycles
2. No component is a path of length $\ge 2$ (contradicts stability)
3. Preferences alternate: one partner is better off in $M$, the other in $M'$

# Construction / Recognition
1. Compute $M \cup M'$ (symmetric difference)
2. Each component with $\ge 3$ vertices is a preference-oriented even cycle
3. Around the cycle, preferences alternate consistently

# Context & Application
This structural lemma is the key tool for proving that all stable matchings match the same vertices and that the $V_1$-optimal matching is $V_2$-pessimal.

# Examples
**Example** (p. 97): In a path $x_1x_2x_3x_4$ from $M \cup M'$, if $x_2$ prefers $x_3$ to $x_1$, stability forces $x_3$ to prefer $x_4$ to $x_2$, and this propagation prevents paths from being components.

# Relationships
## Builds Upon
- **stable-matching** — Concerns the structure of stable matchings

## Enables
- **stable-matching-equal-cardinality** — Theorem 18

# Source Reference
Chapter III, Section III.5, page 97. Lemma 17.

# Verification Notes
- Definition source: Direct from p. 97
- Confidence rationale: Explicitly defined and proved
- Uncertainties: None
- Cross-reference status: Verified
