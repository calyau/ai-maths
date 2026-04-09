---
concept: Linkedness Theorem
slug: linkedness-theorem
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 80
section: "3.5 Linking pairs of vertices"
extraction_confidence: high
aliases:
  - "Jung 1970"
  - "Larman & Mani 1970"
  - "linkage theorem"
prerequisites:
  - k-linked-graph
  - mengers-theorem
extends: []
related:
  - thomas-wollan-theorem
contrasts_with: []
answers_questions:
  - "How connected must a graph be to be k-linked?"
---

# Quick Definition
There exists a function f: N -> N such that every f(k)-connected graph is k-linked.

# Core Definition
**Theorem 3.5.2 (Jung 1970; Larman & Mani 1970).** There is a function f: N -> N such that every f(k)-connected graph is k-linked, for all k in N (Diestel, p. 80).

# Prerequisites
- **k-linked graph** — the property being forced
- **Menger's theorem** — used in the proof to link vertices to branch vertices

# Key Properties
1. Proved for f(k) = h(3k) + 2k, where h is from Lemma 3.5.1
2. The proof finds TK^{3k} in G, then uses Menger to link prescribed vertices to branch vertices
3. The function f is exponential in this proof
4. Can be improved to linear: f(k) = 10k suffices (Theorem 3.5.3 with epsilon condition)

# Construction / Recognition
## Proof Strategy
1. G is f(k)-connected, so d(G) >= h(3k) and G contains TK^{3k}
2. Let U be the 3k branch vertices
3. Given s1,...,sk, t1,...,tk, use Menger to find 2k disjoint paths to U
4. Route through the subdivided edges of TK^{3k} to pair up as desired

# Context & Application
This theorem shows that high connectivity forces the strong property of k-linkedness. The initial exponential bound was later improved to linear by Thomas and Wollan.

# Examples
**Example** (p. 81): The proof constructs paths P1,...,Pk, Q1,...,Qk from si and ti to branch vertices of TK^{3k}, then routes through the subdivision.

# Relationships
## Builds Upon
- **k-linked graph**, **Menger's theorem**

## Related
- **Thomas-Wollan theorem** — gives the linear bound

# Source Reference
Chapter 3, Section 3.5, Theorem 3.5.2, pp. 80-81 (pdf pp. 80-81).

# Verification Notes
- Theorem from p. 80
- Confidence: HIGH — named theorem with proof
