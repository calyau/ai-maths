---
# === CORE IDENTIFICATION ===
concept: Group of Symmetries
slug: group-of-symmetries

# === CLASSIFICATION ===
category: group-fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 8
section: "Definitions and examples"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Sym(S)"
  - symmetry group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - symmetric-group
  - dihedral-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the group of symmetries of a set?"
  - "What is Sym(S)?"
---

# Quick Definition

For any set S, the group of symmetries Sym(S) is the group of all bijections from S to S under composition. The symmetric group S_n is the special case where S = {1, ..., n}.

# Core Definition

Let S be a set and let Sym(S) be the set of bijections S -> S. The product of two elements is their composite: alpha * beta = alpha composed with beta. Associativity follows from the associativity of function composition, the identity map is the neutral element, and inverses exist because elements are bijections. Therefore Sym(S) is a group, called the **group of symmetries** of S (Example 1.4, p. 8).

# Prerequisites

- **Group** — Sym(S) is a group

# Key Properties

1. Elements are bijections S -> S
2. Operation is composition of functions
3. Neutral element is the identity map
4. When S is finite with |S| = n, |Sym(S)| = n!
5. Sym(S) is the "largest" group acting on S

# Construction / Recognition

## To Construct:
1. Take any set S
2. Collect all bijections S -> S
3. Define multiplication as composition

# Context & Application

Milne opens the text with "Group theory is the study of symmetries" (p. 6). The group of symmetries Sym(S) provides the universal framework: any group can be embedded in some Sym(S) (Cayley's theorem). The concept generalizes from abstract sets to geometric objects, where the "symmetries" preserve additional structure.

# Examples

**Example 1** (p. 8, 1.4): Sym({1, ..., n}) = S_n, the symmetric group on n letters, has order n!.

**Example 2** (p. 12, 1.17): The symmetries of a regular n-gon form D_n, a subgroup of Sym({vertices}).

# Relationships

## Builds Upon
- **group** — Sym(S) is a group

## Enables
- **symmetric-group** — S_n = Sym({1, ..., n})
- **dihedral-group** — D_n is a subgroup of Sym({1, ..., n})

# Common Confusions

- **Confusion**: Confusing Sym(S) with the symmetries of a geometric object
  **Clarification**: Sym(S) is the group of all bijections of the set S; geometric symmetry groups are subgroups of Sym(S) that preserve additional structure

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.4, page 8.

# Verification Notes

- Definition source: Direct from 1.4, p. 8
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
- Cross-reference status: Verified against planned cards
