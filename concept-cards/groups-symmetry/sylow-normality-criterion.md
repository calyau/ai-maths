---
# === CORE IDENTIFICATION ===
concept: Sylow Normality Criterion
slug: sylow-normality-criterion

# === CLASSIFICATION ===
category: finite-group-classification
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Sylow Theorems"
chapter_number: 20
pdf_page: 120
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "unique Sylow subgroup is normal"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - second-sylow-theorem
extends: []
related:
  - third-sylow-theorem
  - classification-of-groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a Sylow p-subgroup normal?"
---

# Quick Definition

A Sylow $p$-subgroup $H$ of $G$ is normal if and only if it is the unique Sylow $p$-subgroup. This follows from the Second Sylow Theorem: conjugation sends Sylow $p$-subgroups to Sylow $p$-subgroups.

# Core Definition

If $H$ is a subgroup of $G$, then each conjugate $gHg^{-1}$ is also a subgroup of $G$ and has the same order as $H$. Therefore, if $G$ has no other subgroup of the same order as $H$, then $H$ must be a **normal** subgroup of $G$ (Armstrong, p. 122).

# Prerequisites

- **Second Sylow theorem** -- conjugacy of Sylow subgroups implies unique ones are normal

# Key Properties

1. $H$ is the unique Sylow $p$-subgroup iff $t = 1$
2. $t = 1$ iff $H$ is normal in $G$
3. This is the primary tool for producing normal subgroups in the classification of groups of given order

# Context & Application

Armstrong states this as a "minor though useful observation" before the classification of groups of order 12 (p. 122). It is used repeatedly: a unique Sylow subgroup is automatically normal, simplifying the structure of $G$.

# Examples

**Groups of order 12** (p. 121): When $t_3 = 1$, the unique Sylow 3-subgroup is normal. When $t_3 = 4$, the eight non-identity elements of the four Sylow 3-subgroups leave room for only one Sylow 2-subgroup, which is then normal.

# Relationships

## Builds Upon
- **Second Sylow theorem** -- conjugacy implies uniqueness forces normality

## Enables
- **Classification of groups of order 12** -- produces normal subgroups for the semi-direct product analysis

# Source Reference

Chapter 20: The Sylow Theorems, page 122. Observation made before the order-12 classification.

# Verification Notes

- Statement: Direct from p. 122
- Confidence: HIGH -- explicitly stated observation
