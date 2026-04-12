---
# === CORE IDENTIFICATION ===
concept: Image of a Homomorphism
slug: image-of-homomorphism

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Homomorphisms"
chapter_number: 16
pdf_page: 93
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\operatorname{im}(\\varphi)$"
  - "$\\varphi(G)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
extends: []
related:
  - kernel
  - first-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the image of a homomorphism?"
---

# Quick Definition

The image of a homomorphism $\varphi: G \to G'$ is the subgroup $\varphi(G) = \{\varphi(x) \mid x \in G\}$ of $G'$. By the First Isomorphism Theorem, $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$.

# Core Definition

A homomorphism $\varphi$ maps the whole group $G$ to a subgroup of $G'$ which is called the **image** of $\varphi$ (Armstrong, Ch. 16, p. 93).

# Prerequisites

- **Homomorphism** — The image is defined for a homomorphism

# Key Properties

1. The image is always a subgroup of $G'$
2. $\varphi$ is surjective iff $\operatorname{im}(\varphi) = G'$
3. By the First Isomorphism Theorem: $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$

# Construction / Recognition

## To Compute:
1. Given $\varphi: G \to G'$
2. Compute $\varphi(x)$ for all $x \in G$
3. The set of all such values is the image

# Context & Application

The image tells us "how much" of $G'$ is reached by $\varphi$. Together with the kernel, it completely determines the structure of $\varphi$ via the First Isomorphism Theorem.

# Examples

**Example 1** (p. 93): The natural map $G \to G/H$ has image $G/H$ (surjective) and kernel $H$.

**Example 2** (p. 94): $O_n \to \{\pm 1\}$, $A \mapsto \det A$ has image $\{\pm 1\}$ (surjective).

**Example 3** (p. 95): The homomorphism $\mathbb{H} - \{0\} \to SO_3$ via quaternion conjugation has image all of $SO_3$ (surjective).

# Relationships

## Builds Upon
- **Homomorphism** — Image is defined for a homomorphism

## Related
- **Kernel** — Kernel and image are the two fundamental invariants of a homomorphism
- **First isomorphism theorem** — Relates kernel and image

# Common Errors

- **Error**: Assuming the image is a normal subgroup of $G'$
  **Correction**: The image is a subgroup of $G'$ but not necessarily normal

# Common Confusions

- **Confusion**: Confusing the image with the codomain
  **Clarification**: The image may be a proper subgroup of $G'$. The homomorphism is surjective only when image equals codomain.

# Source Reference

Chapter 16: Homomorphisms, p. 93 (pdf).

# Verification Notes

- Definition source: Direct from p. 93
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
