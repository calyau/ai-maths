---
concept: Bad Set
slug: bad-set
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 50
section: "2.2 Matching in general graphs"
extraction_confidence: high
aliases: []
prerequisites:
  - tuttes-condition
  - odd-component
extends: []
related:
  - tuttes-theorem
contrasts_with: []
answers_questions:
  - "What is a bad set in Tutte's theorem?"
---

# Quick Definition
A bad set S is a vertex set that violates Tutte's condition: q(G-S) > |S|.

# Core Definition
A vertex set S is called a **bad set** if it violates Tutte's condition, i.e., q(G-S) > |S|, where q counts odd components (Diestel, p. 50).

# Prerequisites
- **Tutte's condition** — a bad set violates it
- **Odd component** — used in the definition

# Key Properties
1. A bad set witnesses the non-existence of a 1-factor
2. If no bad set exists, the graph has a 1-factor (Tutte's theorem)
3. In the proof, G is assumed edge-maximal without a 1-factor, and a bad set S is constructed
4. In the edge-maximal case, all components of G-S are complete and S is adjacent to everything

# Context & Application
Bad sets are the certificates for non-existence of 1-factors. Finding a bad set proves that a graph has no perfect matching.

# Examples
**Example** (p. 50): In a graph without a 1-factor, the proof of Tutte's theorem constructs a bad set S satisfying (*): all components of G-S are complete and every s in S is adjacent to all of G-s.

# Relationships
## Builds Upon
- **Tutte's condition**, **odd component**

## Related
- **Tutte's theorem** — characterizes when no bad set exists

# Source Reference
Chapter 2, Section 2.2, p. 50 (pdf p. 50).

# Verification Notes
- From the proof of Theorem 2.2.1
- Confidence: HIGH — explicitly named
