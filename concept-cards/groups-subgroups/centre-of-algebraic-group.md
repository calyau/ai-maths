---
# === CORE IDENTIFICATION ===
concept: Centre of an Algebraic Group
slug: centre-of-algebraic-group

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Basic Theory of Affine Groups"
chapter_number: 1
pdf_page: 84
section: "Group theory: subgroups and quotient groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Z(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - centralizer
extends:
  - centralizer
related:
  - normalizer
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine algebraic group?"
---

# Quick Definition

The centre Z(G) of an affine group G is the centralizer C_G(G), i.e., the affine subgroup of elements commuting with all of G. It is always a normal affine subgroup.

# Core Definition

The **centre** Z(G) of an affine group G is defined to be C_G(G) (p. 84). It is an affine subgroup of G, and if G is algebraic and G(k') is dense in G, then Z(G)(k) = G(k) intersected with Z(G(k')).

# Prerequisites

- **Centralizer** — Z(G) is a special case of the centralizer

# Key Properties

1. Z(G) is always a normal affine subgroup of G
2. Even when G is smooth, Z(G) need not be smooth (7.47)
3. Z(GL_n) = G_m (Example 7.48)
4. Z(SL_p) = mu_p in characteristic p

# Examples

**Example 1** (p. 84): Z(GL_n) = G_m, the group of scalar matrices.

**Example 2** (p. 84): Z(SL_p) = mu_p in characteristic p, which is not smooth.

# Relationships

## Extends
- **Centralizer** — Z(G) = C_G(G)

# Source Reference

Chapter I, Section 7f (p. 84).

# Verification Notes

- Definition source: Direct from p. 84
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
