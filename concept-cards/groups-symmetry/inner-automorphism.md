---
# === CORE IDENTIFICATION ===
concept: Inner Automorphism
slug: inner-automorphism

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
  - conjugation automorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism
  - conjugacy
  - centre-of-a-group
extends:
  - automorphism
related:
  - inner-automorphism-group
  - normal-subgroup
contrasts_with:
  - outer-automorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an inner automorphism?"
  - "How does conjugation define an automorphism?"
---

# Quick Definition

An inner automorphism of a group G is an automorphism of the form x -> gxg^{-1} for some fixed element g in G. It is the automorphism induced by conjugation by g.

# Core Definition

"Conjugation by a fixed element g of G gives a particular type of automorphism x -> gxg^{-1} called an inner automorphism" (Armstrong, Ch. 23, p. 138). Each element g of G determines an inner automorphism, and the collection of all inner automorphisms forms a normal subgroup Inn(G) of Aut(G).

# Prerequisites

- **Automorphism** -- Inner automorphisms are a special class of automorphisms
- **Conjugacy** -- Inner automorphisms are defined via conjugation
- **Centre of a group** -- The kernel of the map g -> (x -> gxg^{-1}) is Z(G)

# Key Properties

1. For each g in G, the map x -> gxg^{-1} is an automorphism of G
2. The map G -> Aut(G) sending g to its conjugation automorphism is a homomorphism
3. The kernel of this homomorphism is the centre Z(G)
4. Inn(G) is a normal subgroup of Aut(G)
5. If G is abelian, Inn(G) is trivial (only the identity automorphism)

# Construction / Recognition

## To Construct an Inner Automorphism
1. Choose a fixed element g in G
2. Define theta_g: G -> G by theta_g(x) = gxg^{-1}
3. This is automatically an automorphism

## To Recognize an Inner Automorphism
1. Given an automorphism theta of G, check whether there exists g in G such that theta(x) = gxg^{-1} for all x
2. If such g exists, theta is inner; otherwise it is outer

# Context & Application

Inner automorphisms connect the concepts of conjugacy and automorphism theory. The theorem Inn(G) = G/Z(G) (Theorem 23.1) provides a concrete description of the inner automorphism group. This result is used in analyzing group structure and in the theory of semidirect products.

# Examples

**Example 1** (p. 138): For any abelian group, the only inner automorphism is the identity, since gxg^{-1} = x for all g, x.

**Example 2** (p. 138): In S_3, conjugation by (12) permutes the 3-cycles (123) and (132) while fixing (12). Since Z(S_3) = {e}, we have Inn(S_3) isomorphic to S_3/Z(S_3) = S_3.

# Relationships

## Builds Upon
- **Automorphism** -- An inner automorphism is a particular type of automorphism
- **Conjugacy** -- Defined via conjugation

## Enables
- **Inner automorphism group** -- Inn(G) = G/Z(G)
- **Normal subgroup** -- Normal subgroups are precisely those invariant under all inner automorphisms (Exercise 23.6)

## Contrasts With
- **Outer automorphism** -- An automorphism that is not inner

# Common Errors

- **Error**: Believing that different group elements always give different inner automorphisms
  **Correction**: Elements g and h give the same inner automorphism if and only if gh^{-1} lies in Z(G)

# Common Confusions

- **Confusion**: Thinking "inner automorphism" means any automorphism that maps a subgroup to itself
  **Clarification**: Inner automorphisms are specifically those defined by conjugation; a subgroup mapped to itself by all automorphisms is a characteristic subgroup

# Source Reference

Chapter 23: Automorphisms, Example (vii) and Theorem 23.1, page 138 (pdf p. 138).

# Verification Notes

- Definition: Directly quoted from Armstrong p. 138, Example (vii)
- Properties: Items 1-4 from Theorem 23.1 and its proof
- Confidence: HIGH -- explicit definition and theorem in source
- Cross-references: Verified against planned extractions
- Uncertainties: None
