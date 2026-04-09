---
# === CORE IDENTIFICATION ===
concept: Groups with Operators (A-Groups)
slug: a-group-operators

# === CLASSIFICATION ===
category: groups-with-operators
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 95
section: "Groups with operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - A-group
  - group with operators

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - automorphism
extends: []
related:
  - admissible-subgroup
  - admissible-homomorphism
  - jordan-holder-for-a-groups
  - krull-schmidt-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group with operators?"
  - "How does the theory of A-groups generalize ordinary group theory?"
---

# Quick Definition

An A-group is a group G together with a homomorphism phi: A -> Aut(G) from a group A to the automorphism group of G. This framework unifies ordinary group theory, the theory of normal subgroups (A = G acting by conjugation), and the theory of characteristic subgroups (A = Aut(G)).

# Core Definition

Let A be a group. A pair (G, phi) consisting of a group G together with a homomorphism phi: A -> Aut(G) is called an *A-group*, or G is said to have A as a *group of operators*.

Write ^alpha x for phi(alpha)(x). Then:
(a) ^{alpha beta} x = ^alpha(^beta x)
(b) ^alpha(xy) = ^alpha x * ^alpha y
(c) ^1 x = x

Conversely, a map (alpha, x) -> ^alpha x : A x G -> G satisfying (a), (b), (c) arises from a homomorphism A -> Aut(G).

(Milne, p. 95-96)

# Prerequisites

- **group** -- G is a group
- **automorphism** -- Aut(G) is the target of phi

# Key Properties

1. Ordinary groups are A-groups with A = {1} (all subgroups/homomorphisms admissible)
2. G with A = G acting by conjugation: admissible subgroups are normal subgroups
3. G with A = Aut(G): admissible subgroups are characteristic subgroups
4. The isomorphism theorems hold for A-groups (with admissibility checked)
5. The Jordan-Holder theorem holds for A-groups

# Examples

**Example 1** (p. 96, 6.25a): A = {1}. All subgroups and homomorphisms are admissible. This is ordinary group theory.

**Example 2** (p. 96, 6.25b): A = G acting by conjugation (g -> i_g). Admissible subgroups = normal subgroups.

**Example 3** (p. 96, 6.25c): A = Aut(G). Admissible subgroups = characteristic subgroups.

# Relationships

## Enables
- **admissible-subgroup** -- subgroups invariant under the operators
- **admissible-homomorphism** -- homomorphisms compatible with operators
- **jordan-holder-for-a-groups** -- Jordan-Holder generalizes to A-groups
- **krull-schmidt-theorem** -- also generalizes to A-groups

# Source Reference

Chapter 6, pp. 95-96. Examples 6.25.

# Verification Notes

- Definition source: Direct from p. 95-96
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
