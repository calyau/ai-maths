---
# === CORE IDENTIFICATION ===
concept: Nontrivial Centre of p-Groups
slug: nontrivial-centre-of-p-groups

# === CLASSIFICATION ===
category: group-actions
subcategory: counting
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 62
section: "p-groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - p-group
  - class-equation
extends: []
related:
  - centre-of-group
  - p-group-properties
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does every nontrivial p-group have a nontrivial centre?"
---

# Quick Definition

Every nontrivial finite $p$-group has nontrivial centre: $|Z(G)| > 1$.

# Core Definition

"Every nontrivial finite $p$-group has nontrivial centre" (Milne, Theorem 4.16, p. 62).

# Prerequisites

- **p-group** — The groups to which the theorem applies
- **Class equation** — The proof tool

# Key Properties

1. Proof: In the class equation $|G| = |Z(G)| + \sum (G : C_G(y))$, every term $(G : C_G(y))$ is a power of $p > 1$, so $p | |Z(G)|$
2. Consequence: $G$ of order $p^n$ has normal subgroups of order $p^m$ for all $m \leq n$ (by induction through $G/Z$)
3. Consequence: every group of order $p^2$ is abelian

# Context & Application

This theorem is the gateway to understanding $p$-group structure. It shows $p$-groups are fundamentally different from simple groups (which have trivial centre).

# Relationships

## Builds Upon
- **p-group**, **class-equation**

## Enables
- **p-group-properties** — Further structural results follow from this

# Source Reference

Chapter 4: Groups Acting on Sets, "p-groups", Theorem 4.16, page 62.

# Verification Notes

- Definition source: Theorem 4.16, p. 62
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
