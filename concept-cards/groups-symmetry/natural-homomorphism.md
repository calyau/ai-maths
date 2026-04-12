---
# === CORE IDENTIFICATION ===
concept: Natural Homomorphism
slug: natural-homomorphism

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
  - "canonical projection"
  - "quotient map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - quotient-group
  - homomorphism
extends: []
related:
  - kernel
  - first-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the natural homomorphism from G to G/H?"
  - "How does every normal subgroup arise as a kernel?"
---

# Quick Definition

For any normal subgroup $H$ of $G$, the function $\varphi: G \to G/H$ defined by $\varphi(x) = xH$ is a surjective homomorphism with kernel $H$. This connects every normal subgroup to a homomorphism.

# Core Definition

If $H$ is a normal subgroup of $G$, the function $\varphi: G \to G/H$ defined by $\varphi(x) = xH$ is a homomorphism because $\varphi(xy) = xyH = (xH)(yH) = \varphi(x)\varphi(y)$ for all $x, y \in G$. The image of this homomorphism is $G/H$ and its kernel is precisely $H$ (Armstrong, Ch. 16, p. 93).

# Prerequisites

- **Normal subgroup** — $H$ must be normal for $G/H$ to be a group
- **Quotient group** — The target of the natural homomorphism
- **Homomorphism** — The natural map is verified to be a homomorphism

# Key Properties

1. Always surjective (every coset $xH$ is hit)
2. Kernel is exactly $H$
3. This shows every normal subgroup is the kernel of some homomorphism
4. Combined with the First Isomorphism Theorem ($\ker(\varphi)$ is always normal), this gives: $H \triangleleft G$ iff $H = \ker(\varphi)$ for some homomorphism $\varphi$

# Construction / Recognition

## To Construct:
1. Start with $H \triangleleft G$
2. Define $\varphi(x) = xH$
3. This is a surjective homomorphism with kernel $H$

# Context & Application

Armstrong presents this immediately before the First Isomorphism Theorem to show that the quotient construction is a special case of the homomorphism framework. The natural homomorphism is the prototype for the theorem: $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$.

# Examples

**Example 1** (p. 93): For $H \triangleleft G$, $\varphi: G \to G/H$, $\varphi(x) = xH$, has image $G/H$ and kernel $H$.

# Relationships

## Builds Upon
- **Normal subgroup** — Required for the construction
- **Quotient group** — The codomain

## Enables
- **First isomorphism theorem** — The natural map is the canonical example

## Related
- **Kernel** — $H$ is the kernel of the natural map

# Common Errors

- **Error**: Defining $\varphi(x) = xH$ without checking $H$ is normal
  **Correction**: If $H$ is not normal, $G/H$ is not a group and $\varphi$ is not a homomorphism

# Common Confusions

- **Confusion**: Thinking the natural homomorphism is injective
  **Clarification**: It is surjective but generally not injective (kernel $= H$, which is non-trivial unless $H = \{e\}$)

# Source Reference

Chapter 16: Homomorphisms, p. 93 (pdf).

# Verification Notes

- Definition source: Direct from p. 93
- Confidence rationale: HIGH — explicit construction
- Uncertainties: None
