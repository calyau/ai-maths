---
# === CORE IDENTIFICATION ===
concept: Centre of a p-Group
slug: centre-of-p-group

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
section: "Theorem 17.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "non-trivial centre of p-group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - conjugation-action
  - orbit-stabilizer-theorem
extends: []
related:
  - groups-of-order-p-squared
  - sylow-p-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does a p-group always have a non-trivial centre?"
---

# Quick Definition

If $p$ is prime and $|G| = p^k$ for some $k \ge 1$, then the centre $Z(G)$ is non-trivial. This follows from the conjugation action and the fact that conjugacy class sizes divide $|G|$.

# Core Definition

**(17.4) Theorem.** If $p$ is prime and if the order of $G$ is a power of $p$, then $G$ has a non-trivial centre (Armstrong, p. 101).

# Prerequisites

- **Conjugation action** -- the proof analyses the partition of $G$ into conjugacy classes
- **Orbit-Stabilizer theorem** -- used to show each conjugacy class has size 1 or a power of $p$

# Key Properties

1. In a $p$-group, every conjugacy class has size $1$ or $p^j$ for some $j \ge 1$
2. The centre consists of the size-1 conjugacy classes
3. If $Z(G)$ were trivial, then $|G| \equiv 1 \pmod{p}$, contradicting $|G| = p^k$
4. Therefore $|Z(G)| \ge p$

# Construction / Recognition

## Proof Sketch (p. 101):
1. Partition $G$ into conjugacy classes
2. Each class has size dividing $|G| = p^k$, so size is $1$ or a power of $p$
3. The centre is the union of size-1 classes
4. Summing class sizes: if $Z(G) = \{e\}$, then $|G| \equiv 1 \pmod{p}$, contradiction

# Context & Application

This theorem is used immediately in Theorem 17.5 to classify groups of order $p^2$, and it is a key ingredient in the theory of finite $p$-groups.

# Examples

**Theorem 17.5** (p. 101): Using Theorem 17.4, Armstrong proves that a group of order $p^2$ is either cyclic or isomorphic to $\mathbb{Z}_p \times \mathbb{Z}_p$.

# Relationships

## Builds Upon
- **Conjugation action** -- the proof uses conjugacy classes
- **Orbit-Stabilizer theorem** -- determines class sizes

## Enables
- **Groups of order p-squared** -- Theorem 17.5 uses this result
- **Sylow theorems** -- p-groups play a central role

# Common Errors

- **Error**: Assuming the centre of a $p$-group has order exactly $p$.
  **Correction**: The centre has order divisible by $p$, but may be larger. For abelian $p$-groups, $Z(G) = G$.

# Common Confusions

- **Confusion**: Thinking non-trivial centre means the group is abelian.
  **Clarification**: Non-trivial centre means $Z(G) \ne \{e\}$, but $Z(G)$ may be a proper subgroup of $G$.

# Source Reference

Chapter 17: Actions, Orbits, and Stabilizers, Theorem 17.4, page 101.

# Verification Notes

- Theorem and proof: Direct from p. 101
- Confidence: HIGH -- explicitly stated theorem with proof
