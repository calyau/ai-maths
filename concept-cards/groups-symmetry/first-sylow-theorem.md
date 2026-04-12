---
# === CORE IDENTIFICATION ===
concept: First Sylow Theorem
slug: first-sylow-theorem

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
section: "Theorem 20.1"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Sylow existence theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - sylow-p-subgroup
  - orbit-stabilizer-theorem
extends: []
related:
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does a Sylow p-subgroup always exist?"
  - "How do Sylow subgroups relate to the prime factorization of |G|?"
---

# Quick Definition

Every finite group $G$ whose order is divisible by a prime $p$ contains at least one subgroup of order $p^m$, where $p^m$ is the highest power of $p$ dividing $|G|$.

# Core Definition

**(20.1) Theorem.** The group $G$ contains at least one subgroup of order $p^m$ (Armstrong, p. 120).

Here $|G| = kp^m$ with $p \nmid k$.

# Prerequisites

- **Sylow p-subgroup** -- the objects whose existence is asserted
- **Orbit-Stabilizer theorem** -- the proof uses it (marked with * in the text)

# Key Properties

1. The existence is guaranteed for every prime $p$ dividing $|G|$
2. The proof is due to Wielandt (1959), using an action on subsets of size $p^m$

# Construction / Recognition

## Proof Sketch (Wielandt's proof, p. 120):
1. Let $X$ be the collection of all subsets of $G$ with $p^m$ elements
2. $G$ acts on $X$ by left translation: $g$ sends $A$ to $gA$
3. $|X| = \binom{kp^m}{p^m}$, which is not divisible by $p$
4. So some orbit $G(A)$ has size not divisible by $p$
5. By Orbit-Stabilizer: $|G| = |G(A)| \cdot |G_A|$, so $p^m$ divides $|G_A|$
6. But $G_A$ stabilizes $A$, meaning $G_A a \subseteq A$ for any $a \in A$, so $|G_A| \le p^m$
7. Therefore $|G_A| = p^m$ and $G_A$ is a Sylow $p$-subgroup

# Context & Application

The First Sylow Theorem is a far-reaching generalisation of Cauchy's theorem (which only guarantees elements of order $p$). Armstrong presents Wielandt's elegant 1959 proof, which avoids induction and uses only the Orbit-Stabilizer theorem.

# Relationships

## Builds Upon
- **Orbit-Stabilizer theorem** -- the sole tool in the proof

## Enables
- **Second Sylow theorem** -- conjugacy of Sylow subgroups
- **Third Sylow theorem** -- count of Sylow subgroups
- **Classification of groups of order 12** -- existence of Sylow subgroups is the starting point

# Common Errors

- **Error**: Thinking the proof constructs the Sylow subgroup explicitly.
  **Correction**: The proof shows existence via a counting argument on orbits; it does not exhibit the subgroup directly.

# Common Confusions

- **Confusion**: Conflating the First Sylow Theorem with Cauchy's theorem.
  **Clarification**: Cauchy guarantees an element of order $p$; Sylow guarantees a subgroup of order $p^m$ (the full prime-power factor).

# Source Reference

Chapter 20: The Sylow Theorems, Theorem 20.1, page 120. Proof on pp. 120--121.

# Verification Notes

- Theorem and proof: Direct from pp. 120--121
- Attribution to Wielandt (1959) noted
- Confidence: HIGH -- explicitly stated and proved
