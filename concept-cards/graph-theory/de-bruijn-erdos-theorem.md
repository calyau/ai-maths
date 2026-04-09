---
concept: "De Bruijn-Erdős Theorem"
slug: de-bruijn-erdos-theorem
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 211
section: "8.1 Basic notions, facts and techniques"
extraction_confidence: high
aliases:
  - "compactness theorem for colouring"
  - "Theorem 8.1.3"
prerequisites:
  - konigs-infinity-lemma
  - compactness-principle
extends: []
related: []
contrasts_with: []
answers_questions:
  - "Can chromatic number results be transferred from finite to infinite graphs?"
---

# Quick Definition
The de Bruijn-Erdős theorem (1951) states that if every finite subgraph of G is k-colourable, then G is k-colourable. It is the prototypical compactness result in graph theory.

# Core Definition
**Theorem 8.1.3** (de Bruijn & Erdős, 1951): Let G = (V, E) be a graph and k in N. If every finite subgraph of G has chromatic number at most k, then so does G (Diestel, p. 211).

# Prerequisites
- **König's infinity lemma** — Used in the proof for countable G
- **Compactness principle** — The theorem is the archetypal compactness result

# Key Properties
1. Two proofs given: one by the infinity lemma (countable case), one by Tychonoff's theorem (general)
2. The infinity lemma proof: enumerate vertices, build tree of compatible k-colourings, find ray
3. The Tychonoff proof: product space of {1,...,k}^V is compact; intersection of closed sets is nonempty

# Source Reference
Chapter 8, Section 8.1, pages 211-212 (Theorem 8.1.3).

# Verification Notes
- Statement and two proofs from pp. 211-212
- Confidence: HIGH — named theorem with two proofs
