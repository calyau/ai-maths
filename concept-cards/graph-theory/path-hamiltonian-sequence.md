---
concept: Path-Hamiltonian Sequence
slug: path-hamiltonian-sequence
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 291
section: "10.2 Hamilton cycles and degree sequences"
extraction_confidence: high
aliases:
  - "path-hamiltonian"
prerequisites:
  - hamiltonian-sequence
  - hamilton-path
extends:
  - hamiltonian-sequence
related:
  - chvatals-theorem
contrasts_with:
  - hamiltonian-sequence
answers_questions:
  - "What is a path-Hamiltonian sequence?"
---

# Quick Definition
An integer sequence is path-Hamiltonian if every graph with a pointwise greater degree sequence has a Hamilton path.

# Core Definition
An integer sequence is called **path-hamiltonian** if every graph with a pointwise greater degree sequence has a Hamilton path (Diestel, p. 291).

**Corollary 10.2.2.** An integer sequence (a1, ..., an) with n >= 2 and 0 <= a1 <= ... <= an < n is path-hamiltonian if and only if every i <= n/2 satisfies: ai < i implies a_{n+1-i} >= n-i.

# Prerequisites
- **Hamiltonian sequence** — the analogous concept for cycles
- **Hamilton path** — the property being forced

# Key Properties
1. Derived from Chvatal's theorem by applying it to G * K1
2. The condition is: for every i <= n/2, ai < i implies a_{n+1-i} >= n-i
3. Slightly weaker than the Hamiltonian sequence condition

# Context & Application
Path-Hamiltonian sequences extend Chvatal's framework from cycles to paths, providing a complete characterization of degree sequences that force Hamilton paths.

# Examples
**Example**: The sequence (0, 1, 1) is path-Hamiltonian for n = 3 (every graph on 3 vertices with at least these degrees has a Hamilton path).

# Relationships
## Builds Upon
- **Hamiltonian sequence**, **Hamilton path**

## Related
- **Chvatal's theorem** — the cycle version

## Contrasts With
- **Hamiltonian sequence** — forces Hamilton cycles rather than paths

# Source Reference
Chapter 10, Section 10.2, Corollary 10.2.2, p. 291 (pdf p. 291).

# Verification Notes
- Corollary from p. 291
- Confidence: HIGH — explicit corollary
