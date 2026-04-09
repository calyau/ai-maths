---
# === CORE IDENTIFICATION ===
concept: Lie Functor
slug: lie-functor

# === CLASSIFICATION ===
category: lie-algebras
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 24
section: "3.3"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{Lie}(G)$"
  - "Lie group to Lie algebra correspondence"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - lie-algebra
  - lie-group-morphism
  - lie-algebra-morphism
extends: []
related:
  - first-fundamental-theorem
  - lie-third-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a Lie algebra relate to its Lie group?"
  - "What must I know before studying the structure theory of Lie algebras?"
---

# Quick Definition

The Lie functor assigns to each Lie group $G$ its Lie algebra $\mathrm{Lie}(G) = T_1G$ and to each Lie group morphism $\varphi$ the corresponding Lie algebra morphism $\varphi_*$. For connected $G_1$, $\mathrm{Hom}(G_1, G_2) \hookrightarrow \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$.

# Core Definition

**Theorem 3.17** (Kirillov): Let $G$ be a Lie group. Then $\mathfrak{g} = T_1G$ has a canonical structure of a Lie algebra; we write $\mathfrak{g} = \mathrm{Lie}(G)$. Every morphism of Lie groups $\varphi: G_1 \to G_2$ defines a morphism of Lie algebras $\varphi_*: \mathfrak{g}_1 \to \mathfrak{g}_2$, so we have a map $\mathrm{Hom}(G_1, G_2) \to \mathrm{Hom}(\mathfrak{g}_1, \mathfrak{g}_2)$; if $G_1$ is connected, then this map is injective.

# Prerequisites

- **Lie group** and **Lie algebra** — the objects
- **Lie group morphism** and **Lie algebra morphism** — the arrows

# Key Properties

1. $G \mapsto \mathrm{Lie}(G)$ is a functor from Lie groups to Lie algebras.
2. The map on Hom sets is injective for connected $G_1$.
3. The functor is surjective on objects (Lie's third theorem, Theorem 3.48).
4. The functor gives an equivalence between connected simply-connected Lie groups and finite-dimensional Lie algebras (Corollary 3.50).

# Construction / Recognition

## To Construct/Create:
1. $\mathrm{Lie}(G) = T_1G$ with bracket from equation (3.2).
2. For morphism $\varphi$, take $\varphi_* = d\varphi|_1$.

## To Identify/Recognize:
1. The assignment sending groups to algebras and group morphisms to algebra morphisms.

# Context & Application

The Lie functor is the central organizing principle of Lie theory. It reduces (many) questions about Lie groups to questions about Lie algebras, which are linear objects.

# Examples

**Example** (p. 22): $\mathrm{Lie}(\mathrm{GL}(n)) = \mathfrak{gl}(n)$, $\mathrm{Lie}(\mathrm{SU}(2)) = \mathfrak{su}(2)$, etc.

# Relationships

## Builds Upon
- **Lie group** and **Lie algebra** — domain and codomain
- **Lie group morphism** and **Lie algebra morphism** — maps

## Enables
- **Equivalence of categories** — for simply-connected groups (Corollary 3.50)

## Related
- **First fundamental theorem** — surjectivity on Hom for simply-connected groups
- **Lie's third theorem** — surjectivity on objects

# Common Errors

- **Error**: Thinking the Lie functor is an equivalence without the simply-connected assumption.
  **Correction**: Multiple non-isomorphic connected groups can have the same Lie algebra (e.g., $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$).

# Common Confusions

- **Confusion**: Whether the Lie functor is faithful (injective on Hom sets) without connectedness.
  **Clarification**: No. For disconnected $G_1$, different morphisms can induce the same map on Lie algebras.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.3, Theorem 3.17, page 24.

# Verification Notes

- Definition source: Synthesized from Theorem 3.17
- Confidence rationale: The term "Lie functor" is standard but not explicitly named in source
- Uncertainties: Terminology is synthesized
- Cross-reference status: Verified with Theorem 3.38, 3.48, Corollary 3.50
