---
# === CORE IDENTIFICATION ===
concept: Conjugacy Classes of D6
slug: conjugacy-classes-of-d6

# === CLASSIFICATION ===
category: conjugacy
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Conjugacy"
chapter_number: 14
pdf_page: 80
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugacy-class
  - dihedral-group
  - conjugation-by-g
extends: []
related:
  - centre-of-a-group
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the conjugacy classes of a dihedral group?"
---

# Quick Definition

The dihedral group $D_6$ has six conjugacy classes: $\{e\}$, $\{r, r^5\}$, $\{r^2, r^4\}$, $\{r^3\}$, $\{s, r^2 s, r^4 s\}$, $\{rs, r^3 s, r^5 s\}$.

# Core Definition

Armstrong computes the conjugacy classes of $D_6$ by direct calculation (Ch. 14, Example (ii), pp. 80-81). The key computations are:

- Conjugating $r^a$ by $s$: $sr^a s = r^{6-a}$, so $r^a$ and $r^{6-a}$ are conjugate
- Conjugating $s$ by $r^b$: $r^b s r^{-b} = r^{2b} s$, producing $s, r^2 s, r^4 s$
- Conjugating $rs$ by $r^b$: $r^b(rs)r^{-b} = r^{2b+1} s$, producing $rs, r^3 s, r^5 s$

# Prerequisites

- **Conjugacy class** — The concept being computed
- **Dihedral group** — $D_6$ with relations $r^6 = e$, $s^2 = e$, $sr = r^5 s$
- **Conjugation by $g$** — The computation method

# Key Properties

1. Six conjugacy classes of sizes 1, 2, 2, 1, 3, 3 (total: 12 = $|D_6|$)
2. The centre $Z(D_6) = \{e, r^3\}$ (the two singleton classes)
3. Rotations pair up: $\{r^a, r^{6-a}\}$, except $r^3$ which is central
4. Reflections split into two classes of three, based on the parity of the exponent of $r$

# Construction / Recognition

## To Compute:
1. Use $sr^a s = r^{6-a}$ to pair rotations
2. Use $r^b s r^{-b} = r^{2b} s$ to find the class of $s$
3. Use $r^b(rs)r^{-b} = r^{2b+1} s$ to find the class of $rs$
4. Verify sizes sum to $|D_6| = 12$

# Context & Application

This is Armstrong's first detailed conjugacy class computation, serving as a model for the general dihedral group analysis (Exercise 14.2). The computation reveals that $\{e, r^3\}$ is a union of conjugacy classes and hence a normal subgroup, which Armstrong uses in Chapter 15.

# Examples

**Example 1** (p. 80): The full list: $\{e\}$, $\{r, r^5\}$, $\{r^2, r^4\}$, $\{r^3\}$, $\{s, r^2 s, r^4 s\}$, $\{rs, r^3 s, r^5 s\}$.

# Relationships

## Builds Upon
- **Dihedral group** — The group whose classes are computed
- **Conjugation by $g$** — The computational tool

## Enables
- **Normal subgroup examples** — $\{e, r^3\}$ is normal in $D_6$ (used in Ch. 15, Example (i))
- **Centre of $D_6$** — $Z(D_6) = \{e, r^3\}$

# Common Errors

- **Error**: Forgetting to conjugate by reflections $r^b s$ as well as rotations $r^b$
  **Correction**: Both types of conjugation must be checked to find the full conjugacy class

# Common Confusions

- **Confusion**: Thinking all reflections are conjugate in $D_6$
  **Clarification**: In $D_6$ (even $n$), reflections split into two classes. For $D_n$ with odd $n$, all reflections are conjugate (Exercise 14.2).

# Source Reference

Chapter 14: Conjugacy, Example (ii), pp. 80-81 (pdf).

# Verification Notes

- Definition source: Direct computation from Example (ii)
- Confidence rationale: HIGH — complete calculation shown
- Uncertainties: None
