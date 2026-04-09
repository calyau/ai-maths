---
# === CORE IDENTIFICATION ===
concept: Projector
slug: projector

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
pdf_page: 103
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "idempotent endomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
extends: []
related:
  - maschke-theorem
  - g-invariant-subspace
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a projector?"
  - "How are projectors used in proving Maschke's theorem?"
---

# Quick Definition

An endomorphism pi of an F-vector space V is a projector if pi^2 = pi. It decomposes V = Ker(pi) + Im(pi).

# Core Definition

An endomorphism pi of an F-vector space V is called a **projector** if pi^2 = pi. The minimal polynomial divides X^2 - X = X(X-1), so V decomposes as V = V_0(pi) + V_1(pi) where V_0(pi) = Ker(pi) and V_1(pi) = Im(pi). Conversely, any direct sum decomposition V = V_0 + V_1 arises from the projector (v_0, v_1) -> (0, v_1). (Milne, Chapter 7, pp. 103-104)

# Prerequisites

- **Linear representation** — projectors appear in the proof of Maschke's theorem

# Key Properties

1. pi^2 = pi (idempotent)
2. V = Ker(pi) + Im(pi) as a direct sum
3. If pi is G-invariant, both Ker(pi) and Im(pi) are G-invariant
4. Direct sum decompositions correspond bijectively to projectors

# Construction / Recognition

1. Given a decomposition V = W + W', the projector onto W along W' sends (w, w') to (w, 0)
2. Given a projector pi, the decomposition is V = Im(pi) + Ker(pi)

# Context & Application

Projectors are the key technical tool in the general proof of Maschke's theorem. To find a G-invariant complement of a G-invariant subspace W, one starts with any projector onto W and averages it over G to obtain a G-invariant projector with the same image.

# Examples

**Example 1** (p. 104): In the proof of Maschke's theorem, pi_bar(v) = (1/|G|) sum_{g in G} g(pi(g^{-1}v)) is a G-invariant projector with Im(pi_bar) = W.

# Relationships

## Builds Upon
- Linear algebra (endomorphisms, eigenspaces)

## Enables
- **maschke-theorem** — the general proof uses averaged projectors

## Related
- **g-invariant-subspace** — G-invariant projectors produce G-invariant decompositions

## Contrasts With
- General endomorphisms (not idempotent)

# Common Errors

- **Error**: Forgetting that averaging a projector does not change its image
  **Correction**: The averaged projector pi_bar has Im(pi_bar) = W because the image of pi is W and W is G-invariant

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 103-104.

# Verification Notes

- Definition source: Direct from pp. 103-104
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
