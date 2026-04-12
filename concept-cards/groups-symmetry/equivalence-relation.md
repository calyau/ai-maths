---
# === CORE IDENTIFICATION ===
concept: Equivalence Relation
slug: equivalence-relation

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
  - set
extends: []
related:
  - partition
  - equivalence-class
  - left-coset-as-equivalence-class
  - conjugacy-equivalence-relation
  - orbit-equivalence-relation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an equivalence relation?"
  - "How are equivalence relations and partitions connected?"
---

# Quick Definition

An equivalence relation on a set $X$ is a subset $\mathcal{R}$ of $X \times X$ satisfying reflexivity, symmetry, and transitivity. Its equivalence classes form a partition of $X$.

# Core Definition

Let $X$ be a set and let $\mathcal{R}$ be a subset of the Cartesian product $X \times X$. Given two points $x$ and $y$ of $X$, we say $x$ is related to $y$ if $(x, y) \in \mathcal{R}$. If the following three properties hold, $\mathcal{R}$ is called an **equivalence relation** on $X$ (Armstrong, Ch. 12, p. 68):

- (a) Each $x \in X$ is related to itself (reflexivity)
- (b) If $x$ is related to $y$, then $y$ is related to $x$ (symmetry)
- (c) If $x$ is related to $y$ and $y$ is related to $z$, then $x$ is related to $z$ (transitivity)

# Prerequisites

- **Set** — Equivalence relations are defined on sets

# Key Properties

1. Reflexive: $(x, x) \in \mathcal{R}$ for all $x \in X$
2. Symmetric: $(x, y) \in \mathcal{R}$ implies $(y, x) \in \mathcal{R}$
3. Transitive: $(x, y) \in \mathcal{R}$ and $(y, z) \in \mathcal{R}$ imply $(x, z) \in \mathcal{R}$
4. The distinct equivalence classes form a partition of $X$ (Theorem 12.2)
5. Conversely, every partition defines an equivalence relation

# Construction / Recognition

## To Verify an Equivalence Relation:
1. Check reflexivity: is every element related to itself?
2. Check symmetry: if $x \sim y$, is $y \sim x$?
3. Check transitivity: if $x \sim y$ and $y \sim z$, is $x \sim z$?

# Context & Application

Armstrong emphasises the generality of Theorem (12.2): "The strength of (12.2) is its *generality*. It will allow us to check quickly and easily that certain decompositions of sets are partitions" (p. 69). He then demonstrates this with conjugacy classes, orbits, and braids.

# Examples

**Example 1** (p. 68): On $\mathbb{Z}$, define $(x, y) \in \mathcal{R}$ iff $x - y$ is divisible by 3. This gives three equivalence classes: multiples of 3, integers $\equiv 1 \pmod{3}$, integers $\equiv 2 \pmod{3}$.

**Example 2** (p. 69): On a group $G$, define $(x, y) \in \mathcal{R}$ iff $y^{-1}x \in H$ for a subgroup $H$. The equivalence classes are the left cosets of $H$.

**Example 3** (p. 69): On a group $G$, define $(x, y) \in \mathcal{R}$ iff $gxg^{-1} = y$ for some $g \in G$. The equivalence classes are conjugacy classes.

# Relationships

## Enables
- **Equivalence class** — Each element's equivalence class is $\mathcal{R}(x)$
- **Partition** — Equivalence classes form a partition (Theorem 12.2)
- **Left coset as equivalence class** — Cosets arise from a specific equivalence relation
- **Conjugacy equivalence relation** — Conjugacy is an equivalence relation
- **Braid group** — Defined via equivalence classes of braids

# Common Errors

- **Error**: Forgetting to check reflexivity, relying on symmetry and transitivity alone
  **Correction**: Exercise 12.5 warns that reflexivity is not redundant; the argument "pick $y$ related to $x$, then symmetry and transitivity give $(x,x) \in \mathcal{R}$" fails if no such $y$ exists

# Common Confusions

- **Confusion**: Thinking any relation that "feels like equality" is an equivalence relation
  **Clarification**: All three properties must be verified. For instance, $\{(x,y) \mid x - y \ge 0\}$ is reflexive and transitive but not symmetric (Exercise 12.1d)

# Source Reference

Chapter 12: Partitions, pp. 68-72 (pdf). Definition and Theorems (12.1), (12.2).

# Verification Notes

- Definition source: Direct from p. 68
- Confidence rationale: HIGH — explicitly defined with three named properties
- Uncertainties: None
