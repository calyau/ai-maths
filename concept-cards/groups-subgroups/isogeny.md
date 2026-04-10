---
# === CORE IDENTIFICATION ===
concept: Isogeny
slug: isogeny

# === CLASSIFICATION ===
category: algebraic-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 15
section: "Introductory overview"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - affine-algebraic-group
extends: []
related:
  - almost-simple-algebraic-group
  - almost-direct-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An isogeny of algebraic groups is a surjective homomorphism G -> H with finite kernel. Two groups are isogenous if there exist isogenies H_1 <- G -> H_2. This is an equivalence relation.

# Core Definition

An **isogeny** of algebraic groups is a surjective homomorphism G -> H with finite kernel (p. 15). Two algebraic groups H_1 and H_2 are **isogenous** if there exist isogenies H_1 <- G -> H_2. This is an equivalence relation.

Isogeny is the appropriate notion of equivalence for almost-simple groups: over an algebraically closed field, every almost-simple group is isogenous to exactly one group on the list A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2 (p. 15).

# Prerequisites

- **Affine algebraic group** — Isogenies are morphisms between algebraic groups

# Key Properties

1. Surjective + finite kernel
2. Defines an equivalence relation on algebraic groups
3. Almost-simple groups are classified up to isogeny by Dynkin diagrams
4. An almost-direct product is defined using isogeny (p. 15)

# Examples

**Example 1** (p. 15): The map SL_n -> PSL_n = SL_n/Z (where Z is the centre) is an isogeny with kernel Z (a finite group of nth roots of unity).

# Relationships

## Related
- **Almost-simple algebraic group** — Classified up to isogeny
- **Almost-direct product** — Defined using the notion of isogeny

# Source Reference

Chapter I, Section 1a (p. 15).

# Verification Notes

- Definition source: Direct from p. 15
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
