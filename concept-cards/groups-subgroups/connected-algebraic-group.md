---
# === CORE IDENTIFICATION ===
concept: Connected Algebraic Group
slug: connected-algebraic-group

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
pdf_page: 14
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
  - connected-component-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

An algebraic group G is connected if |G| is connected as a topological space, equivalently if its only finite quotient group is trivial. Every algebraic group has a unique normal connected subgroup G^0 with G/G^0 finite etale.

# Core Definition

An algebraic group is **connected** if its only finite quotient group is trivial (p. 14). Equivalently, |G| is connected as a topological space (Section 6k, p. 62).

Every algebraic group G contains a unique normal connected subgroup G^0 (the identity component) such that G/G^0 is a finite etale algebraic group (summary 1c, item (a), p. 17).

# Prerequisites

- **Affine algebraic group** — Connectedness is a property of algebraic groups

# Key Properties

1. G has a unique identity component G^0 with G/G^0 finite etale
2. When G is smooth and connected, O(G) is an integral domain (since |G| is irreducible)
3. The five building blocks (semisimple, torus, unipotent, abelian variety, finite) decompose connected groups

# Examples

**Example 1** (p. 16): O_n is not connected (det takes values +/- 1). Its identity component is SO_n.

**Example 2**: GL_n, SL_n, G_a, G_m are all connected.

# Relationships

## Related
- **Connected component group** — G^0 is the identity component

# Source Reference

Chapter I, Section 1a (p. 14), Section 1c (p. 17).

# Verification Notes

- Definition source: Direct from p. 14
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
