---
# === CORE IDENTIFICATION ===
concept: "Cauchy's Theorem via Group Actions"
slug: cauchys-theorem-via-actions

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Actions, Orbits, and Stabilizers"
chapter_number: 17
pdf_page: 98
section: "Example (vi)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit-stabilizer-theorem
extends: []
related:
  - sylow-p-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can Cauchy's theorem be proved using group actions?"
---

# Quick Definition

Cauchy's theorem -- that a finite group whose order is divisible by a prime $p$ contains an element of order $p$ -- can be elegantly reproved using the action of $\mathbb{Z}_p$ on ordered strings $(x_1, \ldots, x_p)$ with $x_1 x_2 \cdots x_p = e$.

# Core Definition

**Example (vi)** (Armstrong, p. 101): Let $G$ be a finite group and $p$ a prime divisor of $|G|$. Let $X$ be the set of ordered strings $(x_1, x_2, \ldots, x_p)$ of elements of $G$ with $x_1 x_2 \cdots x_p = e$. The cyclic group $\mathbb{Z}_p$ acts on $X$ by cyclic permutation of entries: $m \in \mathbb{Z}_p$ sends $(x_1, \ldots, x_p)$ to $(x_{m+1}, \ldots, x_p, x_1, \ldots, x_m)$.

By Corollary 17.3, each orbit has size 1 or $p$. Since $|X|$ is divisible by $p$, and the orbits of size 1 include $(e, e, \ldots, e)$, there must be another fixed string $(x_1, \ldots, x_p)$ with $x_1 = x_2 = \cdots = x_p \ne e$, giving an element of order $p$.

# Prerequisites

- **Group action** -- the proof constructs an action of $\mathbb{Z}_p$
- **Orbit-Stabilizer theorem** -- determines orbit sizes

# Key Properties

1. The set $X$ has $|G|^{p-1}$ elements (choose $x_1, \ldots, x_{p-1}$ freely, then $x_p$ is determined)
2. $|X|$ is divisible by $p$ since $|G|$ is divisible by $p$
3. Each orbit under $\mathbb{Z}_p$ has size 1 or $p$
4. An orbit of size 1 corresponds to a constant string $x_1 = x_2 = \cdots = x_p$, giving an element of order dividing $p$

# Context & Application

This is a recasting of the earlier proof of Cauchy's theorem (Chapter 13) in the language of group actions. Armstrong presents it as Example (vi) to illustrate the power of the Orbit-Stabilizer theorem.

# Relationships

## Builds Upon
- **Group action** -- the proof constructs a $\mathbb{Z}_p$-action
- **Orbit-Stabilizer theorem** -- constrains orbit sizes

## Enables
- **Sylow theorems** -- Cauchy's theorem is a precursor to Sylow theory

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Example (vi), page 101.

# Verification Notes

- Proof: Direct from p. 101
- Confidence: HIGH -- explicit worked example
