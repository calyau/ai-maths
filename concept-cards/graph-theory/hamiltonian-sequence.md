---
concept: Hamiltonian Sequence
slug: hamiltonian-sequence
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
  - "hamiltonian degree sequence"
prerequisites:
  - degree-sequence
  - hamiltonian-graph
extends: []
related:
  - chvatals-theorem
contrasts_with:
  - path-hamiltonian-sequence
answers_questions:
  - "What is a Hamiltonian sequence?"
---

# Quick Definition
An integer sequence (a1, ..., an) is Hamiltonian if every graph with n vertices whose degree sequence is pointwise greater than (a1, ..., an) is Hamiltonian.

# Core Definition
Call an arbitrary integer sequence (a1, ..., an) **hamiltonian** if every graph with n vertices and a degree sequence pointwise greater than (a1, ..., an) is hamiltonian. A sequence (d1, ..., dn) is pointwise greater than (a1, ..., an) if di >= ai for all i (Diestel, p. 289).

# Prerequisites
- **Degree sequence** — Hamiltonian sequences are conditions on degree sequences
- **Hamiltonian graph** — the property being forced

# Key Properties
1. A Hamiltonian sequence forces Hamiltonicity for all graphs with that or larger degree sequence
2. Chvatal's theorem characterizes exactly which sequences are Hamiltonian
3. The condition: for every i < n/2, ai <= i implies a_{n-i} >= n-i
4. Dirac's condition (all degrees >= n/2) corresponds to the Hamiltonian sequence (n/2, ..., n/2)
5. Not every Hamiltonian graph has a Hamiltonian degree sequence (Exercise 7)

# Context & Application
Hamiltonian sequences capture the idea of "enough degrees to force Hamiltonicity." Chvatal's theorem provides the complete characterization, showing exactly which degree thresholds are sufficient.

# Examples
**Example**: The sequence (n/2, ..., n/2) is Hamiltonian (this is Dirac's theorem). The sequence (1, 1, n-2, n-1) for n >= 4 is Hamiltonian (by Chvatal's condition).

# Relationships
## Builds Upon
- **Degree sequence**, **Hamiltonian graph**

## Enables
- **Chvatal's theorem** — characterizes all Hamiltonian sequences

## Contrasts With
- **Path-Hamiltonian sequence** — forces Hamilton paths instead of cycles

# Source Reference
Chapter 10, Section 10.2, p. 289 (pdf p. 289).

# Verification Notes
- Definition from p. 289
- Confidence: HIGH — explicitly defined
