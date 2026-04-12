---
# === CORE IDENTIFICATION ===
concept: Left Coset as Equivalence Class
slug: left-coset-as-equivalence-class

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
  - left-coset
  - subgroup
extends:
  - equivalence-class
related:
  - right-coset
  - lagrange-theorem
  - partition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are left cosets related to equivalence relations?"
  - "Why do left cosets form a partition?"
---

# Quick Definition

The left coset $gH$ is the equivalence class of $g$ under the relation $(x, y) \in \mathcal{R}$ iff $y^{-1}x \in H$. This provides a conceptual explanation for why left cosets partition $G$.

# Core Definition

Let $H$ be a subgroup of $G$ and let $\mathcal{R}$ be the collection of ordered pairs $(x, y)$ with entries from $G$ for which $y^{-1}x \in H$. Armstrong verifies (Ch. 12, Example (iii), p. 69):

- Reflexivity: $x^{-1}x = e \in H$
- Symmetry: if $y^{-1}x \in H$, then $x^{-1}y = (y^{-1}x)^{-1} \in H$
- Transitivity: if $y^{-1}x, z^{-1}y \in H$, then $z^{-1}x = (z^{-1}y)(y^{-1}x) \in H$

The equivalence class $\mathcal{R}(g)$ consists of all $x \in G$ with $g^{-1}x \in H$, i.e., $x = gh$ for some $h \in H$. So $\mathcal{R}(g) = gH$, the left coset.

# Prerequisites

- **Equivalence relation** — The coset partition arises from an equivalence relation
- **Left coset** — The concept being recharacterised
- **Subgroup** — $H$ must be a subgroup for the relation to be an equivalence relation

# Key Properties

1. The relation $y^{-1}x \in H$ is an equivalence relation on $G$
2. The equivalence class of $g$ is exactly $gH$
3. By Theorem (12.2), the distinct left cosets partition $G$
4. This gives a cleaner proof that cosets partition $G$ than the direct argument in Ch. 11

# Construction / Recognition

## To Verify:
1. Define $(x, y) \in \mathcal{R}$ iff $y^{-1}x \in H$
2. Check reflexivity, symmetry, transitivity (using subgroup properties)
3. Identify $\mathcal{R}(g) = gH$
4. Apply Theorem (12.2) to conclude cosets partition $G$

# Context & Application

Armstrong presents this as the "right" way to understand why Lagrange's theorem works. The equivalence relation framework replaces the ad hoc argument of Chapter 11 with a general principle. As Armstrong notes: "The strength of (12.2) is its generality" (p. 69).

# Examples

**Example 1** (p. 69): In $A_4$ with $H = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$, the left cosets $\varepsilon H$, $(123)H$, $(132)H$ partition $A_4$ into three sets of four elements each.

# Relationships

## Builds Upon
- **Equivalence relation** — The coset relation is an equivalence relation
- **Left coset** — Reinterpreted as an equivalence class

## Enables
- **Lagrange's theorem** — Provides the partition needed for the proof

## Related
- **Right coset** — Similarly arises from the relation $xy^{-1} \in H$

# Common Errors

- **Error**: Using the wrong relation ($xy^{-1} \in H$ instead of $y^{-1}x \in H$)
  **Correction**: $y^{-1}x \in H$ gives left cosets; $xy^{-1} \in H$ gives right cosets

# Common Confusions

- **Confusion**: Thinking the equivalence relation approach is just a reformulation with no added value
  **Clarification**: The equivalence relation framework is much more general; it also handles conjugacy classes, orbits, and braids, where direct partition arguments would be more difficult

# Source Reference

Chapter 12: Partitions, Example (iii), p. 69 (pdf).

# Verification Notes

- Definition source: Direct from Example (iii), p. 69
- Confidence rationale: HIGH — explicit verification of equivalence relation properties
- Uncertainties: None
