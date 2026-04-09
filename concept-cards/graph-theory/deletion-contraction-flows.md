---
concept: Deletion-Contraction for Flows
slug: deletion-contraction-flows
category: network-flows
subcategory: algebraic-flows
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Flows"
chapter_number: 6
pdf_page: 155
section: "6.3 Group-valued flows"
extraction_confidence: high
aliases: []
prerequisites:
  - flow-polynomial
  - h-flow
related:
  - tutte-polynomial-mention
answers_questions:
  - "How does deletion-contraction apply to flows?"
---

# Quick Definition
The flow polynomial satisfies P(G) = P(G/e) - P(G-e) for any non-loop edge e, mirroring the deletion-contraction recurrence of the chromatic polynomial.

# Core Definition
In the proof of Theorem 6.3.1: for a non-loop edge e_0, the number of H-flows on G equals P_2(k) - P_1(k), where P_1 is the flow polynomial of G - e_0 and P_2 is the flow polynomial of G / e_0. The H-flows on G correspond to circulations that are nowhere zero except possibly on e_0 (set F_2) minus those that ARE zero on e_0 (set F_1). (Diestel, pp. 145-146)

# Prerequisites
- **Flow polynomial** — The recurrence defines the polynomial
- **H-flow** — The objects being counted

# Key Properties
1. P(G) = P(G/e) - P(G-e) for non-loop edges e
2. Parallels the chromatic polynomial's deletion-contraction
3. Base case: for all loops, P = x^m
4. Both are specializations of the Tutte polynomial

# Source Reference
Chapter 6, Section 6.3, proof of Theorem 6.3.1, pages 145-146 (pdf pages 155-156).

# Verification Notes
- Confidence: HIGH — explicit in the proof
