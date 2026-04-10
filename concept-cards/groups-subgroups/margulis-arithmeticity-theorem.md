---
# === CORE IDENTIFICATION ===
concept: Margulis Arithmeticity Theorem
slug: margulis-arithmeticity-theorem

# === CLASSIFICATION ===
category: arithmetic-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "Arithmetic Subgroups"
chapter_number: 7
pdf_page: 410
section: "The theorem of Margulis"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Margulis's theorem
  - arithmeticity theorem
  - Margulis superrigidity

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup-of-lie-group
  - lattice-in-lie-group
extends: []
related:
  - arithmetic-subgroup
  - congruence-subgroup-problem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

Margulis's arithmeticity theorem states that every lattice (discrete subgroup of finite covolume) in a noncompact almost-simple real algebraic group $H$ is arithmetic, unless $H$ is isogenous to $\mathrm{SO}(1,n)$ or $\mathrm{SU}(1,n)$.

# Core Definition

"Let $\Gamma$ be a discrete subgroup of finite covolume in a noncompact almost-simple real algebraic group $H$; then $\Gamma$ is arithmetic unless $H$ is isogenous to $\mathrm{SO}(1,n)$ or $\mathrm{SU}(1,n)$." (Theorem 15.3, Milne, p. 410)

Here $\mathrm{SO}(1,n)$ corresponds to $x_1^2 + \cdots + x_n^2 - x_{n+1}^2$ and $\mathrm{SU}(1,n)$ corresponds to $z_1\bar{z}_1 + \cdots + z_n\bar{z}_n - z_{n+1}\bar{z}_{n+1}$.

# Prerequisites

- **Arithmetic subgroup of Lie group** — the target concept to be characterized
- **Lattice in Lie group** — the hypothesis of the theorem

# Key Properties

1. The theorem completely answers the Selberg-Pyatetski-Shapiro conjecture
2. The exceptions $\mathrm{SO}(1,n)$ and $\mathrm{SU}(1,n)$ are necessary: $\mathrm{SL}_2(\mathbb{R}) \simeq \mathrm{SO}(1,2)$ has non-arithmetic lattices
3. Non-arithmetic lattices in $\mathrm{SL}_2(\mathbb{R})$ arise from Riemann surfaces: every compact Riemann surface of genus $g \geq 2$ gives a discrete cocompact subgroup of $\mathrm{Aut}(\mathcal{H}) = \mathrm{SL}_2(\mathbb{R})/\{\pm I\}$
4. There are uncountably many discrete cocompact subgroups in $\mathrm{SL}_2(\mathbb{R})/\{\pm I\}$ but only countably many arithmetic ones
5. Different quaternion algebras give nonisomorphic arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$

# Construction / Recognition

## To Apply the Theorem:
1. Verify $H$ is a noncompact almost-simple real algebraic group
2. Verify $\Gamma$ is a lattice in $H$
3. Check that $H$ is not isogenous to $\mathrm{SO}(1,n)$ or $\mathrm{SU}(1,n)$
4. Conclude: $\Gamma$ is arithmetic

# Context & Application

Margulis's theorem is described as his "most spectacular achievement" (Tits 1980, quoted in Milne p. 410). It resolved a long-standing conjecture and showed that the arithmetic construction is essentially the only way to produce lattices in higher-rank semisimple Lie groups. The proof uses Margulis's superrigidity theorem.

# Examples

**Example 1** (p. 410): $\mathrm{SL}_2(\mathbb{R})$ is isogenous to $\mathrm{SO}(1,2)$, so the theorem does not apply. Indeed, the Riemann mapping theorem produces uncountably many non-arithmetic discrete cocompact subgroups.

**Example 2** (p. 410): Arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$ arise from quaternion algebras over totally real fields $F$. If $B = F + Fi + Fj + Fk$ with $B \otimes_{\mathbb{Q}} \mathbb{R} \simeq M_2(\mathbb{R}) \times \mathbb{H} \times \cdots \times \mathbb{H}$, then $G(\mathbb{R}) \simeq \mathrm{SL}_2(\mathbb{R}) \times (\mathbb{H}^1)^{d-1}$ and arithmetic subgroups project to lattices in $\mathrm{SL}_2(\mathbb{R})$.

**Example 3** (p. 410): Nonisomorphic quaternion algebras give different commensurability classes of arithmetic subgroups of $\mathrm{SL}_2(\mathbb{R})$, and all arithmetic commensurability classes arise this way.

# Relationships

## Builds Upon
- **Arithmetic subgroup of Lie group** — the notion characterized by the theorem
- **Lattice in Lie group** — the hypothesis

## Related
- **Arithmetic subgroup** — the algebraic notion that Margulis's theorem shows is essentially the only source of lattices
- **Congruence subgroup problem** — a related structural question about arithmetic groups

# Common Errors

- **Error**: Applying the theorem to $\mathrm{SL}_2(\mathbb{R})$
  **Correction**: $\mathrm{SL}_2(\mathbb{R})$ is isogenous to $\mathrm{SO}(1,2)$, which is an exception

# Common Confusions

- **Confusion**: Thinking the theorem says all discrete subgroups are arithmetic
  **Clarification**: The theorem requires *finite covolume*; arbitrary discrete subgroups need not be arithmetic even in higher rank

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 15, pages 410-411. Theorem 15.3, Definition 15.1, Example 15.2.

# Verification Notes

- Definition source: Theorem 15.3 directly quoted from p. 410
- Confidence: HIGH — explicit theorem statement
- Uncertainties: Proof references Margulis 1991 and Zimmer 1984
- Cross-reference status: Verified
