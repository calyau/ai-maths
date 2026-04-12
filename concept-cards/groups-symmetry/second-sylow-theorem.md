---
# === CORE IDENTIFICATION ===
concept: Second Sylow Theorem
slug: second-sylow-theorem

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
section: "Theorem 20.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Sylow conjugacy theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-sylow-theorem
  - orbit-stabilizer-theorem
extends:
  - first-sylow-theorem
related:
  - third-sylow-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all Sylow p-subgroups conjugate?"
---

# Quick Definition

Any two Sylow $p$-subgroups of a finite group $G$ are conjugate. Equivalently, if $H$ is a Sylow $p$-subgroup, then every Sylow $p$-subgroup has the form $gHg^{-1}$ for some $g \in G$.

# Core Definition

**(20.2) Theorem.** Any two subgroups of $G$ of order $p^m$ are conjugate (Armstrong, p. 120).

# Prerequisites

- **First Sylow theorem** -- ensures existence of Sylow $p$-subgroups
- **Orbit-Stabilizer theorem** -- used in the proof

# Key Properties

1. All Sylow $p$-subgroups form a single conjugacy class of subgroups
2. A Sylow $p$-subgroup is normal in $G$ iff it is the unique one
3. The number of Sylow $p$-subgroups equals $[G : N_G(H)]$ where $N_G(H)$ is the normalizer

# Construction / Recognition

## Proof Sketch (p. 121):
1. Let $H_1, \ldots, H_t$ be all Sylow $p$-subgroups
2. Let $G$ act on $\{H_1, \ldots, H_t\}$ by conjugation
3. The $G$-orbit of $H_1$ has size $\equiv 1 \pmod{p}$ (shown by letting $H_1$ act)
4. If some $H_r$ is not in this orbit, let $H_r$ act: the $G$-orbit of $H_1$ would have size $\equiv 0 \pmod{p}$, contradiction
5. Therefore the $G$-action is transitive: all Sylow $p$-subgroups are conjugate

# Context & Application

Conjugacy of Sylow subgroups is a powerful structural result. It means that if $G$ has a unique Sylow $p$-subgroup, that subgroup must be normal -- a key tool in classifying groups of small order.

# Relationships

## Builds Upon
- **First Sylow theorem** -- existence is needed before conjugacy can be discussed

## Enables
- **Classification of groups of order 12** -- uniqueness of Sylow subgroups implies normality

## Related
- **Third Sylow theorem** -- the count of conjugate Sylow subgroups

# Source Reference

Chapter 20: The Sylow Theorems, Theorem 20.2, page 120. Proof on p. 121.

# Verification Notes

- Theorem and proof: Direct from pp. 120--121
- Confidence: HIGH -- explicitly stated and proved
