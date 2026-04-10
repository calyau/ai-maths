---
concept: Connected Spanning Subgraph Count
slug: connected-spanning-subgraph-count
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 352
section: "X.4 Special Values of the Tutte Polynomial"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - special-values-tutte-polynomial
extends: []
related:
  - spanning-tree-count
  - forest-count
contrasts_with: []
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
The number of connected spanning subgraphs of a connected graph $G$ is $T_G(1,2)$.

# Core Definition
From Theorem 5 (p. 352): $T_G(1,2) = |\{F \subset E : r(F) = r(G)\}|$, counting edge sets whose spanning subgraph has maximal rank (i.e., is connected).

# Prerequisites
- **Tutte polynomial**, **special-values-tutte-polynomial**

# Key Properties
1. $T_G(1,2) = $ number of connected spanning subgraphs
2. $T_G(2,2) = 2^{|E|}$ = total number of spanning subgraphs

# Relationships
## Builds Upon
- **tutte-polynomial**, **special-values-tutte-polynomial**

## Related
- **spanning-tree-count** — Spanning trees are minimal connected spanning subgraphs

# Source Reference
Chapter X, Section X.4, Theorem 5, page 352.

# Verification Notes
- Definition source: Direct from Theorem 5
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
