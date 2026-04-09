---
# === CORE IDENTIFICATION ===
concept: Left-Invariant Vector Field
slug: left-invariant-vector-field

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 14
section: "2.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - left-action
extends: []
related:
  - right-invariant-vector-field
  - bi-invariant-vector-field
  - one-parameter-subgroup
  - exponential-map
contrasts_with:
  - right-invariant-vector-field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponential map?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A left-invariant vector field on a Lie group $G$ is a vector field $v$ such that $g.v = v$ for every $g \in G$, where $g.v$ denotes the pushforward by left multiplication. The space of left-invariant vector fields is isomorphic to $T_1G$.

# Core Definition

**Definition 2.24** (Kirillov): A vector field $v \in \mathrm{Vect}(G)$ is left-invariant if $g.v = v$ for every $g \in G$.

**Theorem 2.25**: The map $v \mapsto v(1)$ defines an isomorphism of the vector space of left-invariant vector fields on $G$ with $T_1G$.

# Prerequisites

- **Lie group** — the group on which the fields live
- **Left action** — invariance is defined with respect to left multiplication

# Key Properties

1. Every $x \in T_1G$ extends uniquely to a left-invariant vector field via $v(g) = gx$ (Theorem 2.25).
2. Left-invariant vector fields are complete: their integral curves exist for all time.
3. The integral curve through $1$ of the left-invariant field corresponding to $x$ is the one-parameter subgroup $\exp(tx)$.
4. The flow of a left-invariant field $v$ with $v(1) = x$ is $g \mapsto g\exp(tx)$ (Proposition 3.6, but corrected: this is for right-invariant; left-invariant flow is $g \mapsto \exp(tx)g$).

# Construction / Recognition

## To Construct/Create:
1. Choose $x \in T_1G$.
2. Define $v(g) = (L_g)_* x = gx$ for all $g \in G$.

## To Identify/Recognize:
1. A vector field invariant under all left translations $L_g$.

# Context & Application

Left-invariant vector fields provide the bridge between the Lie algebra $\mathfrak{g} = T_1G$ and global objects on the group. They are used to define the exponential map and, via their Lie bracket, the commutator on the Lie algebra.

# Examples

**Example 3.10** (p. 22): For $\mathrm{SO}(3, \mathbb{R})$, the left-invariant vector fields corresponding to $J_x, J_y, J_z \in \mathfrak{so}(3, \mathbb{R})$ generate rotations.

# Relationships

## Builds Upon
- **Left action** — invariance is with respect to left multiplication

## Enables
- **Exponential map** — integral curves of left-invariant fields give one-parameter subgroups
- **Lie algebra bracket** — commutator of left-invariant fields (with a sign) gives the bracket

## Related
- **Right-invariant vector field** — invariant under right multiplication

## Contrasts With
- **Right-invariant vector field** — the isomorphism with $\mathfrak{g}$ via right-invariant fields preserves the bracket (Corollary 3.25), while left-invariant fields give the opposite sign (Exercise 3.4)

# Common Errors

- **Error**: Assuming left-invariant and right-invariant extensions of $x \in T_1G$ agree.
  **Correction**: They generally differ; they agree if and only if $x$ is fixed by the adjoint action.

# Common Confusions

- **Confusion**: Which type of invariant vector field gives the correct sign for the Lie bracket.
  **Clarification**: Right-invariant fields give the standard bracket $[x, y]$ (Corollary 3.25); left-invariant fields give $-[x, y]$ (Exercise 3.4).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, Definition 2.24 and Theorem 2.25, page 14.

# Verification Notes

- Definition source: Direct from Definition 2.24 and Theorem 2.25
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Proposition 3.6, Corollary 3.25, Exercise 3.4
