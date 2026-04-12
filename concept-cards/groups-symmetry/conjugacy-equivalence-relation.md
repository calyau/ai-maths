---
# === CORE IDENTIFICATION ===
concept: Conjugacy as Equivalence Relation
slug: conjugacy-equivalence-relation

# === CLASSIFICATION ===
category: equivalence-partitions
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Partitions"
chapter_number: 12
pdf_page: 68
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - equivalence-relation
  - group
extends:
  - equivalence-relation
related:
  - conjugacy-class
  - conjugation-by-g
  - partition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do conjugacy classes partition a group?"
  - "Why is conjugacy an equivalence relation?"
---

# Quick Definition

Conjugacy is an equivalence relation on a group $G$: elements $x$ and $y$ are conjugate if $gxg^{-1} = y$ for some $g \in G$. The equivalence classes (conjugacy classes) partition $G$.

# Core Definition

Let $x, y$ be elements of a group $G$. We say $x$ is **conjugate** to $y$ if $gxg^{-1} = y$ for some $g \in G$. Armstrong verifies this is an equivalence relation (Ch. 12, Example (iv), pp. 69-70):

- Reflexivity: $exe^{-1} = x$
- Symmetry: if $gxg^{-1} = y$, then $g^{-1}yg = x$
- Transitivity: if $g_1xg_1^{-1} = y$ and $g_2yg_2^{-1} = z$, then $(g_2g_1)x(g_2g_1)^{-1} = z$

# Prerequisites

- **Equivalence relation** — Conjugacy is verified to satisfy the three properties
- **Group** — Conjugacy uses the group operation and inverses

# Key Properties

1. Conjugacy is reflexive, symmetric, and transitive
2. The equivalence classes (conjugacy classes) partition $G$
3. In an abelian group, each conjugacy class is a singleton
4. Conjugate elements have the same order

# Construction / Recognition

## To Verify Two Elements Are Conjugate:
1. Given $x, y \in G$, search for $g \in G$ with $gxg^{-1} = y$
2. If such $g$ exists, $x$ and $y$ are conjugate

# Context & Application

Armstrong introduces conjugacy in Chapter 12 as an application of the general partition theorem, then works out the conjugacy classes of specific groups in Chapter 14. The conjugacy partition is essential for defining normal subgroups in Chapter 15.

# Examples

**Example 1** (p. 69): The verification that conjugacy is an equivalence relation, with the transitivity calculation $(g_2g_1)x(g_2g_1)^{-1} = g_2(g_1xg_1^{-1})g_2^{-1} = g_2yg_2^{-1} = z$.

# Relationships

## Builds Upon
- **Equivalence relation** — Conjugacy is a specific equivalence relation

## Enables
- **Conjugacy class** — The equivalence classes of conjugacy
- **Normal subgroup** — Defined as a union of conjugacy classes
- **Centre of a group** — Elements whose conjugacy class is a singleton

# Common Errors

- **Error**: Checking only symmetry and transitivity, not reflexivity
  **Correction**: Reflexivity ($exe^{-1} = x$) must also be verified, though it is straightforward here

# Common Confusions

- **Confusion**: Thinking "conjugate" means "equal"
  **Clarification**: Conjugate elements are related by a group element but are generally distinct. They are equal only when the conjugating element commutes with them.

# Source Reference

Chapter 12: Partitions, Example (iv), pp. 69-70 (pdf).

# Verification Notes

- Definition source: Direct from Example (iv), pp. 69-70
- Confidence rationale: HIGH — explicit verification of all three properties
- Uncertainties: None
