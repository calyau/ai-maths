---
# === CORE IDENTIFICATION ===
concept: Left Coset
slug: left-coset

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lagrange's Theorem"
chapter_number: 11
pdf_page: 64
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "left translate"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - group
extends: []
related:
  - right-coset
  - lagrange-theorem
  - left-coset-as-equivalence-class
  - partition
contrasts_with:
  - right-coset

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a coset?"
  - "How do subgroups relate to the parent group's order (Lagrange's theorem)?"
---

# Quick Definition

Given a subgroup $H$ of a group $G$ and an element $g \in G$, the left coset of $H$ determined by $g$ is the set $gH = \{gh \mid h \in H\}$, obtained by multiplying every element of $H$ on the left by $g$.

# Core Definition

Armstrong introduces left cosets in the proof of Lagrange's theorem. Given a subgroup $H$ of $G$, one chooses an element $g_1$ outside $H$ and forms $g_1H = \{g_1h \mid h \in H\}$. This set has the same size as $H$ (via the bijection $h \to g_1h$) and is disjoint from $H$ (Armstrong, Ch. 11, p. 64). In Chapter 12, the left coset is recharacterised as the equivalence class of $g$ under the relation $(x,y) \in \mathcal{R}$ iff $y^{-1}x \in H$ (Armstrong, Ch. 12, p. 68).

# Prerequisites

- **Subgroup** — Left cosets are defined relative to a subgroup $H$ of $G$
- **Group** — The ambient group $G$ provides the multiplication used to form cosets

# Key Properties

1. Every left coset $gH$ has the same cardinality as $H$ (the map $h \mapsto gh$ is a bijection)
2. Two left cosets are either identical or disjoint
3. The distinct left cosets of $H$ in $G$ form a partition of $G$
4. The coset $eH = H$ is the subgroup itself
5. $g_1H = g_2H$ if and only if $g_1^{-1}g_2 \in H$ (Exercise 11.2)

# Construction / Recognition

## To Construct:
1. Start with a subgroup $H$ of $G$ and an element $g \in G$
2. Multiply every element of $H$ on the left by $g$
3. The resulting set $\{gh \mid h \in H\}$ is the left coset $gH$

## To Recognize:
1. Check that the set has the form $gH$ for some $g$ and subgroup $H$
2. Verify all elements share a common "left factor" modulo $H$

# Context & Application

Left cosets are the fundamental tool in the proof of Lagrange's theorem: they partition $G$ into equal-sized pieces, each the same size as $H$. This forces $|H|$ to divide $|G|$. Left cosets also arise as the elements of quotient groups when $H$ is a normal subgroup.

# Examples

**Example 1** (p. 64): In $S_3$ with $H = \{\varepsilon, (13)\}$, choosing $g_1 = (123)$ gives $g_1H = \{(123), (23)\}$. Choosing $g_2 = (12)$ gives $g_2H = \{(12), (132)\}$. The three cosets $H$, $g_1H$, $g_2H$ partition $S_3$.

# Relationships

## Builds Upon
- **Subgroup** — Cosets are defined relative to a subgroup
- **Group** — Multiplication in the ambient group forms the coset

## Enables
- **Lagrange's theorem** — The coset partition yields the divisibility result
- **Quotient group** — Left cosets of a normal subgroup form a group
- **Index of a subgroup** — The number of distinct left cosets

## Related
- **Left coset as equivalence class** — Cosets arise from an equivalence relation
- **Partition** — Distinct left cosets partition $G$

## Contrasts With
- **Right coset** — Formed by multiplying on the right: $Hg = \{hg \mid h \in H\}$

# Common Errors

- **Error**: Assuming $gH = Hg$ for all subgroups $H$
  **Correction**: Left and right cosets coincide only when $H$ is a normal subgroup of $G$

- **Error**: Treating $gH$ as a subgroup of $G$
  **Correction**: A coset $gH$ is a subgroup only when $g \in H$ (in which case $gH = H$)

# Common Confusions

- **Confusion**: Believing a coset depends on the choice of representative
  **Clarification**: If $g_1H = g_2H$, then both $g_1$ and $g_2$ determine the same coset. The coset is a set, not a pair (element, subgroup)

# Source Reference

Chapter 11: Lagrange's Theorem, pp. 64-67 (pdf). Also Chapter 12: Partitions, Example (iii), pp. 68-69.

# Verification Notes

- Definition source: Direct from pp. 64-65, proof of Lagrange's theorem
- Equivalence relation characterisation: From Ch. 12, Example (iii)
- Confidence rationale: HIGH — explicitly defined and used extensively
- Cross-references: All slugs verified against planned extractions
- Uncertainties: None
