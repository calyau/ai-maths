---
# === CORE IDENTIFICATION ===
concept: Lattice in a Lie Group
slug: lattice-in-lie-group

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
  - lattice subgroup
  - discrete subgroup of finite covolume

# === TYPED RELATIONSHIPS ===
prerequisites:
  - discrete-subgroup-of-lie-group
extends:
  - discrete-subgroup-of-lie-group
related:
  - arithmetic-subgroup
  - cocompact-subgroup
  - margulis-arithmeticity-theorem
contrasts_with:
  - cocompact-subgroup

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

A lattice in a locally compact group $G$ is a discrete subgroup $\Gamma$ such that $\Gamma \backslash G$ has finite volume with respect to the left-invariant Haar measure. Lattices are "large" discrete subgroups that need not be cocompact.

# Core Definition

On each locally compact group $G$ there is a left-invariant Borel measure (Haar measure), unique up to a constant, which induces a measure on $\Gamma \backslash G$. "If $\mu(\Gamma \backslash G) < \infty$, then one says that $\Gamma$ has *finite covolume*, or that $\Gamma$ is a *lattice* in $G$." (Milne, p. 405)

If $K$ is a compact subgroup of $G$, the Haar measure induces a left-invariant measure on $G/K$, and $\mu(\Gamma \backslash G) < \infty$ iff $\mu(\Gamma \backslash G/K) < \infty$.

# Prerequisites

- **Discrete subgroup of Lie group** — a lattice is a discrete subgroup with finite covolume

# Key Properties

1. Every cocompact discrete subgroup is a lattice, but not conversely
2. Finite covolume is a commensurability invariant (Exercise 11-1)
3. For semisimple $G$ with no nontrivial $\mathbb{Q}$-characters, arithmetic subgroups are lattices (Theorem 12.4a)
4. Margulis's theorem: for most semisimple Lie groups, all lattices are arithmetic (Theorem 15.3)

# Construction / Recognition

## To Construct:
1. Take an algebraic group $G$ over $\mathbb{Q}$ with no nontrivial $\mathbb{Q}$-characters
2. Any arithmetic subgroup $\Gamma$ of $G(\mathbb{Q})$ is a lattice in $G(\mathbb{R})$

## To Recognize:
1. Check that $\Gamma$ is discrete in $G$
2. Check that $\int_{\Gamma \backslash G} d\mu < \infty$

# Context & Application

Lattices provide the "right" generalization of the notion of a discrete group acting with compact quotient. For $\mathrm{SL}_2(\mathbb{R})$, non-arithmetic lattices arise from Riemann surfaces, but Margulis showed that for higher-rank semisimple groups, all lattices are arithmetic.

# Examples

**Example 1** (p. 405): $\mathrm{SL}_2(\mathbb{Z})$ is a lattice in $\mathrm{SL}_2(\mathbb{R})$ with $\int_D \frac{dxdy}{y^2} < \infty$, but it is not cocompact.

**Example 2** (p. 405): $\mathbb{G}_m(\mathbb{Z}) = \{\pm 1\}$ is *not* a lattice in $\mathbb{G}_m(\mathbb{R}) = \mathbb{R}^\times$ because $\int_{\mathbb{R}^\times/\{\pm 1\}} \frac{dx}{x} = \infty$.

**Example 3** (p. 405): $\mathbb{Z}^i$ in $\mathbb{R}^n$ has finite covolume iff $i = n$.

# Relationships

## Builds Upon
- **Discrete subgroup of Lie group** — lattices are discrete subgroups with an additional finiteness condition

## Enables
- **Margulis arithmeticity theorem** — characterizes which lattices are arithmetic
- **Reduction theory** — provides tools for understanding lattice quotients

## Related
- **Arithmetic subgroup** — arithmetic subgroups of semisimple groups are lattices
- **Cocompact subgroup** — cocompact subgroups are lattices, but not all lattices are cocompact

## Contrasts With
- **Cocompact subgroup** — cocompact is stronger than finite covolume

# Common Errors

- **Error**: Assuming $G(\mathbb{Z})$ is always a lattice in $G(\mathbb{R})$
  **Correction**: $\mathbb{G}_m(\mathbb{Z}) = \{\pm 1\}$ is not a lattice in $\mathbb{R}^\times$; the group needs no nontrivial characters for this to hold

# Common Confusions

- **Confusion**: Confusing "lattice in a Lie group" with "lattice in a vector space"
  **Clarification**: A lattice in a Lie group is a discrete subgroup of finite covolume; a lattice in a vector space is a finitely generated $\mathbb{Z}$-submodule spanning the space

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 11, pages 405-406. Examples 11.1-11.3.

# Verification Notes

- Definition source: Direct quote from p. 405
- Confidence: HIGH — explicit definition with examples
- Uncertainties: None
- Cross-reference status: Verified
