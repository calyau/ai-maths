---
# === CORE IDENTIFICATION ===
concept: Averaging Over G
slug: averaging-over-g

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
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - "Reynolds operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - group-algebra
extends: []
related:
  - maschke-theorem
  - g-invariant-bilinear-form
  - fixed-point-subspace
  - projector
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the averaging trick in representation theory?"
  - "How does averaging produce G-invariant objects?"
---

# Quick Definition

Averaging over G is the technique of summing (1/|G|) sum_{g in G} over all group elements to produce G-invariant objects from arbitrary ones. It requires char(F) not dividing |G|.

# Core Definition

The **averaging technique** consists of replacing an object (bilinear form, projector, linear map) by its average over G. Key instances: (1) phi_bar(v,w) = sum_{g in G} phi(gv, gw) produces a G-invariant bilinear form (Lemma 7.6). (2) pi_bar(v) = (1/|G|) sum_{g in G} g(pi(g^{-1}v)) produces a G-invariant projector (p. 104). (3) The element pi = (1/|G|) sum_{a in G} a of F[G] is a projector onto the fixed-point subspace V^G (Lemma 7.49). (Milne, Chapter 7, pp. 103-104, 116)

# Prerequisites

- **Linear representation** — the group acts linearly
- **Group algebra** — averaging involves elements of F[G]

# Key Properties

1. Requires |G| to be invertible in F (char(F) does not divide |G|)
2. Produces G-invariant objects from arbitrary ones
3. The average of a projector with image W (G-invariant) is a G-invariant projector with image W
4. pi = (1/|G|) sum a is an idempotent in F[G] projecting onto fixed points

# Context & Application

Averaging over G is the fundamental technique in the representation theory of finite groups. It appears in:
- Both proofs of Maschke's theorem
- The construction of the Reynolds operator pi
- The dimension formula for V^G
- The proof of the orthogonality relations

# Relationships

## Builds Upon
- **linear-representation** — the group action
- **group-algebra** — pi = (1/|G|) sum a lives in F[G]

## Enables
- **maschke-theorem** — both proofs use averaging
- **fixed-point-subspace** — pi projects onto V^G
- **g-invariant-bilinear-form** — averaging creates invariant forms

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 103-104 (Maschke proofs) and p. 116 (Lemma 7.49).

# Verification Notes

- Definition source: Synthesized from multiple passages
- Confidence rationale: MEDIUM — not a single explicit definition but a recurring technique
- Uncertainties: None
