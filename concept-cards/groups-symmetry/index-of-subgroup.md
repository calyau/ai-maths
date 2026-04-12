---
# === CORE IDENTIFICATION ===
concept: Index of a Subgroup
slug: index-of-subgroup

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Quotient Groups"
chapter_number: 15
pdf_page: 86
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "index"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
  - subgroup
extends:
  - lagrange-theorem
related:
  - right-coset
  - quotient-group
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the index of a subgroup?"
  - "How many cosets does a subgroup have?"
---

# Quick Definition

The index of a subgroup $H$ in $G$ is the number of distinct left (or right) cosets of $H$ in $G$. For finite groups, the index equals $|G|/|H|$.

# Core Definition

The *index* of a subgroup $H$ of $G$ is the number of distinct left (or right) cosets of $H$ in $G$ (Armstrong, Ch. 15, p. 88). Even if $H$ is not a normal subgroup, it does not matter which type of coset is used, since the correspondence $xH \to Hx^{-1}$ is a bijection between the set of left cosets and the set of right cosets.

# Prerequisites

- **Left coset** — The index counts the number of distinct left cosets
- **Subgroup** — The index is defined for a subgroup within a group

# Key Properties

1. The number of left cosets equals the number of right cosets
2. For finite groups, the index equals $|G|/|H|$ by Lagrange's theorem
3. A subgroup of index 2 is always normal (Theorem 15.4)
4. If $H$ is normal, the index equals the order of the quotient group $G/H$

# Construction / Recognition

## To Compute:
1. For finite groups: divide $|G|$ by $|H|$
2. For infinite groups: enumerate the distinct cosets

# Context & Application

The index provides a bridge between Lagrange's theorem and quotient groups. The special case of index 2 is particularly important: Armstrong proves (Theorem 15.4) that any subgroup of index 2 is automatically normal, yielding immediate examples like $A_n \triangleleft S_n$ and $SO_n \triangleleft O_n$.

# Examples

**Example 1** (p. 64): $H = \{\varepsilon, (13)\}$ in $S_3$ has index 3 since there are three distinct left cosets.

**Example 2** (p. 88): $A_n$ has index 2 in $S_n$, so $A_n$ is normal in $S_n$.

# Relationships

## Builds Upon
- **Lagrange's theorem** — For finite groups, index = $|G|/|H|$

## Enables
- **Quotient group** — The order of $G/H$ equals the index of $H$
- **Normal subgroup** — Index-2 subgroups are always normal

## Related
- **Right coset** — The number of right cosets equals the number of left cosets

# Common Errors

- **Error**: Computing the index using only left cosets and assuming right cosets give a different count
  **Correction**: The bijection $xH \to Hx^{-1}$ guarantees equal counts

# Common Confusions

- **Confusion**: Thinking the index is only defined for normal subgroups
  **Clarification**: The index is defined for any subgroup; normality is only needed to form a quotient group from the cosets

# Source Reference

Chapter 15: Quotient Groups, p. 88 (pdf). Also implicit in Chapter 11 (Lagrange's Theorem).

# Verification Notes

- Definition source: Direct from Ch. 15, p. 88
- Confidence rationale: HIGH — explicitly defined
- Cross-references: Verified against planned extractions
- Uncertainties: None
