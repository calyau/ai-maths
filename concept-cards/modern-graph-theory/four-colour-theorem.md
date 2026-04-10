---
concept: Four Colour Theorem
slug: four-colour-theorem
category: planar-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 161
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "four color theorem"
  - "4-colour theorem"
prerequisites:
  - five-colour-theorem
  - kempe-chain
  - reducible-configuration
  - unavoidable-set
extends:
  - five-colour-theorem
related:
  - heawood-bound
contrasts_with:
  - five-colour-theorem
answers_questions:
  - "How many colours suffice to colour any planar graph?"
---

# Quick Definition
Every planar graph is 4-colourable. Proved by Appel and Haken in 1976 using computers, it is the most famous result in graph theory.

# Core Definition
The four colour theorem states that every plane graph can be coloured with four colours such that no two adjacent regions share a colour. Equivalently, χ(G) ≤ 4 for every planar graph G. The problem was posed by Francis Guthrie in 1852, popularized by Cayley in 1878, and solved by Appel and Haken in 1976, with a simplified proof by Robertson, Sanders, Seymour and Thomas in the 1990s (Bollobás, pp. 161, 164–166).

# Prerequisites
- **Five colour theorem** — the weaker result proved by similar but simpler methods
- **Kempe chain** — the proof technique from Kempe's 1879 approach
- **Reducible configuration** — key notion in the proof
- **Unavoidable set** — complementary key notion

# Key Properties
1. χ(G) ≤ 4 for every planar graph G
2. K₄ is planar and 4-chromatic, so the bound is tight
3. The proof requires finding an unavoidable set of reducible configurations
4. Appel-Haken used over 1900 reducible configurations and 300 discharging rules
5. Robertson et al. reduced to 633 configurations and 32 discharging rules
6. No human-verifiable proof is known

# Construction / Recognition
## Proof Framework
1. Identify **reducible configurations** — clusters of vertices that no minimal counterexample can contain
2. Identify an **unavoidable set** — show every planar graph contains at least one reducible configuration (using Euler's formula and discharging)
3. These two facts together prove no minimal counterexample exists

# Context & Application
The four colour problem was the most famous open problem in graph theory for over 120 years. Its proof initiated the era of computer-assisted proofs in mathematics. Petersen observed (1891) it is equivalent to every 2-connected cubic planar graph having chromatic index 3.

# Examples
**Example** (p. 162): K₄ and K₁ + C₅ are planar graphs requiring exactly 4 colours.

# Relationships
## Builds Upon
- **Five colour theorem** — the weaker result using similar ideas
- **Kempe chain** — exchange technique used in both proofs

## Related
- **Hadwiger's conjecture** — generalizes: if χ(G) = k then G contracts to Kₖ

## Contrasts With
- **Five colour theorem** — much easier to prove, uses similar ideas

# Common Errors
- **Error**: Thinking Kempe's 1879 proof was correct
  **Correction**: Heawood found the error in 1890; the chain exchange argument fails for 4 colours

# Common Confusions
- **Confusion**: Thinking the four colour theorem is about colouring maps (countries)
  **Clarification**: It is equivalent to vertex colouring of planar graphs; the map version is the dual formulation

# Source Reference
Chapter V: Colouring, Section V.3, pages 161, 164–167.

# Verification Notes
- Definition source: Direct discussion pp. 161, 164–167
- Confidence rationale: Famous theorem extensively discussed
- Uncertainties: None
- Cross-reference status: Verified
