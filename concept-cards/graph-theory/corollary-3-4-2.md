---
concept: Corollary of Mader's Theorem
slug: corollary-3-4-2
category: connectivity
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Connectivity"
chapter_number: 3
pdf_page: 79
section: "3.4 Mader's theorem"
extraction_confidence: high
aliases:
  - "Corollary 3.4.2"
prerequisites:
  - maders-theorem
  - kappa-g-h
  - lambda-g-h
extends:
  - maders-theorem
related: []
contrasts_with: []
answers_questions:
  - "How many independent H-paths are guaranteed by kappa_G(H)?"
---

# Quick Definition
There are at least kappa_G(H)/2 independent H-paths and at least lambda_G(H)/2 edge-disjoint H-paths in G.

# Core Definition
**Corollary 3.4.2.** Given a graph G with an induced subgraph H, there are at least (1/2)*kappa_G(H) independent H-paths and at least (1/2)*lambda_G(H) edge-disjoint H-paths in G (Diestel, p. 79).

# Prerequisites
- **Mader's theorem** — the corollary follows from the general theorem
- **kappa_G(H)** — vertex separator for H-paths
- **lambda_G(H)** — edge separator for H-paths

# Key Properties
1. The factor 1/2 is best possible (Exercises 19, 20)
2. Follows from Mader's theorem by taking F = empty or X = empty
3. Contrasts with Menger's theorem where the bound is exact (no 1/2 factor)
4. The 1/2 factor comes from the floor function in partial C contributions

# Context & Application
This corollary gives clean bounds on H-paths from the more complex Mader's theorem. The factor of 1/2 is surprising and shows that H-paths are harder to find than ordinary A-B paths.

# Examples
**Example** (Exercise 19): There exist G, H where exactly kappa_G(H)/2 independent H-paths exist (the bound is tight).

# Relationships
## Builds Upon
- **Mader's theorem**, **kappa_G(H)**, **lambda_G(H)**

# Source Reference
Chapter 3, Section 3.4, Corollary 3.4.2, p. 79 (pdf p. 79).

# Verification Notes
- Corollary from p. 79
- Confidence: HIGH — explicit corollary with proof
