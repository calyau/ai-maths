---
concept: Euler Characteristic
slug: euler-characteristic
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "chi(S)"
prerequisites:
  - surface
  - euler-formula
extends:
  - euler-formula
related:
  - euler-genus
  - genus
contrasts_with: []
answers_questions:
  - "What is the Euler characteristic of a surface?"
  - "How does Euler's formula generalize to surfaces?"
---

# Quick Definition
The Euler characteristic chi(S) of a surface S is the integer such that n - m + l = chi(S) whenever a graph with n vertices, m edges is embedded in S with l disc faces. For the sphere, chi = 2.

# Core Definition
**Theorem B.2**: "For every surface S there exists an integer chi(S) such that whenever a graph G with n vertices and m edges is embedded in S so that there are l faces and every face is a disc, we have n - m + l = chi(S)" (Diestel, p. 363).

# Prerequisites
- **Surface** -- chi is defined for surfaces
- **Euler's formula** -- Generalizes n - m + l = 2

# Key Properties
1. chi(S^2) = 2 (the sphere)
2. chi is negative for most surfaces
3. chi(S) = 2 - epsilon(S), where epsilon is the Euler genus
4. Adding a handle decreases chi by 2
5. Adding a crosscap decreases chi by 1
6. chi is a topological invariant: distinct surfaces have distinct chi

# Context & Application
The Euler characteristic is the fundamental topological invariant of surfaces. It extends Euler's formula from the plane to arbitrary surfaces and provides the key tool for distinguishing surfaces. The generalized Euler formula is central to the graph minor theorem.

# Relationships
## Builds Upon
- **Surface**, **Euler's formula**

## Enables
- **Euler genus** -- epsilon(S) = 2 - chi(S)
- Surface classification
- Graph minor theorem

# Source Reference
Appendix B, Theorem B.2, page 363.

# Verification Notes
- Theorem statement from p. 363
- Confidence: HIGH -- named theorem
