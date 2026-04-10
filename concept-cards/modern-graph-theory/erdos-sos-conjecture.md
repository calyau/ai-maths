---
concept: "Erdős-Sós Conjecture"
slug: erdos-sos-conjecture
category: extremal-graph-theory
subcategory: open-problems
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.6 Simple Applications of Szemerédi's Lemma"
extraction_confidence: high
aliases:
  - "Erdős-Sós 1963"
prerequisites:
  - extremal-function
extends: []
related:
  - tree-embedding-via-regularity
contrasts_with: []
answers_questions:
  - "What is the Erdős-Sós conjecture?"
---

# Quick Definition
Every graph of order $n$ and more than $(k-1)n/2$ edges contains every tree with $k$ edges.

# Core Definition
The Erdős-Sós conjecture (1963): every graph of order $n$ and size $\lfloor(k-1)n/2\rfloor + 1$ contains every tree with $k$ edges (Bollobás, p. 153).

# Prerequisites
- **Extremal function** — The conjecture determines $ex(n; T)$ for trees

# Key Properties
1. Open as of 1998 (when the book was published)
2. Would generalize the path result (Theorem 3)
3. Related to the Komlós-Sárközy-Szemerédi theorem (Theorem 36)
4. The bound $(k-1)n/2$ matches the extremal function for $P_k$

# Context & Application
One of the "best known" conjectures in extremal graph theory (p. 153).

# Examples
**Example**: For $k = 2$ (trees = single edges), the conjecture says $e(G) > n/2$ guarantees any edge, which is trivially true.

# Relationships
## Related
- **tree-embedding-via-regularity** — Partial results

# Source Reference
Chapter IV, Section IV.6, page 153.

# Verification Notes
- Definition source: Direct from p. 153
- Confidence rationale: Explicitly stated as conjecture
- Uncertainties: Status as of publication (1998)
- Cross-reference status: Verified
