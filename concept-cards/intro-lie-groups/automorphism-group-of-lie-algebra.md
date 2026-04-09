---
# === CORE IDENTIFICATION ===
concept: Automorphism Group of a Lie Algebra
slug: automorphism-group-of-lie-algebra

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
  - "$\\mathrm{Aut}(\\mathfrak{g})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
  - stabilizer-lie-algebra
extends: []
related:
  - derivation-of-lie-algebra
  - adjoint-action-on-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
---

# Quick Definition

$\mathrm{Aut}(\mathfrak{g}) = \{g \in \mathrm{GL}(\mathfrak{g}) \mid [ga, gb] = g[a, b] \;\forall a, b\}$ is a Lie group with Lie algebra $\mathrm{Der}(\mathfrak{g})$, the derivations of $\mathfrak{g}$.

# Core Definition

**Equation (3.12)** (Kirillov): $\mathrm{Aut}(\mathfrak{g}) = \{g \in \mathrm{GL}(\mathfrak{g}) \mid [ga, gb] = g[a, b] \;\forall a, b \in \mathfrak{g}\}$ is a Lie group with Lie algebra $\mathrm{Der}(\mathfrak{g})$ (equation 3.13).

# Prerequisites

- **Lie algebra** — the algebra whose automorphisms we study
- **Stabilizer Lie algebra** — used in the proof

# Key Properties

1. $\mathrm{Aut}(\mathfrak{g})$ is a closed subgroup of $\mathrm{GL}(\mathfrak{g})$, hence a Lie group.
2. $\mathrm{Lie}(\mathrm{Aut}(\mathfrak{g})) = \mathrm{Der}(\mathfrak{g})$.
3. The map $g \mapsto \mathrm{Ad}\, g$ gives a morphism $G \to \mathrm{Aut}(\mathfrak{g})$ (Exercise 3.9).
4. Inner automorphisms ($\mathrm{Ad}\, g$ for $g \in G$) form a normal subgroup.
5. Inner derivations ($\mathrm{ad}\, x$ for $x \in \mathfrak{g}$) form an ideal in $\mathrm{Der}(\mathfrak{g})$ (Exercise 3.9).

# Construction / Recognition

## To Construct/Create:
1. Take all invertible linear maps $\mathfrak{g} \to \mathfrak{g}$ preserving the bracket.

## To Identify/Recognize:
1. Bracket-preserving invertible linear maps.

# Context & Application

The automorphism group and its Lie algebra of derivations play an important role in the structure theory. For semisimple algebras, $\mathrm{Der}(\mathfrak{g}) = \mathrm{ad}(\mathfrak{g})$ (all derivations are inner).

# Examples

**Example** (p. 28, Exercise 3.9): $\mathrm{Ad}: G \to \mathrm{Aut}(\mathfrak{g})$ is a Lie group morphism; $\mathrm{ad}: \mathfrak{g} \to \mathrm{Der}(\mathfrak{g})$ is the corresponding Lie algebra morphism.

# Relationships

## Builds Upon
- **Lie algebra** — the object of study
- **Stabilizer Lie algebra** — $\mathrm{Aut}(\mathfrak{g}) = \mathrm{Stab}(\text{bracket})$

## Enables
- **Derivation algebra** — $\mathrm{Der}(\mathfrak{g}) = \mathrm{Lie}(\mathrm{Aut}(\mathfrak{g}))$

## Related
- **Adjoint representation** — $\mathrm{Ad}: G \to \mathrm{Aut}(\mathfrak{g})$

# Common Errors

- **Error**: Assuming $\mathrm{Aut}(\mathfrak{g})$ is the same as the outer automorphism group.
  **Correction**: $\mathrm{Aut}(\mathfrak{g})$ includes both inner and outer automorphisms. The outer automorphism group is $\mathrm{Aut}(\mathfrak{g})/\mathrm{Inn}(\mathfrak{g})$.

# Common Confusions

- **Confusion**: Whether $\mathrm{Aut}(\mathfrak{g})$ depends on the choice of Lie group $G$.
  **Clarification**: No. $\mathrm{Aut}(\mathfrak{g})$ depends only on the abstract Lie algebra $\mathfrak{g}$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.6, equations (3.12)-(3.13), Example 3.30, Exercise 3.9, pages 28-29.

# Verification Notes

- Definition source: Direct from equation (3.12)
- Confidence rationale: Explicit formula
- Uncertainties: None
- Cross-reference status: Verified with Exercise 3.9
