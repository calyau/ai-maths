---
# === CORE IDENTIFICATION ===
concept: Orbit-Stabilizer Theorem
slug: orbit-stabilizer-theorem

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
section: "Theorem 17.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "orbit-stabilizer lemma"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - orbit
  - stabilizer
  - coset
extends: []
related:
  - conjugate-stabilizers-theorem
  - counting-theorem
  - lagranges-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do orbits and stabilizers relate (Orbit-Stabilizer theorem)?"
  - "How does the size of an orbit relate to the order of the group?"
---

# Quick Definition

For each $x \in X$, the size of the orbit $G(x)$ equals the index of the stabilizer $G_x$ in $G$. If $G$ is finite, $|G(x)| \cdot |G_x| = |G|$.

# Core Definition

**(17.2) Orbit-Stabilizer Theorem.** For each $x \in X$, the correspondence $g(x) \to gG_x$ is a bijection between $G(x)$ and the set of left cosets of $G_x$ in $G$ (Armstrong, p. 100).

The theorem says that the cardinality of the orbit of $x$ is equal to the index of the stabilizer of $x$ in $G$.

**(17.3) Corollary.** If $G$ is finite, the size of each orbit is a divisor of the order of $G$. This follows because $|G(x)| = |G|/|G_x|$, so $|G(x)| \cdot |G_x| = |G|$ (p. 100).

# Prerequisites

- **Group action** -- the theorem concerns an action of $G$ on $X$
- **Orbit** -- the orbit $G(x)$ appears on one side of the bijection
- **Stabilizer** -- the stabilizer $G_x$ determines the cosets on the other side
- **Coset** -- the bijection maps orbit elements to left cosets of $G_x$

# Key Properties

1. $|G(x)| = [G : G_x]$ (the index of $G_x$ in $G$)
2. If $G$ is finite: $|G(x)| \cdot |G_x| = |G|$
3. The orbit size divides $|G|$ when $G$ is finite
4. The bijection $g(x) \mapsto gG_x$ is well-defined and injective

# Construction / Recognition

## Proof Sketch (p. 100):
1. The map $g(x) \mapsto gG_x$ is clearly surjective (every coset has the form $gG_x$).
2. It is injective: if $gG_x = g'G_x$, then $g = g'h$ for some $h \in G_x$, so $g(x) = g'h(x) = g'(x)$.

# Context & Application

The Orbit-Stabilizer theorem is one of the most frequently used tools in finite group theory. Armstrong marks every use of it with an asterisk (*) in the proofs of the Sylow theorems (Chapter 20) to highlight its centrality. It generalises Lagrange's theorem and provides the key step in the proof of the Counting Theorem.

# Examples

**Example (v, continued)** (p. 100): For the conjugation action on a finite group, the number of elements in each conjugacy class divides $|G|$.

**Example (vi)** (p. 101): In the proof of Cauchy's theorem recast via group actions, $\mathbb{Z}_p$ acts on strings $(x_1, \ldots, x_p)$. By Corollary 17.3, each orbit contains either 1 or $p$ strings.

# Relationships

## Builds Upon
- **Orbit** -- provides the set being counted
- **Stabilizer** -- provides the subgroup whose index gives the count
- **Lagrange's theorem** -- the orbit size divides $|G|$ by Lagrange

## Enables
- **Counting theorem** -- the proof sums $|G_x|$ over orbits using this theorem
- **Sylow theorems** -- repeatedly invoked (Chapter 20)

## Related
- **Conjugate stabilizers theorem** -- companion result about stabilizer structure within orbits

# Common Errors

- **Error**: Writing $|G(x)| = |G_x|$ instead of $|G(x)| = |G|/|G_x|$.
  **Correction**: The orbit size equals the index, not the order, of the stabilizer.

# Common Confusions

- **Confusion**: Thinking the theorem only applies to finite groups.
  **Clarification**: The bijection between $G(x)$ and cosets of $G_x$ holds for any group. The equation $|G(x)| \cdot |G_x| = |G|$ is the finite case.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Theorem 17.2 and Corollary 17.3, page 100.

# Verification Notes

- Theorem statement and proof: Direct from p. 100
- Corollary: Direct from p. 100
- Confidence: HIGH -- central theorem, explicitly stated and proved
