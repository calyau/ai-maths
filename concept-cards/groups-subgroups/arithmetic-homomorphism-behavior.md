---
# === CORE IDENTIFICATION ===
concept: Behavior of Arithmetic Subgroups under Homomorphisms
slug: arithmetic-homomorphism-behavior

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
pdf_page: 400
section: "Behaviour with respect to homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arithmetic-subgroup
extends: []
related:
  - congruence-subgroup-problem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an arithmetic subgroup?"
  - "What distinguishes an isogeny from an isomorphism of algebraic groups?"
---

# Quick Definition

The image of an arithmetic subgroup under a homomorphism of algebraic groups is contained in an arithmetic subgroup of the target. Under a quotient map, the image is of finite index in an arithmetic subgroup. However, isogenies need not preserve the congruence property.

# Core Definition

Proposition 5.2 (Milne, p. 400): "Let $\varphi: G \to G'$ be a homomorphism of algebraic groups over $\mathbb{Q}$. For any arithmetic subgroup $\Gamma$ of $G(\mathbb{Q})$, $\varphi(\Gamma)$ is contained in an arithmetic subgroup of $G'(\mathbb{Q})$."

Remark 5.3: If $\varphi$ is a quotient map, then $\varphi(\Gamma)$ is of finite index in an arithmetic subgroup of $G'(\mathbb{Q})$, so arithmetic subgroups map to arithmetic subgroups.

Important contrast (Section 14): "The image of a congruence subgroup under an isogeny of algebraic groups need not be a congruence subgroup."

# Prerequisites

- **Arithmetic subgroup** — the objects being mapped

# Key Properties

1. Images of arithmetic subgroups under homomorphisms are contained in arithmetic subgroups (Proposition 5.2)
2. Under quotient maps, images are of finite index in arithmetic subgroups (Remark 5.3)
3. Since $\varphi(G(\mathbb{Q}))$ typically has infinite index in $G'(\mathbb{Q})$, the finite index statement is nontrivial
4. Congruence subgroups are *not* preserved by isogenies in general
5. This failure of congruence preservation is related to the congruence subgroup problem

# Construction / Recognition

## To Show $\varphi(\Gamma)$ is Arithmetic:
1. Let $\rho': G' \to \mathrm{GL}_V$ be faithful, $L$ a lattice
2. Find a lattice $L' \supset L$ stable under $(\rho' \circ \varphi)(\Gamma)$ (using Proposition 5.1)
3. Then $\varphi(\Gamma) \subset G'(\mathbb{Q})_{L'}$

# Context & Application

This functoriality of arithmetic subgroups is fundamental for the theory. The failure of congruence subgroups to be preserved under isogenies is a key point: it shows that the congruence subgroup problem is sensitive to the isogeny class, not just the isomorphism class, of the group.

# Examples

**Example 1** (p. 400): For $\varphi: G \to G'$ a quotient map and $\Gamma$ arithmetic in $G(\mathbb{Q})$: $\varphi(\Gamma)$ is of finite index in an arithmetic subgroup of $G'(\mathbb{Q})$ (Remark 5.3).

**Example 2** (p. 409): For $G$ simply connected and $G' = G/N$: the isogeny $G \to G'$ maps congruence subgroups to subgroups that may not be congruence.

# Relationships

## Builds Upon
- **Arithmetic subgroup** — the objects whose functoriality is studied

## Related
- **Congruence subgroup problem** — the failure of isogenies to preserve congruence subgroups motivates the CSP

# Common Errors

- **Error**: Assuming $\varphi(\Gamma)$ is always an arithmetic subgroup (not just contained in one)
  **Correction**: For general homomorphisms, $\varphi(\Gamma)$ is only *contained in* an arithmetic subgroup; for quotient maps, it has finite index in one

# Common Confusions

- **Confusion**: Thinking isogenies preserve congruence subgroups because they preserve arithmetic subgroups
  **Clarification**: Arithmetic and congruence behave differently: isogenies preserve arithmeticity but not the congruence property

# Source Reference

Chapter VII: Arithmetic Subgroups, Section 5, pages 400-401. Propositions 5.1, 5.2, Remark 5.3.

# Verification Notes

- Definition source: Propositions 5.1-5.2, Remark 5.3 from pp. 400-401
- Confidence: HIGH — explicit propositions
- Uncertainties: None
- Cross-reference status: Verified
