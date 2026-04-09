---
# === CORE IDENTIFICATION ===
concept: Normalizer and Sylow Subgroups
slug: normalizer-and-sylow

# === CLASSIFICATION ===
category: sylow-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "The Sylow Theorems; Applications"
chapter_number: 5
pdf_page: 78
section: "The Sylow theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - normalizer
extends: []
related:
  - number-of-sylow-p-subgroups
  - sylow-second-theorem
  - normalizer-condition-for-sylow
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the normalizer of a Sylow p-subgroup relate to the number of Sylow p-subgroups?"
---

# Quick Definition

The number of Sylow p-subgroups equals the index of the normalizer of any Sylow p-subgroup: s_p = (G : N_G(P)). This equals m / (N_G(P) : P) where |G| = p^r m.

# Core Definition

Let P be a Sylow p-subgroup of G. Since all Sylow p-subgroups are conjugate (Sylow II(a)), the number of conjugates of P equals

s_p = (G : N_G(P)) = |G| / |N_G(P)| = m / (N_G(P) : P).

(Milne, proof of Theorem 5.6(b), p. 79)

# Prerequisites

- **sylow-p-subgroup** -- P is a Sylow p-subgroup
- **normalizer** -- N_G(P) is the stabilizer of P under conjugation

# Key Properties

1. s_p = (G : N_G(P)) is the number of conjugates of P
2. N_G(P) is the largest subgroup of G in which P is normal
3. P is always a Sylow p-subgroup of N_G(P) (and it is the unique one, hence normal in N_G(P))
4. s_p divides m because s_p = m / (N_G(P) : P) and (N_G(P) : P) is a positive integer

# Context & Application

The normalizer of a Sylow subgroup is the key intermediary between the Sylow subgroup and the full group. Knowing N_G(P) immediately determines s_p and can reveal structural information about G.

# Examples

**Example 1** (p. 79): In the proof of Sylow II(b), s_p = (G : N_G(P)) = p^r m / |N_G(P)|. Since P is contained in N_G(P), we have |N_G(P)| = p^r * (N_G(P) : P), giving s_p = m / (N_G(P) : P).

# Relationships

## Builds Upon
- **normalizer** -- core concept
- **sylow-second-theorem** -- conjugacy gives s_p = (G : N_G(P))

## Enables
- **number-of-sylow-p-subgroups** -- the formula s_p = (G : N_G(P))
- **non-simplicity-criteria** -- bounding the normalizer constrains s_p

# Source Reference

Chapter 5, within proof of Theorem 5.6(b), p. 79.

# Verification Notes

- Definition source: From proof of 5.6(b)
- Confidence rationale: HIGH -- explicit formula in proof
- Uncertainties: None
