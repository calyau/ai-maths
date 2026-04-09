---
# === CORE IDENTIFICATION ===
concept: "Frattini's Argument"
slug: frattinis-argument

# === CLASSIFICATION ===
category: nilpotent-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 95
section: "Nilpotent groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-second-theorem
  - normal-subgroup
  - normalizer
extends: []
related:
  - maximal-subgroups-of-nilpotent-groups
  - nilpotent-iff-direct-product-of-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Frattini's argument?"
  - "How does it connect Sylow subgroups of normal subgroups to the full group?"
---

# Quick Definition

If H is a normal subgroup of G and P is a Sylow p-subgroup of H, then G = H * N_G(P). This is because every conjugate of P in G is also a conjugate within H, so the normalizer of P in G "covers" the remaining cosets.

# Core Definition

**Proposition 6.22 (Frattini's Argument).** Let H be a normal subgroup of a finite group G, and let P be a Sylow p-subgroup of H. Then G = H * N_G(P).

Proof: For g in G, gPg^{-1} is contained in gHg^{-1} = H, so gPg^{-1} is a Sylow p-subgroup of H. By Sylow II, hPh^{-1} = gPg^{-1} for some h in H, so h^{-1}g is in N_G(P), giving g in H * N_G(P).

(Milne, Proposition 6.22, p. 95)

# Prerequisites

- **sylow-second-theorem** -- conjugacy of Sylow subgroups within H
- **normal-subgroup** -- H must be normal in G
- **normalizer** -- N_G(P) is the key subgroup

# Key Properties

1. The argument works for any Sylow p-subgroup of any normal subgroup
2. It shows G/H is isomorphic to N_G(P)/(H intersect N_G(P))
3. This is used in the proof that nilpotent groups have all maximal subgroups normal (Theorem 6.23)

# Context & Application

Frattini's argument is a standard technique in group theory for "factoring" a group through the normalizer of a Sylow subgroup. It is used in the proof that a finite group is nilpotent iff every maximal proper subgroup is normal.

# Relationships

## Builds Upon
- **sylow-second-theorem** -- conjugacy in H

## Enables
- **maximal-subgroups-of-nilpotent-groups** -- used in the proof of Theorem 6.23

# Source Reference

Chapter 6, Proposition 6.22, p. 95.

# Verification Notes

- Definition source: Direct from Proposition 6.22
- Confidence rationale: HIGH -- explicit proposition with proof
- Uncertainties: None
