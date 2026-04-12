---
# === CORE IDENTIFICATION ===
concept: Free Product
slug: free-product

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: "Exercises"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "G * H"
  - coproduct of groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-group
  - group
extends:
  - free-group
related:
  - direct-product
  - presentation-of-a-group
contrasts_with:
  - direct-product

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the free product of two groups?"
  - "How does a free product differ from a direct product?"
---

# Quick Definition

The free product G * H of groups G and H consists of reduced words with factors alternating between elements of G and H (neither being the identity). It is the "freest" group containing both G and H as subgroups.

# Core Definition

"If G and H are groups we can form words x_1 x_2 ... x_n where each x_i lies in the disjoint union G union H. Call a word reduced this time if x_i and x_{i+1} never belong to the same group and if x_i is never the identity of G or H. Throw in the empty word, and agree to multiply reduced words by juxtaposition, reducing the product as necessary. Show that the result is a group. This group is called the free product G * H of G and H" (Armstrong, Exercise 27.11, p. 178).

# Prerequisites

- **Free group** -- Free products generalize the free group construction
- **Group** -- G and H are groups

# Key Properties

1. Elements are reduced words alternating between G-factors and H-factors
2. Both G and H embed as subgroups of G * H
3. No relations hold between elements of G and elements of H
4. Z * Z is isomorphic to F_2 (Exercise 27.13)
5. Z_2 * Z_2 is isomorphic to the infinite dihedral group (Exercise 27.14)
6. Universal property (Exercise 27.12): G * H is characterized by extending pairs of homomorphisms from G and H to a single homomorphism

# Construction / Recognition

## To Form the Free Product G * H
1. Take the disjoint union of G and H as the alphabet
2. Form words x_1 x_2 ... x_n with x_i in G union H
3. Reduce: combine adjacent factors from the same group and omit identities
4. Multiply by concatenation followed by reduction

# Context & Application

The free product is a fundamental construction in combinatorial group theory. Armstrong introduces it in the exercises and connects it to free groups (Z * Z = F_2). The free product plays a key role in the theory of groups acting on trees, developed in Chapter 28.

# Examples

**Example 1** (Exercise 27.13, p. 178): Z * Z is isomorphic to F_2, the free group on two generators.

**Example 2** (Exercise 27.14, p. 178): Z_2 * Z_2 is isomorphic to the infinite dihedral group D_infinity.

# Relationships

## Builds Upon
- **Free group** -- Free products generalize free groups

## Related
- **Presentation of a group** -- Free products can be described by presentations

## Contrasts With
- **Direct product** -- In G x H, elements of G and H commute; in G * H, they do not

# Common Errors

- **Error**: Assuming elements of G and H commute in G * H
  **Correction**: In the free product, no relations between G and H are imposed; gh and hg are generally different for g in G, h in H

# Common Confusions

- **Confusion**: Confusing the free product with the direct product
  **Clarification**: G x H imposes commutativity between G and H factors; G * H imposes no such relations. G * H is typically much larger than G x H

# Source Reference

Chapter 27: Free Groups and Presentations, Exercises 27.11-27.14, pages 178-179 (pdf pp. 178-179).

# Verification Notes

- Definition: Directly quoted from Exercise 27.11
- Confidence: HIGH -- explicit definition in exercise
- Cross-references: Verified against planned extractions
- Uncertainties: None
