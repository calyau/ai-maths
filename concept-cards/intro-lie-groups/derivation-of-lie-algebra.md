---
# === CORE IDENTIFICATION ===
concept: Derivation of a Lie Algebra
slug: derivation-of-lie-algebra

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
pdf_page: 28
section: "3.6"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{Der}(\\mathfrak{g})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - ad-map
extends: []
related:
  - stabilizer-lie-algebra
  - automorphism-group-of-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

A derivation of a Lie algebra $\mathfrak{g}$ is a linear map $D: \mathfrak{g} \to \mathfrak{g}$ satisfying the Leibniz rule $D[a, b] = [Da, b] + [a, Db]$. The space $\mathrm{Der}(\mathfrak{g})$ is itself a Lie algebra.

# Core Definition

**Equation (3.13)** (Kirillov): $\mathrm{Der}(\mathfrak{g}) = \{x \in \mathfrak{gl}(\mathfrak{g}) \mid [xa, b] + [a, xb] = x[a, b] \;\forall a, b \in \mathfrak{g}\}$.

$\mathrm{Der}(\mathfrak{g})$ is the Lie algebra of $\mathrm{Aut}(\mathfrak{g})$ (equation 3.12-3.13).

The maps $\mathrm{ad}\, x$ for $x \in \mathfrak{g}$ are called inner derivations; they form an ideal $\mathrm{ad}(\mathfrak{g}) \subset \mathrm{Der}(\mathfrak{g})$ (Exercise 3.9).

# Prerequisites

- **Lie algebra** — the algebra being differentiated
- **ad map** — inner derivations are of the form $\mathrm{ad}\, x$

# Key Properties

1. $\mathrm{Der}(\mathfrak{g})$ is a Lie subalgebra of $\mathfrak{gl}(\mathfrak{g})$.
2. $\mathrm{ad}(\mathfrak{g})$ is an ideal in $\mathrm{Der}(\mathfrak{g})$ (Exercise 3.9 part 2).
3. $\mathrm{Aut}(\mathfrak{g})$ is a Lie group with Lie algebra $\mathrm{Der}(\mathfrak{g})$ (Example 3.30).
4. The Jacobi identity is equivalent to $\mathrm{ad}\, x$ being a derivation.

# Construction / Recognition

## To Construct/Create:
1. Find all linear maps $D: \mathfrak{g} \to \mathfrak{g}$ satisfying $D[a,b] = [Da, b] + [a, Db]$.

## To Identify/Recognize:
1. A linear map on $\mathfrak{g}$ satisfying the Leibniz rule with respect to the bracket.

# Context & Application

Derivations are the infinitesimal automorphisms of a Lie algebra. Inner derivations (those of the form $\mathrm{ad}\, x$) correspond to the adjoint action.

# Examples

**Example** (p. 28): For any Lie algebra $\mathfrak{g}$, the maps $\mathrm{ad}\, x$ are derivations (the Jacobi identity is precisely this statement).

**Example 3.30** (p. 28): For a finite-dimensional associative algebra $A$, $\mathrm{Der}(A) = \{x \mid (x.a)b + a(x.b) = x.(ab)\}$ is the Lie algebra of $\mathrm{Aut}(A)$.

# Relationships

## Builds Upon
- **Lie algebra** — the algebra being studied
- **ad map** — inner derivations

## Enables
- **Automorphism group of Lie algebra** — $\mathrm{Der}(\mathfrak{g}) = \mathrm{Lie}(\mathrm{Aut}(\mathfrak{g}))$

## Related
- **Stabilizer Lie algebra** — derivations arise as the Lie algebra of the automorphism stabilizer

# Common Errors

- **Error**: Assuming all derivations are inner.
  **Correction**: While inner derivations form an ideal, there may be outer derivations (derivations not of the form $\mathrm{ad}\, x$).

# Common Confusions

- **Confusion**: Confusing derivations of Lie algebras with derivations of associative algebras.
  **Clarification**: Same concept (Leibniz rule), different bracket: Lie algebras use $[\,,\,]$, associative algebras use the commutator $ab - ba$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, equations (3.12)-(3.13), Example 3.30, Exercise 3.9, pages 28-29.

# Verification Notes

- Definition source: Direct from equations (3.12)-(3.13) and Example 3.30
- Confidence rationale: Explicit formula in source
- Uncertainties: None
- Cross-reference status: Verified with Exercise 3.9
