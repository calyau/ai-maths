---
# === CORE IDENTIFICATION ===
concept: Kernel of a Homomorphism
slug: kernel

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
  - "$\\ker(\\varphi)$"
  - "kernel"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
extends: []
related:
  - normal-subgroup
  - image-of-homomorphism
  - first-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the kernel of a homomorphism relate to normal subgroups?"
  - "What is the kernel of a homomorphism?"
---

# Quick Definition

The kernel of a homomorphism $\varphi: G \to G'$ is the set $K = \{x \in G \mid \varphi(x) = e'\}$ of elements mapped to the identity. The kernel is always a normal subgroup of $G$.

# Core Definition

The **kernel** $K$ of $\varphi$ is the set of those elements of $G$ which $\varphi$ maps to the identity of $G'$; in symbols $K = \{x \in G \mid \varphi(x) = e\}$ (Armstrong, Ch. 16, p. 93).

By the First Isomorphism Theorem (16.1), the kernel is always a normal subgroup of $G$. Conversely, every normal subgroup is the kernel of the natural projection $G \to G/H$.

# Prerequisites

- **Homomorphism** — The kernel is defined for a homomorphism

# Key Properties

1. $K$ is a subgroup of $G$: if $x, y \in K$ then $\varphi(xy^{-1}) = \varphi(x)\varphi(y)^{-1} = e$
2. $K$ is normal in $G$: $\varphi(gxg^{-1}) = \varphi(g)\varphi(x)\varphi(g)^{-1} = \varphi(g)\varphi(g)^{-1} = e$
3. $\varphi$ is injective iff $K = \{e\}$ (Corollary 16.3)
4. Every normal subgroup $H$ of $G$ is the kernel of the natural map $G \to G/H$
5. $G/K \cong \operatorname{im}(\varphi)$ (First Isomorphism Theorem)

# Construction / Recognition

## To Compute:
1. Given $\varphi: G \to G'$
2. Find all $x \in G$ with $\varphi(x) = e'$
3. This set is the kernel

# Context & Application

The kernel provides the fundamental link between homomorphisms and normal subgroups: a subgroup is normal if and only if it is the kernel of some homomorphism. This means studying normal subgroups and studying homomorphisms are equivalent endeavours.

# Examples

**Example 1** (p. 94): $\varphi: \mathbb{Z} \to \mathbb{Z}_n$, $x \mapsto x \pmod{n}$. Kernel: $n\mathbb{Z}$.

**Example 2** (p. 94): $\varphi: \mathbb{R} \to C$, $x \mapsto e^{2\pi i x}$. Kernel: $\mathbb{Z}$.

**Example 3** (p. 94): $\varphi: O_n \to \{\pm 1\}$, $A \mapsto \det A$. Kernel: $SO_n$.

**Example 4** (p. 94): $\varphi: C \to C$, $z \mapsto z^2$. Kernel: $\{\pm 1\}$.

**Example 5** (p. 95): $\varphi: S_4 \to S_3$ (conjugation action on double transpositions). Kernel: Klein four-group $V$.

# Relationships

## Builds Upon
- **Homomorphism** — Kernel is defined for a homomorphism

## Enables
- **First isomorphism theorem** — $G/K \cong \operatorname{im}(\varphi)$

## Related
- **Normal subgroup** — Every kernel is normal; every normal subgroup is a kernel
- **Image of a homomorphism** — The kernel and image together determine $\varphi$ up to the isomorphism theorem

# Common Errors

- **Error**: Computing the kernel as $\varphi^{-1}(\{e'\})$ and forgetting to verify it is a subgroup
  **Correction**: The kernel is always a subgroup (proved in Theorem 16.1), so if your computation gives something that is not a subgroup, you made an error

# Common Confusions

- **Confusion**: Thinking the kernel is a subgroup of $G'$
  **Clarification**: The kernel is a subgroup of $G$ (the domain), not $G'$ (the codomain)

# Source Reference

Chapter 16: Homomorphisms, pp. 93-95 (pdf). Definition, Theorem (16.1), Corollaries (16.2), (16.3).

# Verification Notes

- Definition source: Direct from p. 93
- Confidence rationale: HIGH — explicitly defined with proof of normality
- Uncertainties: None
