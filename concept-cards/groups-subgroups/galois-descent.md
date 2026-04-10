---
# === CORE IDENTIFICATION ===
concept: Galois Descent of Affine Groups
slug: galois-descent

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 39
section: "Some basic constructions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-group
  - extension-of-scalars
extends: []
related:
  - weil-restriction-of-scalars
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

Let Omega/k be a Galois extension with group Gamma. The functor G -> G_Omega is an equivalence from affine groups over k to affine groups over Omega equipped with a continuous semilinear action of Gamma.

# Core Definition

Let Omega be a Galois extension of k with Gamma = Gal(Omega/k). A **continuous action** of Gamma on an affine group G over Omega is a continuous action of Gamma on O(G) preserving the k-algebra structure and the comultiplication (p. 39-40).

**Proposition 4.13** (p. 40): The functor G -> G_Omega from affine groups over k to affine groups over Omega equipped with a continuous action of Gamma is an equivalence of categories.

This is an immediate consequence of the equivalence for vector spaces (Proposition 4.12): V -> Omega tensor V from k-vector spaces to Omega-vector spaces with continuous Gamma-action.

# Prerequisites

- **Affine group** — Descent applies to affine groups
- **Extension of scalars** — The functor G -> G_Omega

# Key Properties

1. Equivalence of categories: groups over k <-> groups over Omega with Gamma-action
2. Foundation for the theory of forms and inner twists
3. Extends the classical result for vector spaces

# Source Reference

Chapter I, Section 4e (p. 39-40), Propositions 4.12-4.13.

# Verification Notes

- Definition source: Direct from Propositions 4.12-4.13
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
