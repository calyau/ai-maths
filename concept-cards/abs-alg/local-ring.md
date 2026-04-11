---
concept: Local Ring
slug: local-ring
category: commutative-algebra
subcategory: ring-structures
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 707
section: "15.4 Localization"
extraction_confidence: high
aliases:
  - "local domain"
prerequisites:
  - ring
  - maximal-ideal
extends: []
related:
  - localization
  - discrete-valuation-ring
contrasts_with: []
answers_questions:
  - "What is a local ring?"
---

# Quick Definition
A commutative ring with exactly one maximal ideal is called a local ring. The localization R_P of any ring at a prime P is a local ring.

# Core Definition
A commutative ring R is a **local ring** if it has a unique maximal ideal M. The localization R_P at any prime ideal P is a local ring with unique maximal ideal P·R_P. Elements outside M are units in a local ring.

# Prerequisites
- **ring** — Local rings are commutative rings with 1
- **maximal-ideal** — Having a unique maximal ideal defines the property

# Key Properties
1. Elements not in the maximal ideal are units
2. R_P is always a local ring for any prime P
3. Nakayama's Lemma applies to modules over local rings

# Relationships
## Builds Upon
- **localization** — Localizing at a prime always gives a local ring

## Enables
- **discrete-valuation-ring** — DVRs are local PIDs

# Source Reference
Chapter 15, Section 15.4, pages 707-708.

# Verification Notes
- Confidence: HIGH — well-established concept
