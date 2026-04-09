---
concept: Tail of a Ray
slug: tail-of-a-ray
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 206
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "tail"
  - "subray"
prerequisites:
  - ray
extends:
  - ray
related:
  - end-of-a-graph
  - comb
contrasts_with: []
answers_questions:
  - "What is a tail of a ray?"
---

# Quick Definition
The tails of a ray are its subrays. Any two tails of the same ray differ only by a finite initial segment.

# Core Definition
The subrays of a ray or double ray are its *tails*. Formally, every ray has infinitely many tails, but any two of them differ only by a finite initial segment (Diestel, p. 206).

# Prerequisites
- **Ray** — Tails are subrays of a ray

# Key Properties
1. Every ray has infinitely many tails
2. Any two tails of the same ray differ only by a finite initial segment
3. Two rays are equivalent (belong to the same end) if and only if they have tails in the same component of G - S for every finite set S

# Construction / Recognition
## To Identify a Tail
1. Given a ray R = x_0x_1x_2..., a tail is any subray x_nx_{n+1}x_{n+2}... for some n

# Context & Application
Tails are used in the definition of ends: two rays are equivalent if for every finite vertex set S, both have a tail in the same component of G - S.

# Examples
**Example 1** (p. 206): For the ray x_0x_1x_2..., the subray x_5x_6x_7... is a tail.

# Relationships
## Builds Upon
- **Ray** — Tails are subrays of rays

## Enables
- **End of a graph** — Defined via the eventual behaviour captured by tails

# Source Reference
Chapter 8, Section 8.1, page 206.

# Verification Notes
- Definition directly from p. 206
- Confidence: HIGH — explicit definition
