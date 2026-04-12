---
# === CORE IDENTIFICATION ===
concept: Third Sylow Theorem
slug: third-sylow-theorem

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
section: "Theorem 20.3"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Sylow counting theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - first-sylow-theorem
  - second-sylow-theorem
extends:
  - second-sylow-theorem
related:
  - classification-of-groups-of-order-12
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How many Sylow p-subgroups does a group have?"
  - "What constraints exist on the number of Sylow p-subgroups?"
---

# Quick Definition

The number $t$ of Sylow $p$-subgroups of a finite group $G$ satisfies $t \equiv 1 \pmod{p}$ and $t$ divides $k = |G|/p^m$.

# Core Definition

**(20.3) Theorem.** The number of subgroups of $G$ of order $p^m$ is congruent to 1 modulo $p$ and is a factor of $k$ (Armstrong, p. 120).

Here $|G| = kp^m$ with $p \nmid k$.

# Prerequisites

- **First Sylow theorem** -- at least one Sylow $p$-subgroup exists
- **Second Sylow theorem** -- all Sylow $p$-subgroups are conjugate, so the count is the orbit size

# Key Properties

1. $t \equiv 1 \pmod{p}$
2. $t \mid k$ where $k = |G|/p^m$
3. $t = 1$ iff the Sylow $p$-subgroup is normal
4. These two conditions severely restrict the possible values of $t$

# Construction / Recognition

## Proof Sketch (pp. 121--122):
1. Let $H_1$ act on $\{H_1, \ldots, H_t\}$ by conjugation
2. The orbit $\{H_1\}$ has size 1; all other orbits have size divisible by $p$ (using a key lemma)
3. Therefore $t \equiv 1 \pmod{p}$
4. Since $G$ acts transitively (by the Second Sylow Theorem), $t$ divides $|G|$
5. Since $p \nmid t$, we get $t \mid k$

## Key Lemma (p. 122):
The stabilizer $K_j$ of $H_j$ under the $H_1$-conjugation action equals $H_1 \cap H_j$. The proof uses the Second Isomorphism Theorem to show $K_j \subseteq H_j$.

# Context & Application

The Third Sylow Theorem is the most computationally useful of the three. When classifying groups of a given order, one lists the possible values of $t$ satisfying both $t \equiv 1 \pmod{p}$ and $t \mid k$, often narrowing possibilities dramatically.

# Examples

**Groups of order 12** (p. 121): $|G| = 12 = 4 \cdot 3$. For $p = 3$: $t \equiv 1 \pmod{3}$ and $t \mid 4$, so $t \in \{1, 4\}$. For $p = 2$: $t \equiv 1 \pmod{2}$ and $t \mid 3$, so $t \in \{1, 3\}$.

# Relationships

## Builds Upon
- **Second Sylow theorem** -- transitivity of the $G$-action gives $t \mid |G|$

## Enables
- **Classification of groups of order 12** -- the constraints on $t$ drive the case analysis

# Common Errors

- **Error**: Forgetting that $t$ must satisfy both conditions simultaneously.
  **Correction**: $t \equiv 1 \pmod{p}$ AND $t \mid k$. Both conditions must hold.

# Common Confusions

- **Confusion**: Thinking $t \mid |G|$ rather than $t \mid k$.
  **Clarification**: $t$ divides $k = |G|/p^m$, not $|G|$ itself (though it does also divide $|G|$).

# Source Reference

Chapter 20: The Sylow Theorems, Theorem 20.3, page 120. Proof on pp. 121--122.

# Verification Notes

- Theorem and proof: Direct from pp. 120--122
- Confidence: HIGH -- explicitly stated and proved
