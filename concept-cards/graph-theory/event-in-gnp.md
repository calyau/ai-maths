---
concept: Event in G(n,p)
slug: event-in-gnp
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 305
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Event in G(n,p)?"
---

# Quick Definition
An event in G(n,p) is any set of graphs on V. The event A_e that edge e is present has probability p. Events A_e are independent (Proposition 11.1.1).

# Core Definition
Any set of graphs on V is an *event* in G(n,p). The event A_e = {omega | omega(e) = 1_e} that edge e is in G has probability p. These events are independent: P(A_{e1} cap ... cap A_{ek}) = p^k (Proposition 11.1.1, Diestel, pp. 305-306).

# Source Reference
Chapter 11, Section 11.1 The notion of a random graph, page 305.

# Verification Notes
- Extracted from source
- Confidence: HIGH
