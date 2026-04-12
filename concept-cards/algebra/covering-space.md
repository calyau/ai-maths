---
concept: Covering Space (Branched)
slug: covering-space
category: ring-theory
subcategory: algebraic-geometry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Algebraic Geometry"
extraction_confidence: medium
aliases:
  - "branched covering"
  - "n-sheeted covering"
prerequisites:
  - riemann-surface
extends: []
related:
  - algebraic-variety
contrasts_with: []
answers_questions:
  - "What is a branched covering?"
---

# Quick Definition

An n-sheeted covering space is a continuous map pi: X -> T where every fibre has n points and pi is a local homeomorphism. A branched covering allows finitely many "branch points" where fibres may be smaller.

# Core Definition

A continuous map pi from X to T is an n-sheeted covering space if every fibre has n points and pi maps a neighborhood of each point homeomorphically to a neighborhood of its image (Artin, Definition 11.9.14, p. 370). A map is an n-sheeted branched covering if there is a finite set A of branch points such that the restriction to the complement is an n-sheeted covering (p. 370).

# Prerequisites

- **Riemann surface** -- The primary example of a branched covering

# Key Properties

1. Away from branch points, the map is a local homeomorphism
2. At branch points, fibres may have fewer than n points
3. Riemann surfaces of irreducible polynomials are branched coverings

# Examples

**Example 1** (p. 370): The Riemann surface of x^2 - t is a 2-sheeted covering, branched at t = 0.

# Relationships

## Builds Upon
- **Riemann surface** -- Riemann surfaces are branched coverings

# Source Reference

Chapter 11: Rings, Section 11.9, Definition 11.9.14, pages 370-372.

# Verification Notes

- Definition source: Direct from Definition 11.9.14
- Confidence rationale: Medium -- topological definition, not purely algebraic
- Uncertainties: None
- Cross-reference status: Verified
