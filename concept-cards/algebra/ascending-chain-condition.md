---
concept: Ascending Chain Condition
slug: ascending-chain-condition
category: module-theory
subcategory: ring-properties
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.6 Noetherian Rings"
extraction_confidence: high
aliases:
  - "ACC"
prerequisites:
  - module
extends: []
related:
  - noetherian-ring
  - noetherian-module
contrasts_with: []
answers_questions:
  - "What is the ascending chain condition?"
---

# Quick Definition

The ascending chain condition (ACC) on an R-module V states that there is no infinite strictly increasing chain W_1 < W_2 < ... of submodules of V. It is equivalent to every submodule being finitely generated.

# Core Definition

The following conditions on an R-module V are equivalent (Artin, Proposition 14.6.1): (i) Every submodule of V is finitely generated; (ii) Ascending chain condition: there is no infinite strictly increasing chain W_1 < W_2 < ... of submodules of V. A ring is Noetherian if and only if it satisfies the ACC on ideals (Corollary 14.6.3).

# Prerequisites

- **Module** -- The ACC is a property of modules

# Key Properties

1. Equivalent to every submodule being finitely generated (14.6.1)
2. For a ring R, ACC on ideals is equivalent to being Noetherian (14.6.3)
3. If an increasing chain stabilizes, every element of the union is in some W_k

# Context & Application

The ACC provides the chain condition formulation of the Noetherian property, which is often easier to verify than directly checking finite generation of all submodules.

# Examples

**Example 1** (p. 449): In Z, the chain (2) < (1) shows that chains do terminate (Z is Noetherian).

# Relationships

## Related
- **Noetherian ring** -- A ring satisfying ACC on ideals
- **Noetherian module** -- A module satisfying ACC on submodules

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.6, pages 448-449. Proposition 14.6.1, Corollary 14.6.3.

# Verification Notes

- Definition source: Direct from Artin, Proposition 14.6.1
- Confidence rationale: Explicitly stated with equivalence proof
- Uncertainties: None
- Cross-reference status: Verified
