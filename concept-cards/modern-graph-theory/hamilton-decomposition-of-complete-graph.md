---
concept: Hamilton Decomposition of Complete Graph
slug: hamilton-decomposition-of-complete-graph
category: paths-and-cycles
subcategory: hamilton-euler
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.3 Hamilton Cycles and Euler Circuits"
extraction_confidence: high
aliases: []
prerequisites:
  - complete-graph
  - hamilton-cycle
  - hamilton-path
extends: []
related:
  - euler-circuit
contrasts_with: []
answers_questions:
  - "When can a complete graph be decomposed into Hamilton cycles?"
---

# Quick Definition

For odd $n \ge 3$, $K_n$ can be decomposed into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton cycles. For even $n \ge 2$, $K_n$ can be decomposed into $\frac{1}{2}(n-1)$ edge-disjoint Hamilton paths.

# Core Definition

"**Theorem 11.** For $n \ge 3$ the complete graph $K_n$ is decomposable into edge disjoint Hamilton cycles iff $n$ is odd. For $n \ge 2$ the complete graph $K_n$ is decomposable into edge-disjoint Hamilton paths iff $n$ is even" (Bollobás, p. 24).

# Prerequisites

- **Complete graph** — The theorem concerns $K_n$
- **Hamilton cycle** — The decomposition uses Hamilton cycles
- **Hamilton path** — Used for even $n$

# Key Properties

1. $K_n$ with odd $n$ decomposes into $\frac{1}{2}(n-1)$ Hamilton cycles
2. $K_n$ with even $n$ decomposes into $\frac{1}{2}(n-1)$ Hamilton paths
3. Necessity: $K_n$ is $(n-1)$-regular, so $n-1$ must be even for Hamilton cycle decomposition
4. The construction extends Hamilton paths in $K_{n-1}$ to Hamilton cycles in $K_n$

# Construction / Recognition

1. For even $n$: decompose $K_n$ into $\frac{1}{2}(n-1)$ Hamilton paths (see Fig. I.13)
2. Each vertex is the endpoint of exactly one path
3. For odd $n$: add a vertex to $K_{n-1}$ and extend each Hamilton path to a Hamilton cycle

# Context & Application

This result shows that the travelling salesman can arrange his journeys so that each route is a Hamilton cycle, covering all edges of $K_n$ without repetition, provided $n$ is odd.

# Examples

**Example** (p. 24): Fig. I.13 shows three edge-disjoint Hamilton paths in $K_6$.

# Relationships

## Builds Upon
- **Complete graph**, **Hamilton cycle**, **Hamilton path**

## Related
- **Euler circuit** — Concatenating the Hamilton cycles gives an Euler circuit of $K_n$ for odd $n$

# Common Errors

- **Error**: Trying to decompose $K_n$ into Hamilton cycles when $n$ is even
  **Correction**: For even $n$, only Hamilton path decomposition is possible

# Common Confusions

- **Confusion**: Thinking this works for arbitrary graphs
  **Clarification**: This result is specific to complete graphs; decomposing general regular graphs into Hamilton cycles is much harder

# Source Reference

Chapter I: Fundamentals, Section I.3, Theorem 11, page 24.

# Verification Notes

- Definition source: Direct theorem statement from p. 24
- Confidence rationale: Explicitly stated with constructive proof
- Uncertainties: None
- Cross-reference status: Verified
