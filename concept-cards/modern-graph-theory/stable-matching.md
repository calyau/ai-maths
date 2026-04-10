---
concept: Stable Matching
slug: stable-matching
category: matchings
subcategory: stable-matchings
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.5 Stable Matchings"
extraction_confidence: high
aliases:
  - "stable marriage"
prerequisites:
  - matching
extends:
  - matching
related:
  - gale-shapley-algorithm
  - optimal-stable-matching
  - preference-oriented-cycle
contrasts_with:
  - maximum-matching
answers_questions:
  - "What is a stable matching?"
---

# Quick Definition
A stable matching in a bipartite graph with preferences is a matching $M$ where no unmatched pair $(a, B)$ would both prefer each other to their current partners (or singlehood).

# Core Definition
Given a bipartite graph $G = G_2(n,m)$ where each boy orders his known girls by preference and each girl orders her known boys, a stable matching $M$ is a set of independent edges such that if $aB \in E(G) - M$, then either $aA \in M$ for some girl $A$ preferred to $B$ by $a$, or $bB \in M$ for some boy $b$ preferred to $a$ by $B$ (Bollobás, p. 94).

# Prerequisites
- **Matching** — A stable matching is a matching with additional conditions

# Key Properties
1. Every stable matching is a maximal matching (cannot be enlarged)
2. A stable matching need not be a maximum matching (maximum cardinality)
3. All stable matchings have the same cardinality (Theorem 18)
4. All stable matchings are incident with the same set of vertices (Theorem 18)
5. A stable matching always exists (Theorem 16)

# Construction / Recognition
1. Check that $M$ is a matching (independent edges)
2. For each edge $aB \notin M$: verify either $a$ has a preferred partner in $M$, or $B$ has a preferred partner in $M$
3. If all such pairs are "blocked," $M$ is stable

# Context & Application
Stable matchings model real-world assignment problems (college admissions, organ donation matching, residency matching) where participants have preferences and an unstable assignment would be undermined by "blocking pairs."

# Examples
**Example** (p. 94, Fig. III.8): If $a$ prefers $B$ to $A$ and $B$ prefers $a$ to $b$, then $M = \{aB\}$ is the only stable matching.

# Relationships
## Builds Upon
- **matching** — A stable matching is a specialized matching

## Enables
- **gale-shapley-algorithm** — Constructs stable matchings
- **optimal-stable-matching** — Best stable matching for one side

## Contrasts With
- **maximum-matching** — A maximum matching maximizes cardinality; a stable matching satisfies preference conditions

# Common Errors
- **Error**: Assuming a stable matching must cover all vertices
  **Correction**: A stable matching need not be complete; it need only be maximal

# Common Confusions
- **Confusion**: Thinking stability means the matching cannot be improved
  **Clarification**: Stability means no *pair* of agents would both benefit from deviating; it does not optimize a global objective

# Source Reference
Chapter III, Section III.5, pages 93-95.

# Verification Notes
- Definition source: Direct from p. 94
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
