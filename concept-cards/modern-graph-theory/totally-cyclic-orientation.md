---
concept: Totally Cyclic Orientation
slug: totally-cyclic-orientation
category: tutte-polynomial
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "The Tutte Polynomial"
chapter_number: 10
pdf_page: 379
section: "X.7 Exercises"
extraction_confidence: high
aliases: []
prerequisites:
  - tutte-polynomial
  - special-values-tutte-polynomial
extends: []
related:
  - acyclic-orientation-count
contrasts_with:
  - acyclic-orientation-count
answers_questions:
  - "What information does the Tutte polynomial encode?"
---

# Quick Definition
A totally cyclic orientation of a bridgeless graph is an orientation where every edge lies in some oriented cycle. The number of such orientations is $T_G(0, 2)$.

# Core Definition
Exercise 10 (p. 379): "An orientation of a graph is totally cyclic if every edge is contained in some oriented cycle. Prove that the number of totally cyclic orientations of a bridgeless graph is $T_G(0, 2)$."

# Prerequisites
- **Tutte polynomial**, **special-values-tutte-polynomial**

# Key Properties
1. Requires the graph to be bridgeless (bridges cannot be in oriented cycles)
2. $T_G(0, 2)$ counts totally cyclic orientations
3. Dual to acyclic orientations: $T_G(2, 0)$ counts acyclic, $T_G(0, 2)$ counts totally cyclic

# Relationships
## Builds Upon
- **tutte-polynomial**, **special-values-tutte-polynomial**

## Contrasts With
- **acyclic-orientation-count** — $T_G(2,0)$ for acyclic; $T_G(0,2)$ for totally cyclic

# Source Reference
Chapter X, Exercise 10, page 379.

# Verification Notes
- Definition source: From Exercise 10
- Confidence rationale: Explicit exercise statement
- Uncertainties: None
- Cross-reference status: Verified
