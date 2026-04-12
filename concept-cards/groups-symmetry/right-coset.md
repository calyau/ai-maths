---
# === CORE IDENTIFICATION ===
concept: Right Coset
slug: right-coset

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
  - subgroup
  - equivalence-relation
extends: []
related:
  - left-coset
  - normal-subgroup
  - index-of-subgroup
contrasts_with:
  - left-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a right coset?"
  - "How do right cosets differ from left cosets?"
---

# Quick Definition

The right coset of a subgroup $H$ determined by $g$ is the set $Hg = \{hg \mid h \in H\}$, obtained by multiplying every element of $H$ on the right by $g$.

# Core Definition

If the equivalence relation is changed to the collection of ordered pairs $(x, y) \in G \times G$ for which $xy^{-1} \in H$, the equivalence class of $g$ is the *right coset* $Hg$, obtained by multiplying every element of $H$ on the right by $g$ (Armstrong, Ch. 12, p. 69).

# Prerequisites

- **Subgroup** — Right cosets are defined relative to a subgroup
- **Equivalence relation** — The right coset relation $xy^{-1} \in H$ is an equivalence relation

# Key Properties

1. $Hg = \{hg \mid h \in H\}$
2. The distinct right cosets partition $G$
3. The number of right cosets equals the number of left cosets (the index of $H$)
4. Left and right cosets coincide ($gH = Hg$ for all $g$) if and only if $H$ is normal (Theorem 15.3)

# Construction / Recognition

## To Construct:
1. Start with a subgroup $H$ and element $g \in G$
2. Multiply each element of $H$ on the right by $g$

# Context & Application

Armstrong introduces right cosets alongside left cosets in Chapter 12 and returns to them in Chapter 15, where the coincidence of left and right cosets characterises normal subgroups (Theorem 15.3).

# Examples

**Example 1** (Exercise 12.7): In $A_4$ with $H = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$, the left and right cosets coincide. With $H = \{\varepsilon, (123), (132)\}$, they do not.

# Relationships

## Builds Upon
- **Subgroup** — Right cosets require a subgroup

## Related
- **Normal subgroup** — $gH = Hg$ for all $g$ iff $H$ is normal
- **Index of a subgroup** — Number of right cosets = number of left cosets

## Contrasts With
- **Left coset** — $gH$ vs $Hg$; these coincide iff $H$ is normal

# Common Errors

- **Error**: Assuming left and right cosets always coincide
  **Correction**: They coincide precisely when $H$ is a normal subgroup

# Common Confusions

- **Confusion**: Thinking $gH = Hg$ means $gh = hg$ for all $h \in H$
  **Clarification**: $gH = Hg$ means the *sets* are equal; for each $h_1 \in H$ there exists $h_2 \in H$ with $gh_1 = h_2 g$, but $h_1$ and $h_2$ may differ

# Source Reference

Chapter 12: Partitions, Example (iii), p. 69 (pdf). Also Chapter 15: Quotient Groups, Theorem (15.3).

# Verification Notes

- Definition source: Direct from p. 69
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
