---
# === CORE IDENTIFICATION ===
concept: Sylow Lemma on Stabilizer Intersection
slug: sylow-lemma-stabilizer-intersection

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
section: "Lemma"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - second-sylow-theorem
extends: []
related:
  - third-sylow-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the stabilizer when one Sylow p-subgroup acts on others by conjugation?"
---

# Quick Definition

When a Sylow $p$-subgroup $H_1$ acts by conjugation on the set of all Sylow $p$-subgroups, the stabilizer of $H_j$ is precisely $H_1 \cap H_j$.

# Core Definition

**Lemma.** Let $H_1, \ldots, H_t$ be the Sylow $p$-subgroups of $G$. If $H_1$ acts on $\{H_1, \ldots, H_t\}$ by conjugation and $K_j$ is the stabilizer of $H_j$, then $K_j = H_1 \cap H_j$ (Armstrong, p. 122).

# Prerequisites

- **Sylow p-subgroup** -- the objects being acted upon
- **Second Sylow theorem** -- context for the conjugation action

# Key Properties

1. $K_j = \{h \in H_1 \mid hH_jh^{-1} = H_j\} = H_1 \cap H_j$
2. In particular, $K_1 = H_1$ (the orbit of $H_1$ has size 1)
3. For $j \ne 1$: $|K_j| < p^m$, so the orbit of $H_j$ has size divisible by $p$
4. This gives $t \equiv 1 \pmod{p}$

# Construction / Recognition

## Proof Sketch (p. 122):
1. By definition $K_j \subseteq H_1$ and $H_1 \cap H_j \subseteq K_j$
2. Since $K_j$ normalizes $H_j$, the product $K_j H_j$ is a subgroup
3. By the Second Isomorphism Theorem: $|K_j H_j| = |K_j| \cdot |H_j| / |K_j \cap H_j|$
4. This is a power of $p$, but the largest available is $p^m = |H_j|$
5. So $K_j H_j = H_j$, hence $K_j \subseteq H_j$, giving $K_j = H_1 \cap H_j$

# Context & Application

This lemma is the technical heart of the proofs of the Second and Third Sylow Theorems. It shows that distinct Sylow subgroups are separated enough that their overlap creates orbits of size divisible by $p$.

# Relationships

## Builds Upon
- **Sylow p-subgroup** -- the objects involved

## Enables
- **Third Sylow theorem** -- the congruence $t \equiv 1 \pmod{p}$ follows directly

# Source Reference

Chapter 20: The Sylow Theorems, Lemma, page 122.

# Verification Notes

- Lemma and proof: Direct from p. 122
- Confidence: HIGH -- explicitly stated and proved
