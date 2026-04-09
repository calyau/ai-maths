---
# === CORE IDENTIFICATION ===
concept: Kernel
slug: kernel

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 20
section: "Kernels and quotients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - kernel of a homomorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - normal-subgroup
extends: []
related:
  - image-of-homomorphism
  - quotient-group
  - factorization-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the kernel of a homomorphism relate to normal subgroups?"
  - "When is a homomorphism injective?"
---

# Quick Definition

The kernel of a homomorphism $\alpha: G \to G'$ is the set of elements in $G$ that map to the identity: $\mathrm{Ker}(\alpha) = \{g \in G \mid \alpha(g) = e\}$. It is always a normal subgroup.

# Core Definition

"The *kernel* of a homomorphism $\alpha: G \to G'$ is $\mathrm{Ker}(\alpha) = \{g \in G \mid \alpha(g) = e\}$." (Milne, p. 20)

"If $\alpha$ is injective, then $\mathrm{Ker}(\alpha) = \{e\}$. Conversely, if $\mathrm{Ker}(\alpha) = \{e\}$, then $\alpha$ is injective." (Milne, p. 20)

# Prerequisites

- **Homomorphism** — The kernel is defined for a homomorphism
- **Normal subgroup** — The kernel is always normal (Proposition 1.41)

# Key Properties

1. $\mathrm{Ker}(\alpha)$ is a normal subgroup of $G$ (Proposition 1.41)
2. $\alpha$ is injective $\iff$ $\mathrm{Ker}(\alpha) = \{e\}$
3. Every normal subgroup is the kernel of some homomorphism (Proposition 1.42)
4. The normal subgroups of $G$ are exactly the kernels of homomorphisms from $G$

# Construction / Recognition

## To Compute the Kernel:
1. Given $\alpha: G \to G'$, solve $\alpha(g) = e_{G'}$
2. The solution set is $\mathrm{Ker}(\alpha)$

## To Verify a Normal Subgroup is a Kernel:
- Every normal subgroup $N$ is the kernel of the canonical map $G \to G/N$

# Context & Application

The kernel is the central bridge between homomorphisms and normal subgroups. The fundamental relationship "normal subgroups = kernels" (Propositions 1.41 and 1.42) is one of the most important facts in group theory.

# Examples

**Example 1** (p. 20): The kernel of $\det: \mathrm{GL}_n(F) \to F^{\times}$ is $\mathrm{SL}_n(F)$, the special linear group of matrices with determinant 1.

**Example 2** (p. 20): The kernel of $g \mapsto gN: G \to G/N$ is exactly $N$.

# Relationships

## Builds Upon
- **homomorphism** — the kernel is defined for homomorphisms
- **normal-subgroup** — the kernel is always normal

## Enables
- **quotient-group** — $G/\mathrm{Ker}(\alpha)$ is the quotient
- **factorization-theorem** — $\alpha$ factors through $G/\mathrm{Ker}(\alpha)$

## Related
- **image-of-homomorphism** — kernel and image together describe a homomorphism

# Common Errors

- **Error**: Forgetting that the kernel is defined relative to a specific homomorphism
  **Correction**: Always specify which homomorphism's kernel is being discussed

# Common Confusions

- **Confusion**: Thinking any subgroup can be a kernel
  **Clarification**: Only normal subgroups can be kernels; this is precisely the content of Propositions 1.41 and 1.42

# Source Reference

Chapter 1, Section "Kernels and quotients", pages 20-21. Proposition 1.41 (kernel is normal), Proposition 1.42 (every normal subgroup is a kernel).

# Verification Notes

- Definition source: Direct quote from p. 20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified with Propositions 1.41, 1.42
- Uncertainties: None
