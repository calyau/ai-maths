---
concept: Vertex Degree
slug: vertex-degree
category: graph-fundamentals
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.1 Definitions"
extraction_confidence: high
aliases:
  - degree
  - "$d(x)$"
  - minimum degree "$\\delta(G)$"
  - maximum degree "$\\Delta(G)$"
  - regular graph
  - k-regular
  - cubic graph
prerequisites:
  - graph
  - neighbourhood
extends: []
related:
  - degree-sequence
  - handshaking-lemma
contrasts_with: []
answers_questions:
  - "What is the degree of a vertex?"
  - "What is a regular graph?"
---

# Quick Definition

The degree $d(x) = |\Gamma(x)|$ of a vertex $x$ is the number of edges incident with $x$. A graph is $k$-regular if every vertex has degree $k$.

# Core Definition

"The degree of $x$ is $d(x) = |\Gamma(x)|$" (Bollobás, p. 11). The minimum degree is $\delta(G)$ and the maximum degree is $\Delta(G)$. "A vertex of degree 0 is said to be an isolated vertex. If $\delta(G) = \Delta(G) = k$, that is, every vertex of $G$ has degree $k$, then $G$ is said to be $k$-regular or regular of degree $k$. [...] A 3-regular graph is said to be cubic" (p. 12).

# Prerequisites

- **Graph** — Degree is defined within a graph
- **Neighbourhood** — Degree is the size of the neighbourhood

# Key Properties

1. $0 \le \delta(G) \le d(x) \le \Delta(G) \le n - 1$
2. $\delta(G) \le \lfloor 2e(G)/n \rfloor$ and $\Delta(G) \ge \lceil 2e(G)/n \rceil$
3. A vertex of degree 0 is isolated
4. A graph is regular if all vertices have the same degree
5. Cubic = 3-regular

# Construction / Recognition

To find $d(x)$: count the number of edges incident with $x$, or equivalently count $|\Gamma(x)|$.

# Context & Application

Degree is a fundamental local property of a vertex. It appears in the handshaking lemma, degree sequence characterizations, and as a parameter in many extremal results. The minimum degree $\delta(G)$ often governs the existence of substructures like Hamilton cycles.

# Examples

**Example** (p. 12): In $K_n$, every vertex has degree $n - 1$, so $K_n$ is $(n-1)$-regular. The Petersen graph is cubic (3-regular).

# Relationships

## Builds Upon
- **Graph**, **Neighbourhood**

## Enables
- **Degree sequence** — The ordered list of all vertex degrees
- **Handshaking lemma** — Sum of degrees equals twice the number of edges
- **Regular graph theory** — Study of $k$-regular graphs

# Common Errors

- **Error**: Counting each edge twice when computing degree
  **Correction**: Each edge contributes 1 to the degree of each of its two endvertices

# Common Confusions

- **Confusion**: In multigraphs, a loop contributes 2 to the degree, not 1
  **Clarification**: In simple graphs this issue does not arise since loops are forbidden

# Source Reference

Chapter I: Fundamentals, Section I.1 Definitions, pages 11-12.

# Verification Notes

- Definition source: Direct from pp. 11-12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
