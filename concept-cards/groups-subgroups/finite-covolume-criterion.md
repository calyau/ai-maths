---
# === CORE IDENTIFICATION ===
concept: Finite Covolume Criterion
slug: finite-covolume-criterion

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
pdf_page: 407
section: "Reduction theory"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Borel-Harish-Chandra theorem
  - compactness criterion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
  - reduction-theory
  - reductive-algebraic-group
extends: []
related:
  - lattice-in-lie-group
  - cocompact-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

For a reductive group $G$ over $\mathbb{Q}$ and arithmetic subgroup $\Gamma$: the volume of $\Gamma \backslash G(\mathbb{R})$ is finite iff $G$ has no nontrivial $\mathbb{Q}$-character, and $\Gamma \backslash G(\mathbb{R})$ is compact iff additionally $G(\mathbb{Q})$ has no nontrivial unipotent element.

# Core Definition

Theorem 12.4 (Milne, p. 407): Let $G$ be a reductive group over $\mathbb{Q}$, and let $\Gamma$ be an arithmetic subgroup of $G(\mathbb{Q})$.

(a) The volume of $\Gamma \backslash G(\mathbb{R})$ is finite if and only if $G$ has no nontrivial character over $\mathbb{Q}$ (for example, if $G$ is semisimple).

(b) The quotient $\Gamma \backslash G(\mathbb{R})$ is compact if and only if $G$ has no nontrivial character over $\mathbb{Q}$ and $G(\mathbb{Q})$ has no unipotent element $\neq 1$.

# Prerequisites

- **Arithmetic subgroup** — the discrete group in the quotient
- **Reduction theory** — provides the proof via Siegel sets
- **Reductive algebraic group** — the theorem applies to reductive groups

# Key Properties

1. Semisimple groups have no nontrivial characters, so their arithmetic subgroups always have finite covolume
2. The compactness criterion requires checking for rational unipotent elements
3. The necessity of the character condition follows from the example $\mathbb{G}_m(\mathbb{Z}) \backslash \mathbb{G}_m(\mathbb{R})$ having infinite volume
4. The sufficiency uses finiteness of Siegel set measure (Theorem 12.3)

# Construction / Recognition

## To Determine Finiteness of Covolume:
1. Check if $\mathrm{Hom}_{\mathbb{Q}}(G, \mathbb{G}_m) = 0$
2. If yes, $\Gamma \backslash G(\mathbb{R})$ has finite volume

## To Determine Compactness:
1. Check the character condition as above
2. Check if $G(\mathbb{Q})$ contains a unipotent element $\neq 1$
3. If no characters and no unipotents, the quotient is compact

# Context & Application

This criterion is the key result connecting the algebraic structure of $G$ to the geometric properties of $\Gamma \backslash G(\mathbb{R})$. It shows that the topology of the quotient is determined by algebraic data about the group.

# Examples

**Example 1** (p. 405): $\mathbb{G}_m(\mathbb{Z}) = \{\pm 1\}$ in $\mathbb{G}_m(\mathbb{R}) = \mathbb{R}^\times$ has infinite covolume because $\mathbb{G}_m$ has a nontrivial character (the identity).

**Example 2** (p. 407): $\mathrm{SL}_2(\mathbb{Z}) \backslash \mathrm{SL}_2(\mathbb{R})$ has finite volume but is not compact: $\mathrm{SL}_2$ is semisimple (no characters) but $\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix} \in \mathrm{SL}_2(\mathbb{Q})$ is unipotent.

**Example 3** (p. 407): For $B$ a quaternion division algebra with $B \otimes \mathbb{R} \simeq M_2(\mathbb{R})$, the norm-1 group $G$ has compact quotient: if $g$ is unipotent then $g - 1$ is nilpotent, hence zero in a division algebra.

**Example 4** (p. 407): $\mathrm{SO}(q)(\mathbb{Z}) \backslash \mathrm{SO}(q)(\mathbb{R})$ is compact iff $q$ does not represent zero over $\mathbb{Q}$ (Example 12.6).

# Relationships

## Builds Upon
- **Reduction theory** — provides the proof
- **Arithmetic subgroup** — the groups whose covolume is studied

## Enables
- **Lattice in Lie group** — the criterion shows when arithmetic subgroups are lattices
- **Cocompact subgroup** — the criterion determines when arithmetic subgroups are cocompact

# Common Errors

- **Error**: Applying the compactness criterion to non-reductive groups
  **Correction**: Theorem 12.4 is stated for reductive groups

# Common Confusions

- **Confusion**: Thinking "no rational unipotents" means "no unipotent subgroups over $\mathbb{Q}$"
  **Clarification**: The condition is about individual elements: $G(\mathbb{Q})$ has no $g \neq 1$ with $(g - 1)^n = 0$

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 12, page 407. Theorem 12.4, Examples 12.5-12.6.

# Verification Notes

- Definition source: Theorem 12.4 directly stated on p. 407
- Confidence: HIGH — explicit theorem with proof references
- Uncertainties: None
- Cross-reference status: Verified
