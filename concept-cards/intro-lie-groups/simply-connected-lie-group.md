---
# === CORE IDENTIFICATION ===
concept: Simply-Connected Lie Group
slug: simply-connected-lie-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: subgroups
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 33
section: "3.8"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - universal-cover-of-lie-group
extends: []
related:
  - equivalence-of-categories
  - first-fundamental-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A simply-connected Lie group is one with trivial fundamental group ($\pi_1 = \{1\}$). For any Lie algebra $\mathfrak{g}$, there exists a unique connected simply-connected Lie group $G$ with $\mathrm{Lie}(G) = \mathfrak{g}$.

# Core Definition

**Corollary 3.49** (Kirillov): For any Lie algebra $\mathfrak{g}$, there is a unique (up to isomorphism) connected simply-connected Lie group $G$ with $\mathrm{Lie}(G) = \mathfrak{g}$. Any other connected Lie group $G'$ with Lie algebra $\mathfrak{g}$ must be of the form $G/Z$ for some discrete central subgroup $Z \subset G$.

# Prerequisites

- **Lie group** — the base concept
- **Universal cover of Lie group** — construction of the simply-connected group

# Key Properties

1. Unique simply-connected group for each Lie algebra (Corollary 3.49).
2. All other connected groups with the same algebra are quotients $G/Z$ with $Z$ discrete and central.
3. For simply-connected $G_1$: $\mathrm{Hom}(G_1, G_2) = \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$ (Theorem 3.38).
4. Equivalence of categories: simply-connected connected Lie groups $\leftrightarrow$ finite-dimensional Lie algebras (Corollary 3.50).

# Construction / Recognition

## To Construct/Create:
1. Given $\mathfrak{g}$, find any Lie group with this algebra (Lie's third theorem).
2. Take the universal cover of its connected component.

## To Identify/Recognize:
1. A connected Lie group with $\pi_1 = \{1\}$.

# Context & Application

Simply-connected groups are the "canonical" representatives for each Lie algebra. The category equivalence means that studying Lie algebras is equivalent to studying these groups.

# Examples

**Example**: $\mathrm{SU}(n)$ is simply connected for $n \geq 2$.

**Example**: $\mathrm{SL}(n, \mathbb{C})$ is simply connected.

**Example**: $\mathrm{Spin}(n)$ is the simply-connected group with $\mathrm{Lie}(\mathrm{Spin}(n)) = \mathfrak{so}(n)$.

# Relationships

## Builds Upon
- **Universal cover of Lie group** — provides the construction

## Enables
- **Equivalence of categories** — Corollary 3.50
- **First fundamental theorem** — full surjectivity of Hom

## Related
- **Discrete central subgroup** — $G/Z$ gives non-simply-connected groups

# Common Errors

- **Error**: Assuming compact Lie groups are simply connected.
  **Correction**: $\mathrm{SO}(n)$ and $\mathrm{U}(n)$ are compact but not simply connected.

# Common Confusions

- **Confusion**: Whether the simply-connected group is always "nicer."
  **Clarification**: Not always; $\mathrm{Spin}(n)$ is harder to construct explicitly than $\mathrm{SO}(n)$. The algebra is often more convenient to work with.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.8, Corollary 3.49, 3.50, page 33.

# Verification Notes

- Definition source: Direct from Corollary 3.49
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified
