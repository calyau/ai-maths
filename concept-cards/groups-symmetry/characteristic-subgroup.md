---
# === CORE IDENTIFICATION ===
concept: Characteristic Subgroup
slug: characteristic-subgroup

# === CLASSIFICATION ===
category: automorphisms
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Automorphisms"
chapter_number: 23
pdf_page: 138
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism
  - normal-subgroup
extends:
  - normal-subgroup
related:
  - centre-of-a-group
  - commutator-subgroup
contrasts_with:
  - normal-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a characteristic subgroup?"
  - "How does a characteristic subgroup differ from a normal subgroup?"
---

# Quick Definition

A characteristic subgroup of G is a subgroup that is invariant under every automorphism of G. Every characteristic subgroup is normal, but not every normal subgroup is characteristic.

# Core Definition

"A subgroup H of G is called a characteristic subgroup of G if H is sent to itself by every automorphism of G" (Armstrong, Exercise 23.5, p. 138). This is a stronger condition than normality, which only requires invariance under inner automorphisms.

# Prerequisites

- **Automorphism** -- Characteristic subgroups must be invariant under all automorphisms, not just inner ones
- **Normal subgroup** -- Every characteristic subgroup is normal, since inner automorphisms are automorphisms

# Key Properties

1. A characteristic subgroup is invariant under every automorphism of G (not just inner ones)
2. Every characteristic subgroup is normal (since inner automorphisms are automorphisms)
3. The centre Z(G) is a characteristic subgroup (Exercise 23.5)
4. The commutator subgroup [G, G] is a characteristic subgroup (Exercise 23.5)
5. Not every normal subgroup is characteristic (Exercise 23.6)

# Construction / Recognition

## To Verify a Subgroup is Characteristic
1. Take an arbitrary automorphism theta of G
2. Show that theta(H) is contained in H for every such theta
3. Since theta^{-1} is also an automorphism, this implies theta(H) = H

# Context & Application

Armstrong introduces characteristic subgroups in the exercises of Chapter 23. The concept refines the notion of normality: normal subgroups are invariant under conjugation, while characteristic subgroups are invariant under all automorphisms. This stronger condition is useful for proving that certain subgroups remain normal when embedded in larger groups.

# Examples

**Example 1** (Exercise 23.5, p. 138): The centre Z(G) is characteristic because any automorphism theta preserves commutativity: if z commutes with all elements, then theta(z) commutes with all elements.

**Example 2** (Exercise 23.5, p. 138): The commutator subgroup [G, G] is characteristic because automorphisms send commutators to commutators.

**Example 3** (Exercise 23.6, p. 138): There exist normal subgroups that are not characteristic. Armstrong asks the reader to supply such an example.

# Relationships

## Builds Upon
- **Normal subgroup** -- Characteristic is a stronger condition than normal

## Related
- **Centre of a group** -- Z(G) is always characteristic
- **Commutator subgroup** -- [G, G] is always characteristic

## Contrasts With
- **Normal subgroup** -- A normal subgroup need only be invariant under inner automorphisms; a characteristic subgroup must be invariant under all automorphisms

# Common Errors

- **Error**: Assuming every normal subgroup is characteristic
  **Correction**: Normal subgroups are only invariant under inner automorphisms; there exist normal subgroups sent to different subgroups by outer automorphisms

# Common Confusions

- **Confusion**: Thinking characteristic and normal are equivalent for abelian groups
  **Clarification**: Even in abelian groups (where every subgroup is normal), not all subgroups need be characteristic

# Source Reference

Chapter 23: Automorphisms, Exercises 23.5-23.7, pages 136-137 (pdf pp. 143-144).

# Verification Notes

- Definition: Directly quoted from Exercise 23.5
- Properties: Items 3-4 from Exercise 23.5; item 5 from Exercise 23.6
- Confidence: HIGH -- explicit definition in exercise text
- Cross-references: Verified against planned extractions
- Uncertainties: None
