---
# === CORE IDENTIFICATION ===
concept: "Maschke's Theorem"
slug: maschke-theorem

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 102
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Maschke's theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - g-invariant-subspace
extends: []
related:
  - completely-reducible-representation
  - semisimple-module
  - group-algebra
  - semisimple-f-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Maschke's theorem connect semisimplicity to group order?"
  - "When is every representation of a finite group completely reducible?"
  - "What condition on the field ensures complete reducibility?"
---

# Quick Definition

If char(F) does not divide |G|, then every G-invariant subspace W of a representation space V has a G-invariant complement, i.e., V = W + W' with W' also G-invariant.

# Core Definition

**Theorem 7.4 (Maschke).** Let G -> GL(V) be a linear representation of G. If the characteristic of F does not divide |G|, then every G-invariant subspace W of V has a G-invariant complement, i.e., there exists a G-invariant subspace W' such that V = W + W'. (Milne, Chapter 7, p. 102)

# Prerequisites

- **Linear representation** — the theorem applies to linear representations
- **G-invariant subspace** — the key concept being complemented

# Key Properties

1. The condition char(F) does not divide |G| is necessary (counterexample: C_p over char p, p. 102)
2. Always applies when F has characteristic zero
3. Implies every F[G]-module is semisimple (Proposition 7.9)
4. Implies F[G] is a semisimple F-algebra
5. Equivalent to: every representation is completely reducible

# Construction / Recognition

Two proofs are given:

**Proof 1 (F = R or C):** Average a positive definite bilinear form over G to get a G-invariant positive definite form. Take orthogonal complements.

**Proof 2 (general case):** Start with any projector pi with image W. Average it: pi_bar(v) = (1/|G|) sum_{g in G} g(pi(g^{-1}v)). This gives a G-invariant projector with the same image W. Its kernel is the G-invariant complement.

# Context & Application

Maschke's theorem is the foundational result of the representation theory of finite groups. It reduces the study of representations to the study of irreducible representations. It also establishes F[G] as a semisimple algebra, opening the door to Wedderburn theory.

The condition char(F) does not divide |G| is essential. When it fails, modular representation theory (a much harder subject) is needed.

# Examples

**Example 1** (p. 102): Counterexample: G = C_p over F of characteristic p. The representation via (1, 1; 0, 1) has an invariant subspace with no invariant complement.

**Example 2** (p. 105, 7.9): Every F[G]-module decomposes as a direct sum of simple submodules when char(F) does not divide |G|.

# Relationships

## Builds Upon
- **linear-representation** — applies to linear representations
- **g-invariant-subspace** — concerns complements of invariant subspaces

## Enables
- **completely-reducible-representation** — all representations are completely reducible
- **semisimple-module** — all F[G]-modules are semisimple
- **semisimple-f-algebra** — F[G] is semisimple
- **decomposition-of-f-g** — F[G] decomposes as a product of matrix algebras

## Related
- **g-invariant-bilinear-form** — used in the first proof
- **unitary-representation** — all real representations are unitary

## Contrasts With
- Modular representation theory (char(F) divides |G|)

# Common Errors

- **Error**: Applying Maschke's theorem when char(F) divides |G|
  **Correction**: The theorem requires char(F) does not divide |G|; it fails otherwise

- **Error**: Thinking the averaging trick works without the characteristic condition
  **Correction**: Division by |G| requires |G| to be invertible in F, which fails when char(F) | |G|

# Common Confusions

- **Confusion**: Thinking Maschke's theorem says the averaged bilinear form is nondegenerate
  **Clarification**: The bilinear form proof only works for R and C (positive definiteness); the general proof uses averaged projectors instead

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.4 and proofs, pp. 102-104.

# Verification Notes

- Definition source: Direct from Theorem 7.4, p. 102
- Confidence rationale: HIGH — named theorem with explicit statement
- Uncertainties: None
