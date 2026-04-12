---
# === CORE IDENTIFICATION ===
concept: Inner Automorphism Group
slug: inner-automorphism-group

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
  - "Inn(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - inner-automorphism
  - automorphism-group
  - centre-of-a-group
  - first-isomorphism-theorem
extends:
  - inner-automorphism
related:
  - quotient-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Inn(G) and how is it related to G/Z(G)?"
  - "Why is Inn(G) a normal subgroup of Aut(G)?"
---

# Quick Definition

The inner automorphism group Inn(G) is the subgroup of Aut(G) consisting of all inner automorphisms. It is isomorphic to the quotient group G/Z(G), where Z(G) is the centre of G.

# Core Definition

"The inner automorphisms form a normal subgroup Inn(G) of Aut(G)" (Armstrong, Ch. 23, p. 138). Theorem 23.1 establishes that "Inn(G) is isomorphic to the quotient group G/Z(G)." The proof proceeds by observing that the function from G to Aut(G) sending each g to the inner automorphism x -> gxg^{-1} is a homomorphism whose image is Inn(G) and whose kernel is Z(G), then applying the First Isomorphism Theorem (Armstrong, p. 138).

# Prerequisites

- **Inner automorphism** -- Inn(G) consists of all inner automorphisms
- **Automorphism group** -- Inn(G) is a subgroup of Aut(G)
- **Centre of a group** -- Z(G) is the kernel of the conjugation homomorphism
- **First Isomorphism Theorem** -- Used to establish Inn(G) = G/Z(G)

# Key Properties

1. Inn(G) is a normal subgroup of Aut(G)
2. Inn(G) is isomorphic to G/Z(G) (Theorem 23.1)
3. Inn(G) is trivial if and only if G is abelian
4. The quotient Aut(G)/Inn(G) is called the outer automorphism group
5. If Z(G) = {e}, then G is isomorphic to Inn(G)

# Construction / Recognition

## To Compute Inn(G)
1. Identify the centre Z(G)
2. Form the quotient G/Z(G)
3. Inn(G) is isomorphic to this quotient

# Context & Application

The isomorphism Inn(G) = G/Z(G) is a fundamental structural result connecting the internal symmetries of a group to its centre. Armstrong proves this as Theorem 23.1 and uses it implicitly when analyzing semidirect products and the Euclidean group.

# Examples

**Example 1** (p. 138): For abelian groups, Z(G) = G, so Inn(G) = G/G = {e} -- only the identity automorphism is inner.

**Example 2** (p. 138): For S_3, Z(S_3) = {e}, so Inn(S_3) is isomorphic to S_3/{e} = S_3. Since Aut(S_3) is also isomorphic to S_3, every automorphism of S_3 is inner.

# Relationships

## Builds Upon
- **Inner automorphism** -- Inn(G) is the collection of all inner automorphisms
- **Automorphism group** -- Inn(G) is a normal subgroup of Aut(G)

## Enables
- **Outer automorphism group** -- Defined as Aut(G)/Inn(G)

## Related
- **Quotient group** -- Inn(G) = G/Z(G) is a quotient group

# Common Errors

- **Error**: Computing Inn(G) by listing conjugation automorphisms without accounting for duplicates
  **Correction**: Elements g and h define the same inner automorphism iff g and h lie in the same coset of Z(G); use |Inn(G)| = |G|/|Z(G)|

# Common Confusions

- **Confusion**: Believing Inn(G) = Aut(G) always
  **Clarification**: Inn(G) may be a proper subgroup of Aut(G); the quotient Aut(G)/Inn(G) measures the "outer" automorphisms

# Source Reference

Chapter 23: Automorphisms, Theorem 23.1 and its proof, page 138 (pdf p. 138).

# Verification Notes

- Definition and theorem: Directly from Armstrong p. 138
- Proof method: First Isomorphism Theorem applied to conjugation homomorphism
- Confidence: HIGH -- explicit theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
