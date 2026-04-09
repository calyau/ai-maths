---
# === CORE IDENTIFICATION ===
concept: Internal Direct Product
slug: direct-product-internal

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 23
section: "Direct products"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - internal direct product
  - direct product of subgroups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
extends: []
related:
  - direct-product-criteria
  - commutator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a group an internal direct product of subgroups?"
  - "What is the difference between internal and external direct products?"
---

# Quick Definition

A group $G$ is a direct product of subgroups $H_1, \ldots, H_k$ if the map $(h_1, \ldots, h_k) \mapsto h_1 \cdots h_k: H_1 \times \cdots \times H_k \to G$ is an isomorphism.

# Core Definition

"We say that $G$ is a **direct product** of the subgroups $H_i$ if the map $(h_1, h_2, \ldots, h_k) \mapsto h_1 h_2 \cdots h_k: H_1 \times H_2 \times \cdots \times H_k \to G$ is an isomorphism of groups." (Milne, p. 23)

This means each $g \in G$ can be written uniquely as $g = h_1 \cdots h_k$ with $h_i \in H_i$, and multiplication works componentwise.

# Prerequisites

- **Normal subgroup** — the factors must be normal in criteria for direct products

# Key Properties

1. Each element $g$ has a unique expression $g = h_1 \cdots h_k$
2. If $g = h_1 \cdots h_k$ and $g' = h'_1 \cdots h'_k$, then $gg' = (h_1h'_1) \cdots (h_kh'_k)$

# Construction / Recognition

See direct-product-criteria for the characterizations (Propositions 1.50-1.52).

# Context & Application

The internal direct product decomposes a group into simpler pieces. This is the basis for the structure theorem for finitely generated abelian groups.

# Examples

**Example 1** (p. 13): $D_2 = C_2 \times C_2$ (the Klein 4-group).

**Example 2**: $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ since $\gcd(2,3) = 1$.

# Relationships

## Builds Upon
- **normal-subgroup** — factors must be normal

## Enables
- **fundamental-theorem-finitely-generated-abelian-groups** — decomposes abelian groups

## Related
- **direct-product-criteria** — conditions ensuring a group is a direct product

# Source Reference

Chapter 1, Section "Direct products", pages 23-24. Propositions 1.50-1.52.

# Verification Notes

- Definition source: Direct from p. 23
- Confidence: HIGH — explicit definition
- Uncertainties: None
