---
# === CORE IDENTIFICATION ===
concept: Cauchy's Theorem
slug: cauchy-theorem

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
pdf_page: 61
section: "The class equation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - class-equation
extends: []
related:
  - p-group
  - lagrange-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does a group contain an element of prime order?"
---

# Quick Definition

If the prime $p$ divides $|G|$, then $G$ contains an element of order $p$.

# Core Definition

"If the prime $p$ divides $|G|$, then $G$ contains an element of order $p$" (Milne, Theorem 4.13, p. 61).

# Prerequisites

- **Class equation** — The proof uses the class equation and induction

# Key Properties

1. Provides a partial converse to Lagrange's theorem for prime divisors
2. Proved by induction on $|G|$ using the class equation
3. Key step: if $p$ divides all terms $(G : C_G(y))$, then $p | |Z(G)|$, and use structure of abelian groups

# Context & Application

Cauchy's theorem is fundamental for proving the existence of subgroups of prime order. It is used in the proof of the Sylow theorems and in classifying small groups.

# Examples

**Example 1** (p. 61): A group of order $2p$ ($p$ odd prime) contains elements of orders 2 and $p$ (Corollary 4.15), leading to the classification: cyclic or dihedral.

# Relationships

## Builds Upon
- **class-equation**

## Enables
- **p-group** — Corollary: a finite group is a $p$-group iff every element has $p$-power order

# Source Reference

Chapter 4: Groups Acting on Sets, "The class equation", Theorem 4.13, page 61.

# Verification Notes

- Definition source: Theorem 4.13, p. 61
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
