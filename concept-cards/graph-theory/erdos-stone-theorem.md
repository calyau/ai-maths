---
concept: "Erd\u0151s-Stone Theorem"
slug: erdos-stone-theorem
category: extremal-graph-theory
subcategory: subgraph-density
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Extremal Graph Theory"
chapter_number: 7
pdf_page: 177
section: "7.1 Subgraphs"
extraction_confidence: high
aliases:
  - "Erdos-Stone theorem"
  - "Theorem 7.1.2"
prerequisites:
  - turan-theorem
  - turan-graph
  - extremal-number
  - regularity-lemma
extends:
  - turan-theorem
related:
  - edge-density
  - regularity-graph
  - embedding-lemma
answers_questions:
  - "How does edge density relate to the existence of subgraphs?"
  - "What is the asymptotic extremal density for a given graph H?"
---

# Quick Definition
The Erdos-Stone theorem states that for r >= 2, s >= 1, and any epsilon > 0, every sufficiently large graph with at least t_{r-1}(n) + epsilon*n^2 edges contains K_s^r as a subgraph.

# Core Definition
**Theorem 7.1.2** (Erdos & Stone 1946): For all integers r >= 2 and s >= 1, and every epsilon > 0, there exists an integer n_0 such that every graph with n >= n_0 vertices and at least t_{r-1}(n) + epsilon*n^2 edges contains K_s^r as a subgraph.

**Corollary 7.1.3**: For every graph H with at least one edge,
lim_{n->infinity} ex(n,H) / C(n,2) = (chi(H) - 2) / (chi(H) - 1).

This means the asymptotic extremal density is determined by the chromatic number of H alone. (Diestel, pp. 167-168)

# Prerequisites
- **Turan's theorem** — The Erdos-Stone theorem extends it
- **Turan graph** — The threshold t_{r-1}(n) appears in the statement
- **Extremal number** — The corollary determines the asymptotic value of ex(n,H)
- **Regularity lemma** — Used in the proof (Section 7.5)

# Key Properties
1. Just epsilon*n^2 edges beyond the Turan number force not just K^r but the much larger K_s^r
2. The asymptotic extremal density depends only on chi(H)
3. For bipartite H (chi(H) = 2), the limit is 0, meaning ex(n,H) is o(n^2)
4. Established as a "meta-theorem" for dense extremal graph theory
5. The proof uses the regularity lemma (Section 7.5)

# Context & Application
The Erdos-Stone theorem is the fundamental result of dense extremal graph theory. Its corollary shows that the chromatic number of H completely determines the asymptotic behaviour of ex(n, H) up to lower-order terms. Diestel calls Corollary 7.1.3 an "entirely unexpected" result that "established the theorem as a kind of meta-theorem."

# Examples
**Example** (p. 168): For H with chi(H) = r, we have H subset K_s^r for large s, so ex(n,H) is sandwiched between t_{r-1}(n) and t_{r-1}(n) + epsilon*n^2 for any epsilon.

# Relationships
## Builds Upon
- **Turan's theorem** — The starting point; Erdos-Stone refines it

## Enables
- Asymptotic determination of **extremal number** for all H
- **Edge density** — The critical density is (chi(H)-2)/(chi(H)-1)

# Common Confusions
- **Confusion**: Thinking the Erdos-Stone theorem determines ex(n, H) exactly
  **Clarification**: It gives the asymptotic LIMIT of ex(n,H)/C(n,2); the exact value of ex(n,H) remains unknown for most H

# Source Reference
Chapter 7, Section 7.1, Theorem 7.1.2, pages 167-168 (pdf pages 177-178). Proof in Section 7.5.

# Verification Notes
- Confidence: HIGH — named theorem with full proof later in the chapter
