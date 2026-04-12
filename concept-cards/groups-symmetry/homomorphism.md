---
# === CORE IDENTIFICATION ===
concept: Homomorphism
slug: homomorphism

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
  - "group homomorphism"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - kernel
  - image-of-homomorphism
  - isomorphism
  - first-isomorphism-theorem
contrasts_with:
  - isomorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a homomorphism?"
  - "What distinguishes a homomorphism from an isomorphism?"
---

# Quick Definition

A homomorphism from a group $G$ to a group $G'$ is a function $\varphi: G \to G'$ satisfying $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$. It preserves group structure but need not be bijective.

# Core Definition

Let $G, G'$ be groups. A function $\varphi: G \to G'$ is a **homomorphism** if it takes the multiplication of $G$ to that of $G'$; in other words if $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$ (Armstrong, Ch. 16, p. 93).

A homomorphism sends the identity of $G$ to the identity of $G'$, sends inverses to inverses, and sends each subgroup of $G$ to a subgroup of $G'$. If $\varphi$ is also a bijection, it is an isomorphism.

# Prerequisites

- **Group** — Source and target are groups

# Key Properties

1. $\varphi(e_G) = e_{G'}$
2. $\varphi(x^{-1}) = \varphi(x)^{-1}$
3. $\varphi$ maps subgroups of $G$ to subgroups of $G'$
4. The kernel $K = \{x \in G \mid \varphi(x) = e\}$ is a normal subgroup of $G$
5. The image $\varphi(G)$ is a subgroup of $G'$
6. $\varphi$ is injective iff $K = \{e\}$
7. The natural map $G \to G/H$ defined by $x \mapsto xH$ is always a homomorphism

# Construction / Recognition

## To Verify:
1. Define $\varphi: G \to G'$
2. Check $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$
3. If this holds, $\varphi$ is a homomorphism

# Context & Application

Armstrong notes that properties of isomorphisms proved in Chapter 7 that do not use bijectivity carry over to homomorphisms. The key new object associated with a homomorphism is its kernel, which connects homomorphisms to normal subgroups and quotient groups via the First Isomorphism Theorem.

# Examples

**Example 1** (p. 93): The natural map $\varphi: G \to G/H$ defined by $\varphi(x) = xH$ is a surjective homomorphism with kernel $H$.

**Example 2** (p. 94): $\mathbb{Z} \to \mathbb{Z}_n$, $x \mapsto x \pmod{n}$. Kernel is $n\mathbb{Z}$.

**Example 3** (p. 94): $\mathbb{R} \to C$, $x \mapsto e^{2\pi i x}$. Kernel is $\mathbb{Z}$.

**Example 4** (p. 94): $O_n \to \{\pm 1\}$, $A \mapsto \det A$. Kernel is $SO_n$.

# Relationships

## Enables
- **Kernel** — $\ker(\varphi)$ is always a normal subgroup
- **Image of a homomorphism** — $\varphi(G)$ is always a subgroup
- **First isomorphism theorem** — $G/\ker(\varphi) \cong \operatorname{im}(\varphi)$

## Related
- **Isomorphism** — A bijective homomorphism

## Contrasts With
- **Isomorphism** — An isomorphism is additionally bijective; a homomorphism can have non-trivial kernel and non-surjective image

# Common Errors

- **Error**: Assuming a homomorphism is injective
  **Correction**: A homomorphism is injective iff its kernel is trivial. Many important homomorphisms (e.g., $G \to G/H$) have large kernels.

# Common Confusions

- **Confusion**: Thinking "homomorphism" and "isomorphism" are synonyms
  **Clarification**: Every isomorphism is a homomorphism, but not vice versa. A homomorphism need not be bijective.

# Source Reference

Chapter 16: Homomorphisms, pp. 93-96 (pdf).

# Verification Notes

- Definition source: Direct from p. 93
- Confidence rationale: HIGH — explicitly defined
- Uncertainties: None
