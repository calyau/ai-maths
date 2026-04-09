---
concept: "Chvatal's Theorem"
slug: chvatals-theorem
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 289
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: high
aliases:
  - "Chvatal 1972"
  - "Chvatal's degree sequence theorem"
prerequisites:
  - hamiltonian-sequence
  - degree-sequence
  - hamiltonian-graph
extends:
  - diracs-theorem
related:
  - ores-theorem
  - hamiltonian-closure
contrasts_with: []
answers_questions:
  - "How does the degree sequence relate to Hamiltonicity?"
  - "What is Chvatal's theorem?"
---

# Quick Definition
An integer sequence (a1, ..., an) with 0 <= a1 <= ... <= an < n and n >= 3 is Hamiltonian if and only if for every i < n/2: ai <= i implies a_{n-i} >= n-i.

# Core Definition
**Theorem 10.2.1 (Chvatal 1972).** An integer sequence (a1, ..., an) such that 0 <= a1 <= ... <= an < n and n >= 3 is hamiltonian if and only if the following holds for every i < n/2: ai <= i implies a_{n-i} >= n-i (Diestel, p. 289).

# Prerequisites
- **Hamiltonian sequence** — the concept being characterized
- **Degree sequence** — the theorem applies to degree sequences
- **Hamiltonian graph** — the property being forced

# Key Properties
1. Complete characterization of Hamiltonian sequences
2. Encompasses all earlier results: Dirac, Ore, Posa
3. The condition is symmetric: if the "low degrees" are too small, the "high degrees" must compensate
4. The proof uses edge-maximality: take G without a Hamilton cycle, maximal with respect to edges
5. The condition ai <= i => a_{n-i} >= n-i is both necessary and sufficient

# Construction / Recognition
## Proof Strategy (Forward Direction)
1. Assume the condition holds; suppose for contradiction there's a non-Hamiltonian graph G with pointwise larger degrees
2. Take G edge-maximal without a Hamilton cycle
3. Find non-adjacent x, y with d(x) + d(y) maximum; G+xy has a Hamilton cycle H
4. H-xy gives a Hamilton path x1,...,xn with x1=x, xn=y
5. Define index sets I, J; show I intersect J = empty, so d(x)+d(y) < n
6. Derive contradiction using the Chvatal condition

# Context & Application
Chvatal's theorem is the culmination of the development of degree conditions for Hamiltonicity. It provides a single theorem that encompasses all earlier results. Exercise 8 shows it implies Dirac's theorem: if fewer than i vertices have degree <= i for every i < n/2, then G is Hamiltonian.

# Examples
**Example** (p. 290, Fig. 10.2.1): For the backward direction, a non-Hamiltonian graph with the degree sequence (h,...,h, n-h-1,...,n-h-1, n-1,...,n-1) is constructed, showing the condition is tight.

# Relationships
## Builds Upon
- **Hamiltonian sequence**, **degree sequence**, **Hamiltonian graph**

## Enables
- **Corollary 10.2.2** — path-Hamiltonian sequence characterization

## Related
- **Dirac's theorem** — special case with all ai = n/2
- **Ore's theorem** — also a special case

# Common Errors
- **Error**: Checking the condition only for i = 1
  **Correction**: The condition must hold for all i < n/2

# Common Confusions
- **Confusion**: Thinking Chvatal's theorem applies to a specific graph
  **Clarification**: It applies to degree sequences, not specific graphs; every graph with a pointwise larger degree sequence must be Hamiltonian

# Source Reference
Chapter 10, Section 10.2, Theorem 10.2.1, pp. 289-291 (pdf pp. 289-291).

# Verification Notes
- Theorem from p. 289
- Full proof from pp. 289-291
- Confidence: HIGH — major theorem with complete proof
