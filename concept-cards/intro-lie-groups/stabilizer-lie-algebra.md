---
# === CORE IDENTIFICATION ===
concept: Stabilizer Lie Algebra
slug: stabilizer-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: subalgebras-ideals
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 27
section: "3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "isotropy algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - stabilizer-subgroup
  - lie-algebra-of-vector-fields
extends: []
related:
  - orbit
  - symmetry-group-of-bilinear-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

The Lie algebra of the stabilizer $\mathrm{Stab}(m)$ of a point $m$ under an action of $G$ on $M$ is $\mathfrak{h} = \{x \in \mathfrak{g} \mid \rho_*(x)(m) = 0\}$ — the elements whose corresponding vector field vanishes at $m$.

# Core Definition

**Theorem 3.26** (Kirillov): Let $G$ act on $M$ and let $m \in M$. Then:
1. $\mathrm{Stab}(m)$ is a Lie subgroup with Lie algebra $\mathfrak{h} = \{x \in \mathfrak{g} \mid \rho_*(x)(m) = 0\}$.
2. The map $G/\mathrm{Stab}(m) \to M$ given by $g \mapsto g.m$ is an immersion with tangent space $T_m\mathcal{O}_m = \mathfrak{g}/\mathfrak{h}$.

# Prerequisites

- **Stabilizer subgroup** — the group whose algebra we compute
- **Lie algebra of vector fields** — the action gives a map $\rho_*: \mathfrak{g} \to \mathrm{Vect}(M)$

# Key Properties

1. $\mathfrak{h}$ is the kernel of $\rho_*: \mathfrak{g} \to T_mM$.
2. $\mathfrak{h}$ is a Lie subalgebra (closed under bracket by equation 3.9).
3. $T_m\mathcal{O}_m \cong \mathfrak{g}/\mathfrak{h}$.
4. This provides a practical method for computing Lie algebras of groups defined as stabilizers.

# Construction / Recognition

## To Construct/Create:
1. Compute the action $\rho_*: \mathfrak{g} \to \mathrm{Vect}(M)$.
2. Evaluate at $m$: find $\{x \in \mathfrak{g} \mid \rho_*(x)(m) = 0\}$.

## To Identify/Recognize:
1. Elements of $\mathfrak{g}$ whose induced vector field vanishes at $m$.

# Context & Application

This is the main tool for computing Lie algebras of groups defined as symmetry groups. The classical groups $\mathrm{O}(n)$, $\mathrm{Sp}(2n)$, etc., can all be understood as stabilizers of bilinear forms.

# Examples

**Example 3.29** (p. 28): $\mathrm{O}(V, B) = \mathrm{Stab}(B)$ has Lie algebra $\mathfrak{o}(V, B) = \{x \in \mathfrak{gl}(V) \mid B(x.v, w) + B(v, x.w) = 0\}$.

**Example 3.30** (p. 28): $\mathrm{Aut}(A) = \mathrm{Stab}(\mu)$ has Lie algebra $\mathrm{Der}(A) = \{x \mid (x.a)b + a(x.b) = x.(ab)\}$.

**Corollary 3.28** (p. 27): For a representation $V$ and $v \in V$, $\mathrm{Stab}(v)$ has Lie algebra $\{x \in \mathfrak{g} \mid x.v = 0\}$.

# Relationships

## Builds Upon
- **Stabilizer subgroup** — the Lie algebra of this subgroup
- **Lie algebra of vector fields** — used to identify the infinitesimal condition

## Enables
- **Symmetry group of bilinear form** — $\mathrm{O}(V, B)$ via stabilizer
- **Derivation of a Lie algebra** — $\mathrm{Der}(\mathfrak{g})$ via stabilizer

## Related
- **Orbit** — tangent space is $\mathfrak{g}/\mathfrak{h}$

# Common Errors

- **Error**: Forgetting the Leibniz rule when computing the Lie algebra condition.
  **Correction**: For bilinear forms, the condition $B(gv, gw) = B(v,w)$ becomes $B(xv, w) + B(v, xw) = 0$ (the Leibniz rule applied to the group condition).

# Common Confusions

- **Confusion**: Whether Theorem 3.26 gives a new proof that classical groups are Lie groups.
  **Clarification**: Yes, combined with the stabilizer framework. Example 3.29 recovers $\mathrm{O}(n)$, $\mathrm{Sp}(2n)$, etc., as stabilizers of bilinear forms.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, Theorem 3.26, Corollaries 3.27-3.28, pages 27-28.

# Verification Notes

- Definition source: Direct from Theorem 3.26
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified with Examples 3.29, 3.30, Corollary 3.28
