---
concept: Kernel (of a Directed Graph)
slug: kernel
category: graph-colouring
subcategory: list-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "5.4 List colouring"
extraction_confidence: high
aliases: []
prerequisites:
  - graph
extends: []
related:
  - list-colouring
  - galvin-theorem
contrasts_with: []
answers_questions:
  - "What is a kernel in a directed graph?"
---

# Quick Definition
A kernel of a directed graph D is an independent set U such that every vertex not in U sends a directed edge to some vertex in U.

# Core Definition
"Let us call an independent set U of V(D) a kernel of D if, for every vertex v in D - U, there is an edge in D directed from v to a vertex in U" (Diestel, p. 124).

# Prerequisites
- **Graph** -- Defined for directed graphs

# Key Properties
1. A kernel is both independent and absorbing
2. Non-empty directed graphs always have non-empty kernels (when they exist)
3. Not every directed graph has a kernel
4. Every directed graph without odd directed cycles has a kernel (Richardson's theorem)
5. Used in Lemma 5.4.3 to prove list colouring results

# Context & Application
Kernels provide the technical tool for Galvin's proof that bipartite graphs satisfy ch' = chi'. The key is orienting the line graph so that every induced subgraph has a kernel, then using Lemma 5.4.3 to obtain list colourings.

# Relationships
## Enables
- **Galvin's theorem** -- Uses kernels via Lemma 5.4.3

# Source Reference
Chapter 5, Section 5.4, page 124.

# Verification Notes
- Definition from p. 124
- Confidence: HIGH -- explicit definition
