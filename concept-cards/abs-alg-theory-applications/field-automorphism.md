---
# === CORE IDENTIFICATION ===
concept: Field Automorphism
slug: field-automorphism

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.1 Field Automorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-field
  - isomorphism
extends: []
related:
  - galois-group
  - fixed-field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a field automorphism?"
  - "What distinguishes an inner automorphism from an outer automorphism?"
---

# Quick Definition

A field automorphism is an isomorphism from a field to itself. The set of all automorphisms of a field $F$ forms a group under composition, denoted $\operatorname{Aut}(F)$.

# Core Definition

The set of all automorphisms of a field $F$ is a group under composition of functions (Proposition 23.1, Judson, p. 307). If $E$ is a field extension of $F$, the automorphisms of $E$ that fix $F$ elementwise form a subgroup (Proposition 23.2).

# Prerequisites

- **Extension field** — Automorphisms are studied in the context of extensions
- **Isomorphism** — An automorphism is an isomorphism from a structure to itself

# Key Properties

1. The set of all automorphisms of $F$ forms a group $\operatorname{Aut}(F)$ (Proposition 23.1)
2. Automorphisms fixing a subfield $F$ form a subgroup of $\operatorname{Aut}(E)$ (Proposition 23.2)
3. Any automorphism in $G(E/F)$ permutes the roots of any polynomial in $F[x]$ (Proposition 23.5)
4. An automorphism is completely determined by its action on a set of generators of the extension
5. All field automorphisms are injective (nonzero homomorphisms of fields are injective)

# Context & Application

Field automorphisms are the bridge between field theory and group theory. The group of automorphisms of a field extension is the Galois group, which is the central object of Galois theory. Since fields are commutative, all field automorphisms are "outer" in the sense that there is no meaningful notion of inner automorphism for fields (unlike groups, where inner automorphisms arise from conjugation).

# Examples

**Example 1** (p. 307): Complex conjugation $\sigma(a + bi) = a - bi$ is an automorphism of $\mathbb{C}$ that fixes $\mathbb{R}$.

**Example 2** (p. 308): The map $\sigma(a + b\sqrt{3}) = a - b\sqrt{3}$ is an automorphism of $\mathbb{Q}(\sqrt{3}, \sqrt{5})$ fixing $\mathbb{Q}(\sqrt{5})$.

# Relationships

## Builds Upon
- **Extension field** — Automorphisms act on extensions
- **Isomorphism** — An automorphism is a self-isomorphism

## Enables
- **Galois group** — The group of automorphisms fixing the base field
- **Fixed field** — The subfield left fixed by a collection of automorphisms

# Common Confusions

- **Confusion**: Thinking fields can have "inner" automorphisms like groups do
  **Clarification**: Since fields are commutative, there is no conjugation action. The notion of inner vs. outer automorphism does not apply to fields in the same way it does to groups. All nontrivial field automorphisms are "outer" in the group-theoretic sense.

# Source Reference

Chapter 23: Galois Theory, Section 23.1, pages 307–308. See Propositions 23.1, 23.2, 23.5.

# Verification Notes

- Definition source: Direct from Propositions 23.1 and 23.2
- Confidence: HIGH — explicit propositions
- Cross-reference status: Verified
- Uncertainties: None
