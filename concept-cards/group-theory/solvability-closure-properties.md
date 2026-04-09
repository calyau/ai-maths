---
# === CORE IDENTIFICATION ===
concept: Closure Properties of Solvable Groups
slug: solvability-closure-properties

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 89
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
  - solvable-series
extends:
  - solvable-group
related:
  - solvability-of-p-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is a subgroup of a solvable group solvable?"
  - "Is a quotient of a solvable group solvable?"
  - "Is an extension of solvable groups solvable?"
---

# Quick Definition

Solvability is preserved by taking subgroups, quotients, and extensions: subgroups and quotients of solvable groups are solvable, and if N and G/N are both solvable, then G is solvable.

# Core Definition

**Proposition 6.6.**
(a) Every subgroup and every quotient group of a solvable group is solvable.
(b) An extension of solvable groups is solvable: if N is normal in G with N and G/N both solvable, then G is solvable.

(Milne, Proposition 6.6, pp. 89-90)

# Prerequisites

- **solvable-group** -- the property being studied

# Key Properties

1. For subgroups: if G > G_1 > ... > G_n is solvable, then H > H intersect G_1 > ... > H intersect G_n is solvable for H (quotients inject into the abelian groups G_i/G_{i+1})
2. For quotients: images of a solvable series give a solvable series
3. For extensions: splice the solvable series of G/N with that of N

# Context & Application

These closure properties make solvability a very robust condition. In particular, (b) is the key tool for building solvable groups: if you can find a normal subgroup N such that both N and G/N are solvable, then G is solvable.

# Examples

**Example 1** (p. 90, Corollary 6.7): A finite p-group is solvable. Proof: Z(G) != 1, G/Z(G) is solvable by induction, Z(G) is commutative, so G is solvable by part (b).

# Relationships

## Builds Upon
- **solvable-group** -- the property whose closure is established

## Enables
- **solvability-of-p-groups** -- p-groups are solvable via this result

# Source Reference

Chapter 6, Proposition 6.6, pp. 89-90.

# Verification Notes

- Definition source: Direct from Proposition 6.6
- Confidence rationale: HIGH -- explicit proposition with proof
- Uncertainties: None
