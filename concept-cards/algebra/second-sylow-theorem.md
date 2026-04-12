---
concept: Second Sylow Theorem
slug: second-sylow-theorem
category: group-theory
subcategory: sylow-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.7 The Sylow Theorems"
extraction_confidence: high
aliases: []
prerequisites:
  - sylow-p-subgroup
  - first-sylow-theorem
  - fixed-point-theorem-p-group
extends: []
related:
  - third-sylow-theorem
  - normalizer
contrasts_with: []
answers_questions:
  - "Are all Sylow p-subgroups conjugate?"
  - "Is every p-subgroup contained in a Sylow p-subgroup?"
  - "How do I apply the Sylow theorems to analyze a finite group?"
---

# Quick Definition

The Second Sylow Theorem states: (a) all Sylow p-subgroups are conjugate, and (b) every p-subgroup is contained in a Sylow p-subgroup. A corollary: G has a unique Sylow p-subgroup iff it is normal.

# Core Definition

Let G be a finite group whose order is divisible by p. (a) The Sylow p-subgroups of G are conjugate subgroups. (b) Every subgroup of G that is a p-group is contained in a Sylow p-subgroup (Artin, Theorem 7.7.4, p. 217). The proof uses the Fixed Point Theorem: K acts on the cosets of H, and since p does not divide [G:H], there is a fixed point, showing K is in a conjugate of H.

# Prerequisites

- **Sylow p-subgroup** — The objects being related
- **First Sylow theorem** — Existence is needed first
- **Fixed point theorem (p-group)** — Key proof tool

# Key Properties

1. All Sylow p-subgroups are conjugate (hence isomorphic)
2. Every p-subgroup is in some Sylow p-subgroup
3. Unique Sylow p-subgroup iff it is normal (Corollary 7.7.5)
4. Conjugacy implies: any two Sylow p-subgroups have the same normalizer index

# Context & Application

The conjugacy statement is extremely powerful: it means there is essentially "one" Sylow p-subgroup up to conjugation. Uniqueness implies normality, which is the most common way the Sylow theorems are applied.

# Examples

**Example 1** (p. 218): In a group of order 15, both the Sylow 3-subgroup and Sylow 5-subgroup are unique (hence normal), giving G = C_3 x C_5.

**Example 2** (p. 219): In a group of order 21, the Sylow 7-subgroup must be normal (unique), but there may be 1 or 7 Sylow 3-subgroups.

# Relationships

## Builds Upon
- **Fixed point theorem (p-group)** — The key proof technique

## Enables
- **Unique Sylow implies normal** — The most applied corollary

# Source Reference

Chapter 7: More Group Theory, Section 7.7, Theorem 7.7.4, Corollary 7.7.5, pages 217, 221.

# Verification Notes

- Definition source: Direct from Theorem 7.7.4
- Confidence rationale: Named theorem, explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
