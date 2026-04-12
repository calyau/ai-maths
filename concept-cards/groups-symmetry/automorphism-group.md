---
# === CORE IDENTIFICATION ===
concept: Automorphism Group
slug: automorphism-group

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
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Aut(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism
  - group
extends:
  - automorphism
related:
  - inner-automorphism-group
  - symmetric-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the automorphism group of a group?"
  - "How do I compute Aut(G) for specific groups?"
---

# Quick Definition

The automorphism group Aut(G) of a group G is the group of all automorphisms of G under composition of functions. It measures the internal structural symmetry of G.

# Core Definition

"The set of all automorphisms forms a group under composition of functions which is called the automorphism group of G and written Aut(G)" (Armstrong, Ch. 23, p. 138). The group operation is composition: if theta and phi are automorphisms, their product is the composite theta composed with phi.

# Prerequisites

- **Automorphism** -- Aut(G) is the collection of all automorphisms of G
- **Group** -- Must verify the group axioms hold under composition

# Key Properties

1. Aut(G) is a subgroup of the symmetric group on the underlying set of G
2. Aut(G) always contains at least the identity automorphism
3. Inn(G) is a normal subgroup of Aut(G) (Armstrong, p. 138)
4. For abelian groups, Inn(G) is trivial so Aut(G) consists entirely of "outer" automorphisms
5. |Aut(Z_p)| = p - 1 for prime p, since Aut(Z_p) is isomorphic to R_p (Armstrong, p. 138)

# Construction / Recognition

## To Compute Aut(G)
1. Identify the generators of G
2. Determine where each generator can be sent (must go to an element of the same order that generates the appropriate subgroup)
3. Check which combinations of assignments extend to valid homomorphisms
4. Verify bijectivity for each such assignment
5. Determine the resulting group structure

# Context & Application

Armstrong computes Aut(G) for several concrete groups in Chapter 23. These computations serve both as examples and as tools for constructing semidirect products. The automorphism group is central to the structure theory: knowing Aut(G) reveals what semidirect products can be built using G.

# Examples

**Example 1** (p. 138): Aut(Z) is isomorphic to Z_2. The only automorphisms are the identity and negation.

**Example 2** (p. 138): Aut(Z_2 x Z_2) is isomorphic to S_3, since an automorphism permutes the three non-identity elements and any such permutation works.

**Example 3** (p. 138): Aut(Z_n) is isomorphic to R_n, the group of units modulo n under multiplication. The correspondence theta -> theta(1) is the isomorphism.

**Example 4** (p. 138): Aut(Z x Z) is isomorphic to GL_2(Z), the group of 2x2 integer matrices with determinant +/-1.

# Relationships

## Builds Upon
- **Automorphism** -- Aut(G) collects all automorphisms of G

## Enables
- **Semidirect product** -- Requires a homomorphism phi: J -> Aut(H)
- **Inner automorphism group** -- Inn(G) is a normal subgroup of Aut(G)

## Related
- **Symmetric group** -- Aut(G) embeds in the symmetric group on the elements of G

# Common Errors

- **Error**: Computing Aut(Z_n) as Z_n rather than R_n
  **Correction**: Aut(Z_n) consists of units modulo n, not all residues; its order is Euler's phi(n), not n

- **Error**: Assuming Aut(G x H) = Aut(G) x Aut(H) in general
  **Correction**: This holds when |G| and |H| are coprime (Exercise 23.7) but not in general

# Common Confusions

- **Confusion**: Confusing Aut(G) with Inn(G)
  **Clarification**: Inn(G) consists only of conjugation automorphisms; Aut(G) may contain additional "outer" automorphisms

# Source Reference

Chapter 23: Automorphisms, pages 131-137 (pdf pp. 138-144). Examples (i)-(vi) compute Aut(G) for Z, Z_2 x Z_2, Z_n, S_3, and Z x Z.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 138
- Examples: All directly from source text
- Confidence: HIGH -- explicit definition with extensive worked examples
- Cross-references: Verified against planned extractions
- Uncertainties: None
