---
# === CORE IDENTIFICATION ===
concept: Haar Measure
slug: haar-measure

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - left-invariant Haar measure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - lattice-in-lie-group
  - cocompact-subgroup
  - finite-covolume-criterion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do arithmetic subgroups relate to discrete subgroups of Lie groups?"
---

# Quick Definition

The (left-invariant) Haar measure on a locally compact group $G$ is a Borel measure invariant under left translations, unique up to a positive scalar. It provides the notion of volume needed to define finite covolume (lattice) and cocompact subgroups.

# Core Definition

"On each locally compact group $G$, there exists a left-invariant Borel measure, unique up to a constant, called the *left-invariant Haar measure*." (Milne, p. 405)

The Haar measure on $G$ induces a measure on $\Gamma \backslash G$ for any discrete subgroup $\Gamma$. If $K$ is a compact subgroup, the Haar measure induces a left-invariant measure on $G/K$, and $\mu(\Gamma \backslash G) < \infty$ if and only if $\mu(\Gamma \backslash G/K) < \infty$.

# Prerequisites

- **Lie group** — Haar measure is defined on locally compact groups, in particular Lie groups

# Key Properties

1. Existence and uniqueness (up to scalar) for locally compact groups
2. For real Lie groups, the proof of existence is more elementary than in the general case
3. The Haar measure on $\mathbb{R}^n$ is the Lebesgue measure
4. The Haar measure on $\mathbb{R}^\times$ is $dx/|x|$
5. The left-invariant measure on $\mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2) \simeq \mathcal{H}$ is $dxdy/y^2$

# Construction / Recognition

## Standard Examples:
1. $G = \mathbb{R}^n$: Lebesgue measure
2. $G = \mathbb{R}^\times$: $dx/|x|$
3. $G = \mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2) \simeq \mathcal{H}$: $dxdy/y^2$

# Context & Application

Haar measure is the tool that makes "finite covolume" (and hence the notion of lattice) precise. Without it, one cannot state the key results about arithmetic subgroups being lattices, or formulate Margulis's arithmeticity theorem.

# Examples

**Example 1** (p. 405): For $G = \mathbb{R}^n$ and $\Gamma = \mathbb{Z}^n$, the covolume is $\mu(\mathbb{Z}^n \backslash \mathbb{R}^n) = 1$ (with standard Lebesgue measure on $\mathbb{R}^n$).

**Example 2** (p. 405): For $\mathrm{SL}_2(\mathbb{Z})$ acting on $\mathcal{H}$ with measure $dxdy/y^2$: $\int_D \frac{dxdy}{y^2} \leq \int_{\sqrt{3}/2}^\infty \frac{dy}{y^2} < \infty$.

**Example 3** (p. 405): For $\mathbb{G}_m(\mathbb{Z}) = \{\pm 1\}$ in $\mathbb{R}^\times$ with measure $dx/x$: $\int_0^\infty dx/x = \infty$, so $\{\pm 1\}$ is not a lattice.

# Relationships

## Enables
- **Lattice in Lie group** — finite covolume is measured by Haar measure
- **Cocompact subgroup** — cocompactness implies finite Haar measure of quotient
- **Finite covolume criterion** — the criterion characterizes when the Haar volume is finite

# Common Errors

- **Error**: Assuming the Haar measure is both left- and right-invariant
  **Correction**: Left and right Haar measures may differ for non-unimodular groups; they coincide for semisimple groups

# Common Confusions

- **Confusion**: Thinking finite covolume means compact
  **Clarification**: $\mathrm{SL}_2(\mathbb{Z}) \backslash \mathcal{H}$ has finite volume but is not compact

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 11, page 405.

# Verification Notes

- Definition source: Direct quote from p. 405
- Confidence: MEDIUM — definition is standard but only briefly stated in the source
- Uncertainties: None
- Cross-reference status: Verified
