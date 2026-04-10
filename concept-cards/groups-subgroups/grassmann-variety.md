---
concept: Grassmann Variety
slug: grassmann-variety
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 351
section: "Brief review of algebraic geometry"
extraction_confidence: high
aliases:
  - "Grassmannian"
  - "G_d(V)"
prerequisites: []
extends: []
related:
  - flag-variety
  - parabolic-subgroup
contrasts_with: []
answers_questions:
  - "What is a Grassmann variety?"
---

# Quick Definition

The Grassmann variety G_d(V) is the projective algebraic variety parametrizing d-dimensional subspaces of a vector space V. It is a special case of a generalized flag variety.

# Core Definition

Let V be a vector space of dimension n. The **Grassmann variety** G_d(V) is the set of d-dimensional subspaces of V, equipped with a natural structure as a projective algebraic variety via the Plucker embedding into ℙ^{(n choose d)−1} (Milne, 3.2b, p. 351).

The tangent space at a point S is T_S(G_d(V)) ≅ Hom(S, V/S).

# Prerequisites

This is a foundational concept in algebraic geometry.

# Key Properties

1. Projective variety (hence complete)
2. GL_V acts transitively on it
3. Special case: G_1(V) = ℙ(V)

# Source Reference

Chapter V, Section 3a, 3.2b, page 351.

# Verification Notes

- Definition source: Direct from 3.2b
- Confidence: HIGH
- Uncertainties: None
