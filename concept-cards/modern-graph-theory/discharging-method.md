---
concept: Discharging Method
slug: discharging-method
category: planar-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 167
section: "V.3 Graphs on Surfaces"
extraction_confidence: medium
aliases:
  - "discharging argument"
  - "discharging rules"
prerequisites:
  - euler-formula-for-planar-graphs
  - unavoidable-set
extends: []
related:
  - four-colour-theorem
  - reducible-configuration
contrasts_with: []
answers_questions:
  - "How is the discharging method used to prove unavoidability?"
---

# Quick Definition
The discharging method assigns charges to vertices/faces of a planar graph (based on Euler's formula ensuring total charge > 0), then redistributes charges via rules to show certain configurations must exist.

# Core Definition
In the discharging method, one assigns a charge of 6 − k to each vertex of degree k in a maximal plane graph. By Euler's formula, the total charge is 12 (positive). Charges are then transferred between vertices according to **discharging rules** until the distribution reveals that one of finitely many target configurations must be present. This technique is used to prove that a set of configurations is unavoidable (Bollobás, p. 167).

# Prerequisites
- **Euler's formula for planar graphs** — guarantees positive total charge
- **Unavoidable set** — the concept being established

# Key Properties
1. Total initial charge is always 12 (for maximal planar graphs)
2. Discharging does not change total charge, only redistributes it
3. Appel-Haken: 300+ rules; Robertson et al.: 32 rules
4. The method extends to graphs on surfaces using the Euler-Poincaré formula

# Context & Application
The discharging method, initiated by Heesch, is the key technique for proving unavoidability in the four-colour theorem and many structural results about planar graphs. It has become a standard tool in graph theory.

# Relationships
## Builds Upon
- **Euler's formula** — ensures positive total charge

## Enables
- Unavoidability proofs for the four-colour theorem

# Source Reference
Chapter V: Colouring, Section V.3, page 167.

# Verification Notes
- Definition source: Described on p. 167
- Confidence rationale: Medium — described conceptually but details of rules not given
- Uncertainties: Specific rules not enumerated
- Cross-reference status: Verified
