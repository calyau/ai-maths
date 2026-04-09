---
concept: "Haj\u00F3s's Conjecture"
slug: hajos-conjecture
category: extremal-graph-theory
subcategory: minors
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 185
section: "7.3 Hadwiger's conjecture"
extraction_confidence: high
aliases:
  - "Hajos conjecture"
prerequisites:
  - hadwiger-conjecture
contrasts_with:
  - hadwiger-conjecture
related:
  - girth-forcing-minors
answers_questions:
  - "What is Hajos's conjecture and how does it differ from Hadwiger's?"
---

# Quick Definition
Hajos's conjecture asserts that chi(G) >= r implies G contains TK^r (a topological K^r minor). It is FALSE in general, but true for graphs of large girth.

# Core Definition
The strengthening of Hadwiger's conjecture that graphs of chromatic number at least r contain K^r as a *topological* minor is known as **Hajos's conjecture**. It is false in general (counterexample by Catlin, 1979; Erdos and Fajtlowicz showed it fails for "almost all" graphs). However, Theorem 7.2.5 implies it holds for graphs of large girth (Corollary 7.3.9). (Diestel, p. 176)

# Prerequisites
- **Hadwiger's conjecture** — Hajos is the topological-minor strengthening

# Key Properties
1. Stronger than Hadwiger's conjecture: TK^r instead of K^r minor
2. FALSE in general (counterexamples known since 1979)
3. True for graphs of sufficiently large girth (Corollary 7.3.9)

# Relationships
## Contrasts With
- **Hadwiger's conjecture** — Hadwiger asks for general minors (true for r <= 6); Hajos asks for topological minors (false in general)

# Source Reference
Chapter 7, Section 7.3, page 176 (pdf page 185). Corollary 7.3.9.

# Verification Notes
- Confidence: HIGH — explicitly stated with known counterexamples
