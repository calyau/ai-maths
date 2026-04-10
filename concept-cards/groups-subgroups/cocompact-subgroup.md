---
# === CORE IDENTIFICATION ===
concept: Cocompact Subgroup
slug: cocompact-subgroup

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
pdf_page: 405
section: "\"Large\" discrete subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - uniform subgroup

# === TYPED RELATIONSHIPS ===
prerequisites:
  - discrete-subgroup-of-lie-group
extends: []
related:
  - lattice-in-lie-group
  - finite-covolume-criterion
contrasts_with:
  - lattice-in-lie-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

A discrete subgroup $\Gamma$ of a locally compact group $G$ is cocompact (or uniform) if $\Gamma \backslash G$ is compact. This is a strong condition meaning $\Gamma$ is "large" relative to $G$.

# Core Definition

"A discrete subgroup of a locally compact group $G$ is said to be *cocompact* (or *uniform*) if $\Gamma \backslash G$ is compact." (Milne, p. 405)

# Prerequisites

- **Discrete subgroup of Lie group** — cocompactness is a property of discrete subgroups

# Key Properties

1. Cocompact implies finite covolume (lattice), but not conversely
2. Cocompactness is a commensurability invariant (Exercise 11-1)
3. For semisimple $G$ with no nontrivial $\mathbb{Q}$-characters, $\Gamma \backslash G(\mathbb{R})$ is compact iff $G(\mathbb{Q})$ has no unipotent $\neq 1$ (Theorem 12.4b)

# Construction / Recognition

## To Recognize:
1. Check that $\Gamma \backslash G$ is compact
2. For arithmetic $\Gamma$ in a semisimple $G$: check that $G(\mathbb{Q})$ has no nontrivial unipotent elements

# Context & Application

Cocompactness gives the strongest notion of a "large" discrete subgroup. For arithmetic subgroups of semisimple groups, whether the quotient is compact is determined by whether the group has rational unipotent elements.

# Examples

**Example 1** (p. 405): $\Gamma = \mathbb{Z}e_1 + \cdots + \mathbb{Z}e_n$ in $G = \mathbb{R}^n$ is cocompact iff $n$ equals the rank (i.e., $\Gamma$ is a full lattice).

**Example 2** (p. 405): $\mathrm{SL}_2(\mathbb{Z})$ is *not* cocompact in $\mathrm{SL}_2(\mathbb{R})$ because $\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$ is unipotent in $\mathrm{SL}_2(\mathbb{Q})$. But $\mathrm{SL}_2(\mathbb{Z})$ has finite covolume.

**Example 3** (p. 407): If $B$ is a quaternion division algebra over $\mathbb{Q}$ with $B \otimes \mathbb{R} \simeq M_2(\mathbb{R})$, then $G(\mathbb{Z}) \backslash G(\mathbb{R})$ is compact (no rational unipotents in a division algebra).

# Relationships

## Builds Upon
- **Discrete subgroup of Lie group** — cocompactness is a property of discrete subgroups

## Related
- **Lattice in Lie group** — cocompact subgroups are lattices; the converse is false
- **Finite covolume criterion** — characterizes when arithmetic subgroups are cocompact

## Contrasts With
- **Lattice in Lie group** — lattices may fail to be cocompact (e.g., $\mathrm{SL}_2(\mathbb{Z})$)

# Common Errors

- **Error**: Assuming all lattices are cocompact
  **Correction**: $\mathrm{SL}_2(\mathbb{Z})$ is a non-cocompact lattice in $\mathrm{SL}_2(\mathbb{R})$

# Common Confusions

- **Confusion**: Confusing cocompact with compact
  **Clarification**: $\Gamma$ itself is discrete (not compact); it is the *quotient* $\Gamma \backslash G$ that is compact

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 11, pages 405-406.

# Verification Notes

- Definition source: Direct quote from p. 405
- Confidence: HIGH — explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
