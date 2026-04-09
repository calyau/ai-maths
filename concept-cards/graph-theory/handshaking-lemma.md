---
concept: Handshaking Lemma
slug: handshaking-lemma

category: graph-fundamentals
tier: foundational

source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "The Basics"
chapter_number: 1
pdf_page: 15
section: "1.2 The degree of a vertex"

extraction_confidence: high

aliases:
  - "Proposition 1.2.1"
  - "degree sum formula"

prerequisites:
  - graph
  - degree
  - edge
extends: []
related:
  - average-degree
  - euler-tour
contrasts_with: []

answers_questions:
  - "What is the Handshaking Lemma?"
  - "Why is the number of vertices of odd degree always even?"
---

# Quick Definition
The sum of all vertex degrees in a graph equals twice the number of edges. Consequently, the number of vertices of odd degree is always even.

# Core Definition
If we sum up all the vertex degrees in G, we count every edge exactly twice: once from each of its ends. Thus |E| = (1/2) * sum of d(v). Proposition 1.2.1: The number of vertices of odd degree in a graph is always even (Diestel, p. 5).

# Prerequisites
- **Graph** — the lemma applies to any graph
- **Degree** — it concerns the sum of degrees
- **Edge** — it relates degrees to edge count

# Key Properties
1. Sum of d(v) over all v = 2|E|
2. The number of odd-degree vertices is even
3. epsilon(G) = d(G)/2 follows directly

# Construction / Recognition
## Proof Sketch
A graph on V has (1/2) * sum of d(v) edges, so sum of d(v) is an even number. Hence the number of vertices with odd degree must be even.

# Context & Application
This is one of the most fundamental results in graph theory. It is used in the proof of Euler's theorem and many other results.

# Relationships
## Builds Upon
- **degree**, **edge**

## Enables
- **euler-tour** — the characterization of Eulerian graphs uses even degrees

# Source Reference
Chapter 1: The Basics, Section 1.2, Proposition 1.2.1, page 5 (pdf p. 15).

# Verification Notes
- Direct from p. 5, Proposition 1.2.1
- Confidence: HIGH — explicitly stated as a proposition with proof
