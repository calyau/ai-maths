---
concept: Small X-Separation
slug: small-x-separation
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 84
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "X-separation"
prerequisites:
  - k-linked-graph
  - separator
extends: []
related:
  - thomas-wollan-theorem
contrasts_with: []
answers_questions:
  - "What is a small X-separation?"
---

# Quick Definition
An X-separation (A, B) of G is a proper separation of order <= |X| with X in A. It is small if |A intersect B| < |X|, and linked if A intersect B is linked in G[B].

# Core Definition
Given k in N, G, and A, B, X subsets of V(G), call (A, B) an **X-separation** of G if {A, B} is a proper separation of order <= |X| and X is in A. An X-separation is **small** if |A intersect B| < |X|, and **linked** if A intersect B is linked in G[B] (Diestel, p. 84).

# Prerequisites
- **k-linked graph** — context of the definition
- **Separator** — A intersect B is the separator

# Key Properties
1. X-separation: {A, B} is a proper separation with X in A
2. Small: the separator A intersect B has fewer vertices than X
3. Linked: the separator can be linked in G[B]
4. Key concepts in the proof of Theorem 3.5.3 (Thomas-Wollan)
5. The proof shows that if G has no linked X-separation, then X is linked in G

# Context & Application
Small and linked X-separations are technical concepts in the proof of the Thomas-Wollan theorem. The proof proceeds by showing that either X is linked directly, or an X-separation can be found and handled inductively.

# Examples
**Example** (p. 84): In the proof of Theorem 3.5.3, linked X-separations are handled by induction, reducing to a smaller graph.

# Relationships
## Related
- **Thomas-Wollan theorem** — uses this concept in the proof
- **k-linked graph** — the property being proved

# Source Reference
Chapter 3, Section 3.5, p. 84 (pdf p. 84).

# Verification Notes
- Definition from p. 84
- Confidence: HIGH — explicitly defined
