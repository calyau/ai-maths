---
concept: Noetherian Module
slug: noetherian-module
category: module-theory
subcategory: module-properties
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.6 Noetherian Rings"
extraction_confidence: high
aliases: []
prerequisites:
  - module
  - noetherian-ring
extends: []
related:
  - ascending-chain-condition
  - finitely-generated-module
contrasts_with: []
answers_questions:
  - "What is a Noetherian module?"
---

# Quick Definition

A module V is Noetherian if every submodule of V is finitely generated, equivalently if V satisfies the ascending chain condition on submodules.

# Core Definition

The following conditions on an R-module V are equivalent (Artin, Proposition 14.6.1): (i) every submodule of V is finitely generated; (ii) there is no infinite strictly increasing chain of submodules. If R is Noetherian, then every submodule of a finitely generated R-module is finitely generated (Theorem 14.6.5).

# Prerequisites

- **Module** -- Noetherian is a property of modules
- **Noetherian ring** -- Over Noetherian rings, finitely generated modules are Noetherian

# Key Properties

1. Every submodule of a Noetherian module is finitely generated
2. If R is Noetherian and V is finitely generated, then V is Noetherian (14.6.5)
3. This ensures existence of presentation matrices for finitely generated modules

# Context & Application

The Noetherian property for modules guarantees that the module of relations in a presentation is finitely generated, completing the foundation for the theory of generators and relations.

# Examples

**Example 1** (p. 451): R^m is a Noetherian module over a Noetherian ring R.

# Relationships

## Builds Upon
- **Noetherian ring** -- Provides the base ring
- **Module** -- Noetherian is a module property

## Enables
- **Generators and relations** -- Ensures relation modules are finitely generated

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.6, pages 448-452. Proposition 14.6.1, Theorem 14.6.5.

# Verification Notes

- Definition source: Direct from Artin, Proposition 14.6.1
- Confidence rationale: Explicitly characterized
- Uncertainties: None
- Cross-reference status: Verified
